from flask import Flask,render_template, request, redirect, url_for
import logging
 


ledState = False

class sensorQueue:
	def __init__(self):
		self.que = []
		self.latestValue = 0
	def add(self,newValue):
		self.que.clear()
		self.que.append(newValue)
		self.latestValue = newValue
	def get(self):
		if not self.que:
			return self.latestValue
		value = self.que.pop()
		return value

temperatureQue = sensorQueue()
humidityQue = sensorQueue()
soilMoistureQue = sensorQueue()


class buttonToggle:
	def __init__(ledColour,onMsg,offMsg):
		ledColour.onMsg = onMsg
		ledColour.offMsg = offMsg
		ledColour.state = False

	def toggleState(ledColour):
		ledColour.state = not ledColour.state
	def reset(ledColour):
		ledColour.state = False

led = buttonToggle("1","0")


app = Flask(__name__)

@app.route("/temperature", methods = ["POST","GET"])
def temperature():
	# data = temperatureQueue.pop(0)
	data = temperatureQue.get()
	return str(data);

@app.route("/humidity", methods = ["POST","GET"])
def humidity():
	data = humidityQue.get()
	return str(data);


@app.route("/soilmoisture", methods= ["POST","GET"])
def soilmoisture():
	data = soilMoistureQue.get()

	return str(data) + '';


@app.route('/helloesp')
def helloHandler():
	temperature = request.args.get("temperature")
	humidity = request.args.get("humidity")
	soilMoisturePercent = request.args.get("soilMoisturePercent")

	
	temperatureQue.add(temperature)
	humidityQue.add(humidity)
	soilMoistureQue.add(soilMoisturePercent)





	return f'Hello ESP8266, from Flask -- temperature={temperature}, humidity={humidity}, soilMoisturePercent={soilMoisturePercent} '

@app.route('/espcommands')
def commands():
	commandString = ''
	if led.state:
		commandString += led.onMsg
	else:
		commandString += led.offMsg
	# app.logger.info(commandString)
	return commandString

@app.route("/",methods = ["POST","GET"])
def home():

	if request.method == "POST":
		user = request.form["led-button"]

		if user == "ledToggle":
			led.toggleState()

		return render_template("interface.html")
	else:
		return render_template("interface.html")
app.run(host='0.0.0.0', port= 8090,debug=True)