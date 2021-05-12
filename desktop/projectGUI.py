import tkinter as tk
import time
import pygame
import serial
from subprocess import *
ser = serial.Serial('COM3',9600)

window = tk.Tk()

led_green = False
led_blue = False

class buttonToggle:
	def __init__(ledColour,onMsg,offMsg):
		ledColour.onMsg = onMsg
		ledColour.offMsg = offMsg
		ledColour.state = False

	def toggleState(ledColour):
		ledColour.state = not ledColour.state

	def sendMsg(ledColour):
		if ledColour.state == True:
			sendSerial(ledColour.onMsg)
		else:
			sendSerial(ledColour.offMsg)


myRedButton = buttonToggle("A","a")
myGreenButton = buttonToggle("B","b")
myBlueButton = buttonToggle("C","c")

def redClick():
	myRedButton.toggleState()
	myRedButton.sendMsg()

def greenClick():
    myGreenButton.toggleState()
    myGreenButton.sendMsg()

def blueClick():
    myBlueButton.toggleState()
    myBlueButton.sendMsg() 



def sendSerial(messageChar):
    if(ser.in_waiting > 0):
        toArduino = messageChar
        toArduinoEncode = toArduino.encode()
        ser.write(toArduinoEncode)

def getSerial():
    if(ser.in_waiting > 0):
        line = ser.readline()
        #print(line)
        return line.decode()

    else:
        return ""

def parseSerialInput():
    rawStr = getSerial()

    message = rawStr[0:-2]
    return message


def sendString(messageStr):
	if messageStr != "":
		sendSerial("%")
		print("%")
		for character in messageStr:
			sendSerial(character)
			print(character)		
		sendSerial("*")
		print("*")
	else:
		sendSerial("%")
		for x in range(8):
			sendSerial(" ")
		sendSerial("*")
	#parseSerialInput()
	  

def lcdClick():
	toLcd = lcdEntry.get()
	lcdEntry.delete(0,tk.END)
	
	sendString(toLcd)

def getSensorData():
	fromPi = getSerial()	
	#print (fromPi)

	humidityValue = fromPi[10:13]
	tempOutputValue = fromPi[5:10]
	soilMoistureValue = fromPi[0:5]

	humidityOutputLabel.config(text="Humidity " + str(soilMoistureValue) + "%")
	tempOutputLabel.config(text="Temperature " + str(tempOutputValue) + "C")
	soilMoisture.config(text="Soil Moisture " + str(humidityValue) + "%")

	window.after(150,getSensorData)





titleFrame = tk.Frame()

window.title("Adam GUI")




title = tk.Label(master = titleFrame,text="Adam GUI")
title.pack()


ledButtonFrame = tk.Frame()


redButton = tk.Button(master = ledButtonFrame,text="RED",width=25, height=5, bg="#FF0000", fg="black",command=redClick )
redButton.pack()

greenButton = tk.Button(master = ledButtonFrame,text="GREEN",width=25, height=5, bg="#32CD32", fg="black",command=greenClick )
greenButton.pack()

blueButton = tk.Button(master = ledButtonFrame,text="BLUE",width=25, height=5, bg="#87CEEB", fg="black",command=blueClick)
blueButton.pack()



lcdFrame = tk.Frame()

lcdLabel = tk.Label(master = lcdFrame,text="Enter in for LCD")
lcdLabel.pack()

lcdEntry = tk.Entry(master = lcdFrame,width=30)
lcdEntry.pack()

lcdButton = tk.Button(master = lcdFrame,text="SEND TO LCD",width=25, height=5, bg="#FCFD00", fg="black",command=lcdClick)
lcdButton.pack()



sensorDataFrame = tk.Frame()

sensorTitleLabel = tk.Label(master = sensorDataFrame,text="Sensor Data")
sensorTitleLabel.pack()

humidityOutputLabel = tk.Label(master = sensorDataFrame,text="Humidity")
humidityOutputLabel.pack()

tempOutputLabel = tk.Label(master = sensorDataFrame,text ="Temperature")
tempOutputLabel.pack()

soilMoisture = tk.Label(master = sensorDataFrame,text="Soil Moisture")
soilMoisture.pack()


titleFrame.pack()
ledButtonFrame.pack()
lcdFrame.pack()
sensorDataFrame.pack()

window.after(150,getSensorData)
#window.after()

window.mainloop()
