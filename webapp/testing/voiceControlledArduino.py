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
	r.energy_threshold = 2500
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



	userInput = input("enter 1 to capture voice or 2 to quit: ")
	if userInput == "1":
		print("listening to your voice now!")
		voiceInput = get_audio()
		print(f"You said{voiceInput}")

		if "relay on" in voiceInput:
			# print("Red has been turned on bro")		
			# for x in range(5):
			sendSerial('A')
		elif "relay off" in voiceInput:
			sendSerial('a')
		elif "red light on" in voiceInput:
			sendSerial('B')
		elif "red light off" in voiceInput:
			sendSerial('b')







	elif userInput == "2":
		ser.close()
		print("thanks for using bro!!!")
		break


