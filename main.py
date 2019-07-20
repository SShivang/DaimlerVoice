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

    return response

def WelcomeHandler(response):
    global application_started
    application_started = True
    system('say ' + response.query_result.fulfillment_text)

def ExitHandler(response):
    system('say ' + response.query_result.fulfillment_text)

if __name__ == '__main__':
    while True:
        global application_started
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        recog_str = r.recognize_google(audio, language = 'e', show_all=True)

        if (len(recog_str) != 0):
            transcriptList = recog_str['alternative']
            transcript = transcriptList[0]
            command = transcript['transcript']
            print(command)
            response = detect_intent_texts("daimlervoice-xadvoe", "AIzaSyAC8ja1pF9UmPId7MUZhbB8hAY8P_HWW7E", command , "en")
            if (response.query_result.intent.display_name == "Default Welcome Intent"):
                WelcomeHandler(response)
            if (application_started == True):
                if (response.query_result.intent.display_name == "Exit"):
                    ExitHandler(response)
                    break
