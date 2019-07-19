import speech_recognition as sr
import pyttsx3
import engineio
from os import system
from wit import Wit

access_token = "3PHPBZWHQOAIBLMANLLXOR33KWUKR6TR"

client = Wit(access_token)

if __name__ == '__main__':
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        recog_str = r.recognize_google(audio, language="e")
        wit_intent = client.message(recog_str)
        print(wit_intent)
        # system('say ' + recog_str)
