import serial
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


ser = serial.Serial('COM3',9600,timeout=1)

def sendSerial(messageChar):
    if(ser.in_waiting > 0):
        toArduino = messageChar
        toArduinoEncode = toArduino.encode()
        ser.write(toArduinoEncode)


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


while True:
	voiceInput = get_audio()
	if "red light on" in voiceInput:
		# print("Red has been turned on bro")		
		# for x in range(5):
		sendSerial('A')
	elif "red light off" in voiceInput:
		sendSerial('a')
	elif "blue light on" in voiceInput:
		sendSerial('B')
	elif "blue light off" in voiceInput:
		sendSerial('b')

