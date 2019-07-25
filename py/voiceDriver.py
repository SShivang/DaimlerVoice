import speech_recognition as sr
from gtts import gTTS
from os import system
import apiai
import os
from template import smartList, inventory, parts
from intentGlobals import CONFUSED, GLOBAL_INTENTS, YES_INTENT, NOTE_INTENT, \
RUN_DIAGNOSTICS, NO_INTENT, PART_AVALIABLE, CUSTOMER_APPROVAL, GO_BACK, EXIT, \
REPORT_INTENT, NUMBER_INTENT, THRESHOLD
import json
from twilio.twiml.voice_response import VoiceResponse, Say


def detect_intent_texts(project_id, session_id, text, language_code):

    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(session=session, query_input=query_input)
    return response



mic = False
application_started = False

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


def textToSpeech(text):
    global mic
    print('Audiating: %s', text)
    if mic:
        tts = gTTS(text=text, lang="en")
        file='my.mp3'
        tts.save(file)
        os.system("mpg123 -d 3 -h 2 " + file)


# # def output(str):
#     global mic
#     if (!mic)
#         print("Looking for" + str(part_str))
#     else
#         system(say + " " + "Looking for" + str(part_str))


def get_intent(sio):
    global application_started
    global mic
    response = 'empty response!'
    command = 'default'
    if mic:
        raw_input()
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print('listening...')
            audio = r.listen(source)
            print('interpreting...')
            recog_str = r.recognize_google(audio, language = 'e', show_all=True)
            print('Done')
            print('You said: %s', recog_str)

            if (len(recog_str) != 0):
                transcriptList = recog_str['alternative']
                transcript = transcriptList[0]
                command = transcript['transcript']
                print('command is: ')
                print(command)
                response = detect_intent_texts("daimlervoice-xadvoe", "AIzaSyAC8ja1pF9UmPId7MUZhbB8hAY8P_HWW7E", command , "en")
    else:
        print('enter next command')
        command = raw_input()
        response = detect_intent_texts("daimlervoice-xadvoe", "AIzaSyAC8ja1pF9UmPId7MUZhbB8hAY8P_HWW7E", command , "en")
    print('RETURN FROM GET INTENT')
    result = response.query_result if response != 'empty response!' else command
    print(result)
    return result

from globalActions import handle_note, handle_report


def handle_global_intent(sio, response):
    if response.intent.display_name == NOTE_INTENT:
        handle_note(sio, response)
    elif response.intent.display_name == REPORT_INTENT:
        handle_report(sio)
    else:
        print('No globals')

# def getParts(sio, part_str):

#     # output("Looking for" + str(part_str))
#     # output("After looking at the database we found that there are " + str(inventory[part_str]) + " " + str(part_str))
#     #Check how many of a certain part is avaliable

def contactCustomer(sio):
    textToSpeech("Calling customer")
    account_sid = 'AC0b7ae2e58a61e02e5e18bd892184ce7d'
    auth_token = 'a71f1eca611b70a7de31f526e5ec9f82'
    client = Client(account_sid, auth_token)
    call = client.calls.create(url = 'http://e7b6441d.ngrok.io/', to='+15129684998', from_='+17372048501')

def sendSMSForInvoicing(sio):
    textToSpeech("Calling customer")
    account_sid = 'AC0b7ae2e58a61e02e5e18bd892184ce7d'
    auth_token = 'a71f1eca611b70a7de31f526e5ec9f82'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                              body='After examining all the parts total estimation for this procedure is $1200',
                              from_='+17372048501',
                              to='+15129684998'
                          )
    # call = client.calls.create(url = 'https://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient', to='+15129684998', from_='+17372048501')

    print("Calling customer")
   
def runDiagnostics(sio):
    # output('Running some diagnostics')
    state = smartList[1]
    last_resp = ''
    while state['Step'] != 0:
        print(state)
        sio.emit('local', {'view': 'DIAG', 'text': state['Text'], 'table': state['Display-table'], 'prev': last_resp})
        textToSpeech(state['Text'])
        response = get_intent(sio)
        if not hasattr(response, "intent"): continue
        while(hasattr(response, "intent") and response.intent.display_name in GLOBAL_INTENTS):
            handle_global_intent(sio, response)
            response=get_intent(sio)
        if(response.intent.display_name == CONFUSED):
            continue
        elif(response.intent.display_name == NUMBER_INTENT):
            number_val= response.parameters.fields['number'].number_value
            stat=state['YES_STAT'] if number_val < THRESHOLD else state['NO_STAT']
            last_resp += stat + '  Voltage recorded: ' + str(number_val)
            state = smartList[state['YES']] if number_val < THRESHOLD else smartList[state['NO']]
        elif (response.intent.display_name == YES_INTENT):
            last_resp += state['YES_STAT'] if 'YES_STAT' in state else ''
            state = smartList[state['YES']]
        elif (response.intent.display_name == NO_INTENT):
            last_resp += state['NO_STAT'] if 'NO_STAT' in state else ''
            state = smartList[state['NO']]
    textToSpeech("A sample parts directory was generated and sent to parts department")
    sendSMSForInvoicing(sio)
    textToSpeech("Some parts are not covered by warranty would you like to get approval")
    s = get_intent(sio)
    if (s.intent.display_name):
        contactCustomer(sio)
    textToSpeech("An invoice for the procedure was sent")
    while True:
        sio.emit('local', {'view': 'DIAG', 'text': state['Text']})
        response = get_intent(sio)
        if not hasattr(response, "intent"): continue
        if response.intent.display_name == YES_INTENT or response.intent.display_name == GO_BACK :
            sio.emit('local', {'view': 'MAIN'})
            break

from globalActions import handle_note

def runDriver(sio):
    global mic
    print('Use microphone ? (y/n)')
    textInput = raw_input()
    if textInput == 'y':
        mic = True

    #if any part is not in stock ask if you want to order it
    INIT=True
    while True:
        state = {
            'done' : False
        }
        textToSpeech("What do you want to do? Look at the options below")
        if INIT: textToSpeech("Inventory scan completed. Some parts need to be restocked.")
        INIT = False
        response = get_intent(textInput)
        if not hasattr(response, "intent"): continue
        if(response.intent.display_name in GLOBAL_INTENTS):
            handle_global_intent(sio, response)
            response = get_intent(sio)
        if (response.intent.display_name == RUN_DIAGNOSTICS):
            runDiagnostics(sio)
        elif (response.intent.display_name == PART_AVALIABLE):
            parameter = response.parameters.fields['part'].string_value
            # getParts(sio, parameter)
        elif (response.intent.display_name == CUSTOMER_APPROVAL):
            contactCustomer(sio)
        elif (response.intent.display_name == EXIT):
            # output('Exiting...')
            sio.disconnect()
            break

    sio.disconnect()
