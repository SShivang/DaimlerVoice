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

if __name__ == '__main__':
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        recog_str = r.recognize_google(audio, language = 'e')
        detect_intent_texts("daimlervoice-xadvoe", "AIzaSyAC8ja1pF9UmPId7MUZhbB8hAY8P_HWW7E", recog_str , "en")
