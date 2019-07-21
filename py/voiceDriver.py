import speech_recognition as sr
from os import system
import apiai
import os
from template import smartList, inventory, parts
from intentGlobals import GLOBAL_INTENTS, YES_INTENT, NOTE_INTENT, RUN_DIAGNOSTICS, NO_INTENT, PART_AVALIABLE, CUSTOMER_APPROVAL
import json

def detect_intent_texts(project_id, session_id, text, language_code):

    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(session=session, query_input=query_input)
    print(response)
    return response


mic = False
application_started = False

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
    # print(response)

    return response.query_result if response != 'empty response!' else command


def handle_global_intent(sio, response):
    if response.intent.display_name == NOTE_INTENT:
        handle_note(sio, response)
    else:
        print('No globals')

def getParts(sio, part_str):
    print("Looking for" + str(part_str))

    print("After looking at the database we found that there are " + str(inventory[part_str]) + " " + str(part_str))
    #Check how many of a certain part is avaliable

def contactCustomer(sio):
    print("Calling customer")
    #Need to check the last diagnostic this person ran and check the parts not in warranty
    
    #Twilio

def runDiagnostics(sio):
    print('Running some diagnostics')
    state = smartList[1]
    while state['Step'] != 0:
        print(state['Text'])
        response = get_intent(sio)
        if(response.intent.display_name in GLOBAL_INTENTS):
            handle_global_intent(sio, response)
        if (response.intent.display_name == YES_INTENT):
            state = smartList[state['YES']]
        if (response.intent.display_name == NO_INTENT):
            state = smartList[state['NO']]


    print('diagnostics are over')


from globalActions import handle_note

def runDriver(sio):
    global mic
    print('Use microphone ? (y/n)')
    textInput = raw_input()
    if textInput == 'y':
        mic = True

    #if any part is not in stock ask if you want to order it

    while True:
        temp = get_intent(textInput)
        state = {
            'done' : False
        }
        if (temp.intent.display_name == RUN_DIAGNOSTICS):
            runDiagnostics(sio)

        if (temp.intent.display_name == PART_AVALIABLE):
            parameter = temp.parameters.fields['part'].string_value
            getParts(sio, parameter)

        if (temp.intent.display_name == CUSTOMER_APPROVAL):
            contactCustomer(sio)

    sio.disconnect()
