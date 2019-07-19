import speech_recognition as sr
import pyttsx
from os import system
import apiai

import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/ShivangWork/Desktop/daimlerVoice-d9756f7ed4c9.json"

application_started = False

def apiaiCon():
    access_token = "3b4ddf53dd4548f880610288c23d1b52"


# if __name__ == '__main__':
#     while True:
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             r.adjust_for_ambient_noise(source)
#             system('say ' + 'What is your command')
#             audio = r.listen(source)
#         recog_str = r.recognize_google(audio, language = 'e', show_all=True)
#
#         if (len(recog_str) != 0):
#             transcriptList = recog_str['alternative']
#             transcript = transcriptList[0]
#             command = transcript['transcript']
#             print(command)


def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""

    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    for text in texts:
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

detect_intent_texts("daimlervoice-xadvoe", "AIzaSyAC8ja1pF9UmPId7MUZhbB8hAY8P_HWW7E", ["Call Bob"], "en")




        # system('say ' + recog_str)
