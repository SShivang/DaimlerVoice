import speech_recognition as sr
from os import system
import apiai
import os
from intentGlobals import GLOBAL_INTENTS, YES_INTENT, NOTE_INTENT, RUN_DIAGNOSTICS, NO_INTENT
from globalActions import handle_note


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
    if mic:
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
    print(response)
    
    return response.query_result if response != 'empty response!' else None





def handle_global_intent(sio, response):
    if response.intent.display_name == NOTE_INTENT:
        handle_note(sio, response)
    else:
        print('No globals')


def handle_step3(sio, cur_state):
    print('Check the gasoline')
    return {
        'next_handler': main_menu,
        'done': False
    }



def handle_step2(sio, cur_state):
    print('Check the gasoline')
    return {
        'next_handler': main_menu,
        'done': False
    }



def handle_step1(sio, cur_state):
    print('Is the truck on?')
    while True:
        print('beginning step 1')

        response = get_intent(sio)
        if not response: continue
        if(response.intent.display_name in GLOBAL_INTENTS):
            handle_global_intent(sio, response)
        elif response.intent.display_name == YES_INTENT:
            print('exit step 1')
            # add_to_db(step1info)
            return {
                'next_handler' : handle_step2,
                'done' : cur_state['done']
            }

        elif response.intent.display_name == NO_INTENT:
            return {
                'next_handler' : handle_step3,
                'done' : False
            }
        else:
            print('input not accepted')
        

def main_menu(sio, cur_state):
    print('Welcome to the diagnostic tool. What would you like to do?')
    while True:
        response = get_intent(sio)
        if not response: continue
        if(response.intent.display_name in GLOBAL_INTENTS):
            handle_global_intent(sio, response)
        elif response.intent.display_name == RUN_DIAGNOSTICS:
            # add_to_db(step1info)
            return {
                'next_handler' : handle_step1,
                'done' : cur_state['done']
            }
        else:
            print('input not accepted')



state = {
    'next_handler' : main_menu,
    'done': False
}

def runDriver(sio):
    global mic
    global state
    print('Use microphone ? (y/n)')
    textInput = raw_input()
    if textInput == 'y':
        mic = True
    while not state['done']:
        state = state['next_handler'](sio, state)

    sio.disconnect()


# def testDriver(sio):
#     global application_started
#     print('Use microphone ? (y/n)')
#     textInput = raw_input()
#     with sr.Microphone() as source:
#         while True:
#             if textInput == 'y':
#                 r = sr.Recognizer()
#                 r.adjust_for_ambient_noise(source)
#                 print('listening:')
#                 audio = r.listen(source)
#                 print('interpreting:')
#                 recog_str = r.recognize_google(audio, language = 'e', show_all=True)
#                 print('Done')

#                 if (len(recog_str) != 0):
#                     transcriptList = recog_str['alternative']
#                     transcript = transcriptList[0]
#                     command = transcript['transcript']
#                     print('command is: ')
#                     print(command)
#                     response = detect_intent_texts("daimlervoice-xadvoe", "AIzaSyAC8ja1pF9UmPId7MUZhbB8hAY8P_HWW7E", command , "en")
#                     web_text = response.query_result.parameters.fields['displayText'].string_value
#                     sio.emit('voice', { 'data': web_text })
                    
#             else:
#                 print('enter next command')
#                 command = raw_input()
#                 response = detect_intent_texts("daimlervoice-xadvoe", "AIzaSyAC8ja1pF9UmPId7MUZhbB8hAY8P_HWW7E", command , "en")
#                 web_text = response.query_result.parameters.fields['displayText'].string_value
#                 sio.emit('voice', { 'data': web_text })


        
