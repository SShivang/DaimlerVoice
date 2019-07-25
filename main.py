import speech_recognition as sr
from os import system
import apiai

import os

application_started = False

def detect_intent_texts(project_id, session_id, text, language_code):

    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
            session=session, query_input=query_input)

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))
<<<<<<< HEAD
<<<<<<< HEAD

detect_intent_texts("daimlervoice-xadvoe", "AIzaSyAC8ja1pF9UmPId7MUZhbB8hAY8P_HWW7E", ["Call Bob"], "en")




        # system('say ' + recog_str)

#I'M PRACTICING GITHUB FROM STEVE
=======
=======
>>>>>>> df1e0c47283670dd46586852a8f1d7219f2e9d94
    return response

def WelcomeHandler(response):
    global application_started
    application_started = True
    system('say ' + response.query_result.fulfillment_text)

def ExitHandler(response):
    system('say ' + response.query_result.fulfillment_text)

# detect_intent_texts("daimlervoice-xadvoe", "AIzaSyAC8ja1pF9UmPId7MUZhbB8hAY8P_HWW7E", "command" , "en")

if __name__ == '__main__':
    print("Hello")
    global application_started
    print('Use microphone ? (y/n)')
    textInput = raw_input()
    with sr.Microphone() as source:
        while True:
            if textInput == 'y':
                r = sr.Recognizer()
                r.adjust_for_ambient_noise(source)
                print('listening:')
                audio = r.listen(source)
                print('interpreting:')
                recog_str = r.recognize_google(audio, language = 'e', show_all=True)
                print('Done')

                if (len(recog_str) != 0):
                    transcriptList = recog_str['alternative']
                    transcript = transcriptList[0]
                    command = transcript['transcript']
                    print('command is: ')
                    print(command)
                    response = detect_intent_texts("daimlervoice-xadvoe", "AIzaSyAC8ja1pF9UmPId7MUZhbB8hAY8P_HWW7E", command , "en")
                    web_text = response.query_result.parameters.fields['displayText'].string_value
                    #sio.emit('voice', { 'data': web_text })
            else:
                print('enter next command')
                command = raw_input()
                response = detect_intent_texts("daimlervoice-xadvoe", "AIzaSyAC8ja1pF9UmPId7MUZhbB8hAY8P_HWW7E", command , "en")
                return response
<<<<<<< HEAD
>>>>>>> df1e0c47283670dd46586852a8f1d7219f2e9d94
=======
>>>>>>> df1e0c47283670dd46586852a8f1d7219f2e9d94
