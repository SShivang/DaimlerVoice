import speech_recognition as sr
from gtts import gTTS
from os import system
import apiai
import os
from template import smartList
from intentGlobals import CONFUSED, GLOBAL_INTENTS, YES_INTENT, NOTE_INTENT, \
RUN_DIAGNOSTICS, NO_INTENT, PART_AVALIABLE, CUSTOMER_APPROVAL, GO_BACK, EXIT, \
REPORT_INTENT
import json



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

def textToSpeech(text):
    global mic
    print('Audiating: %s', text)
    if mic:
        tts = gTTS(text=text, lang="en")
        file='my.mp3'
        tts.save(file)
        os.system("mpg123 " + file)


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

def getParts(sio, part_str):
    print("Looking for" + str(part_str))

    #Check how many of a certain part is avaliable

def contactCustomer(sio):
    print("Calling customer")
    #Need to check the last diagnostic this person ran and check the parts not in warranty

    #Twilio

def runDiagnostics(sio):
    print('Running some diagnostics')
    state = smartList[1]
    last_resp = ''
    while state['Step'] != 0:
        print(state)
        sio.emit('local', {'view': 'DIAG', 'text': state['Text'], 'table': state['Display-table'], 'prev': last_resp})
        textToSpeech(state['Text'])
        response = get_intent(sio)
        if not hasattr(response, "intent"): continue
        if(response.intent.display_name in GLOBAL_INTENTS):
            handle_global_intent(sio, response)
        if(response.intent.display_name == CONFUSED):
            continue
        elif (response.intent.display_name == YES_INTENT):
            last_resp = state['YES_STAT']
            state = smartList[state['YES']]
        elif (response.intent.display_name == NO_INTENT):
            state = smartList[state['NO']]
    while True:
        sio.emit('local', {'view': 'DIAG', 'text': state['Text']})
        response = get_intent(sio)
        if not hasattr(response, "intent"): continue
        if response.intent.display_name == YES_INTENT or response.intent.display_name == GO_BACK :
            sio.emit('local', {'view': 'MAIN'})
            break

    
    print('diagnostics are over')

def runDriver(sio):
    global mic
    print('Use microphone ? (y/n)')
    textInput = raw_input()
    if textInput == 'y':
        mic = True

    #if any part is not in stock ask if you want to order it

    while True:
        state = {
            'done' : False
        }
        textToSpeech("What do you want to do? Look at the options below")
        response = get_intent(textInput)
        if not hasattr(response, "intent"): continue
        if(response.intent.display_name in GLOBAL_INTENTS):
            handle_global_intent(sio, response)
        elif (response.intent.display_name == RUN_DIAGNOSTICS):
            runDiagnostics(sio)
        

        elif (response.intent.display_name == PART_AVALIABLE):
            parameter = response.parameters.fields['part'].string_value
            getParts(sio, parameter)

        elif (response.intent.display_name == CUSTOMER_APPROVAL):
            contactCustomer(sio)
        elif (response.intent.display_name == EXIT):
            print('Exiting...')
            sio.disconnect()
            break



    sio.disconnect()
