import serial
import time
import threading
import collections
from queue import Queue

class serialPort:
	def __init__(self,port,baudrate):
		self.ser = serial.Serial()
		self.ser.port = port
		self.ser.baudrate = baudrate
		self.ser.timeout =1
	def startSerial(self):

		self.ser.open()

	def closeSerial(self):
		self.ser.close()

	def sendStuff(self,message):
		ser = self.ser
		if ser.in_waiting > 0:
			messageEncode = message.encode()
			ser.write(messageEncode)

	def getStuff(self):
		ser = self.ser
		ser.flush()
		if(ser.in_waiting > 0):
			line = ser.readline()
			print(line.decode())
	def reset(self):
		ser.close()
		ser.open()




def serialFunc(q):
	myPort = serialPort("COM3",9600)
	while True:
		try: 
			print("Connecting to Arduino")
			myPort.startSerial()
			time.sleep(1)
			break
		except:
			print("Error Connecting to Arduino!!!")
			time.sleep(0.5)

	while True:
		if not q.empty():
			fromQ = q.get()

			if fromQ == "A":
				myPort.sendStuff()



q = Queue()

# t = threading.Thread(target=serialFunc,args = (myPort.ser,q))
t = threading.Thread(target=serialFunc,args=(q,))

t.start()





while True:
	userInput = input("enter somehting in: ")
	# myPort.getStuff()
	if userInput == "close":
		q.put("close")
		# myPort.closeSerial()

		break
	elif userInput == "sensor":
		myPort.getStuff()
	else:
		# myPort.sendStuff(userInput)
		q.put(userInput)
