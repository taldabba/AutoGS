import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS





def get_audio():
	r = sr.Recognizer()
	r.energy_threshold = 2000
	with sr.Microphone() as source:
		audio = r.listen(source)

		said = ""

		try: 
			said = r.recognize_google(audio)
			print(said)
		except Exception as e:
			print("Exception" + str(e))

	return said


def speak(text):
	tts = gTTS(text=text,lang="en")
	filename = "voice.mp3"
	tts.save(filename)
	playsound.playsound(filename)




speak("hello")
string = get_audio()
if "callum" in string:
	print("bruh")
