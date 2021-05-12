from flask import Flask,render_template, request, redirect, url_for
import logging
# from objects import buttonToggle
import time
from subprocess import *
import threading
from threading import Thread
from queue import Queue
import serial
import logging
import sys
import sched
import random
import collections	

class buttonToggle:
	def __init__(ledColour,onMsg,offMsg):
		ledColour.onMsg = onMsg
		ledColour.offMsg = offMsg
		ledColour.state = False

	def toggleState(ledColour):
		ledColour.state = not ledColour.state
	def reset(ledColour):
		ledColour.state = False

class serialPort:
	def __init__(self,port):

		def initializeSerialFunc(comsTypeQue,tData,hData,smData):
			def pullSensors():
				print("bruh")

			while True:
				# ser = serial.Serial('COM3',19200)
				try:
					print("Connecting to Arduino")
					ser = serial.Serial('COM3',9600,timeout=1)
					time.sleep(1)
					# ser.close()
					# ser.open()
				except:
					print("Error Connecting to Arduino")
					time.sleep(1)

				else:
					print("Arduino is Connected")
					# pullTimer = threading.Timer(0.0,pullSensors)
					# pullTimer.start()
					break
			
			while True:

				#get anything that is beong sent to the arduino
				toArduino = "null"

				# print(time_start)
				# print(time.time())
				
				# if(ser.in_waiting > 0):
				# 	line = ser.readline()
				# 	print(line.decode())

				if not comsTypeQue.empty():
					
					toArduino = comsTypeQue.get()					
					print(toArduino)
					if toArduino != "null":
						if toArduino == "RESET":
							print("RESETTING ARDUINO")
							
							ser.close()
							ser.open()
							time.sleep(1)													
						
						elif toArduino == "SENSOR":
							
							for x in range(1):
								if(ser.in_waiting > 0):
									line = ser.readline()
									print(line.decode())
								# 	# time.sleep(0.5)	

						elif toArduino[0] == "%" and toArduino[-1] == "*":		
							if(ser.in_waiting > 0):
								toArduinoEncode = toArduino.encode()
								ser.write(toArduinoEncode)

						
						elif ser.in_waiting > 0:
							toArduinoEncode = toArduino.encode()
							ser.write(toArduinoEncode)
					time.sleep(1)
				else:
					if(ser.in_waiting > 0):
						line = ser.readline()
						lineDecoded = line.decode()

						humidityValue = lineDecoded[10:13]
						tempOutputValue = lineDecoded[5:10]
						soilMoistureValue = lineDecoded[0:5]

						tData.append(tempOutputValue)
						hData.append(humidityValue)
						smData.append(soilMoistureValue)

						time.sleep(0.15)
			
		self.port = port
		self.comsTypeQue = Queue()
		self.tData=collections.deque(maxlen=1)
		self.hData=collections.deque(maxlen=1)
		self.smData=collections.deque(maxlen=1)
		self.thread = threading.Thread(target =initializeSerialFunc,args =(self.comsTypeQue,self.tData,self.hData,self.smData))
		
		# self.timerThread = threading.Thread()

	def initializeSerial(self):
		self.thread.start()
		pass
		# time.sleep(2)
	def reset(self):		
		# self.thread.join()
		myPort.led("RESET")
	

	def led(self,toArd):
		self.comsTypeQue.put(toArd) 

	def toLcd(self,string):
		string = "%" + string + "*"
		self.led(string)
	def lcdClear(self):
		self.toLcd(" ")

def getSensor(q):
	while True:
		try:
			data = q.popleft()
			return data
		except IndexError:
			pass
		else:			
			return data

app = Flask(__name__)

myPort = serialPort('COM3')
myPort.initializeSerial()

redButton = buttonToggle("A","a")
greenButton = buttonToggle("B","b")
blueButton = buttonToggle("C","c")

@app.route("/temperature", methods = ["POST","GET"])
def temperature():
	data = getSensor(myPort.tData)
	return str(data);

@app.route("/humidity", methods = ["POST","GET"])
def humidity():
	data = getSensor(myPort.hData)
	return str(data);

@app.route("/soilmoisture", methods= ["POST","GET"])
def soilmoisture():
	data = getSensor(myPort.smData)

	return str(data);

@app.route("/",methods = ["POST","GET"])
def home():

	if request.method == "POST":
		user = ""
		lcdText = ""
		try: 
			user = request.form["led-button"]
		except:
			lcdText = request.form["lcd"]
		
		if user == "RED_BUTTON":			
			redButton.toggleState()
			if redButton.state == True:
				myPort.led(redButton.onMsg)			
			else:
				myPort.led(redButton.offMsg)
		elif user == "GREEN_BUTTON":
			greenButton.toggleState()
			if greenButton.state == True:
				myPort.led(greenButton.onMsg)			
			else:
				myPort.led(greenButton.offMsg)
		elif user == "BLUE_BUTTON":
			blueButton.toggleState()
			if blueButton.state == True:
				myPort.led(blueButton.onMsg)			
			else:
				myPort.led(blueButton.offMsg)

		elif user == "RESET":
			myPort.reset()
			redButton.reset()
			blueButton.reset()
			greenButton.reset()
		elif user == "SENSOR":
			myPort.led(user)

		else:
			myPort.toLcd(lcdText)

		return render_template("interface.html")
	else:
		return render_template("interface.html")

if __name__ =="__main__":
	app.run(port=8082,debug = True)