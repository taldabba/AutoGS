import time
from subprocess import *
import threading
from threading import Thread
from collections import deque 
from queue import Queue
import serial
import logging
import sys
import sched
import random
import collections
import speech_recognition
import pyttsx3

def consoleThreadFunc():
	while True:
		userInput = input("Enter y to let me listen to your voice: ")
		if userInput == "y":
			pass

def voiceListenerFunc():
	while True:
		try:
			with speech_recognition.Microphone() as mic:

				recognizer.adjust_for_ambient_noise(mic,duration = 0.2)
				audio = recognizer.listen(mic)

				text = recognizer.recognize_google(audio)
				text = text.lower()

				print(f"Recognized {text}")


		except:

			recognizer = speech_recognition.Recognizer()

			continue



textFeed = collections.deque(maxlen=1)
consoleThreadFunc = threading.Thread(target=consoleThreadFunc,args=(textFeed))
voiceListenerThread = threading.Thread(target=voiceListenerFunc)


voiceListenerFunc()



# voiceListenerThread.start()"C:\Users\adami\Downloads\PyAudio-0.2.11-cp39-cp39-win_amd64.whl"