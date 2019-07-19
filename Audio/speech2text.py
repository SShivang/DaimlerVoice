

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

r = sr.Recognizer()


with sr.Microphone() as source: 
		print("SPEAK...")
		audio = r.listen(source)

		try:
			text = r.recognize_google(audio)
			print("You said {}".format(text))
		except:
			print("Sorry, WHAT YOU SAIDDD?!?")	

text = "Hello, this is a test"
engine.say("You said {}".format(text))
engine.runAndWait()



