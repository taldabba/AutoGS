import serial

class serialPort:
	def __init__(self,port,baudrate):
		self.ser = serial.Serial()
		self.ser.port = port
		self.ser.baudrate = baudrate


myPort = serialPort("com")