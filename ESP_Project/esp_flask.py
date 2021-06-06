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

redQue = sensorQueue()
blueQue = sensorQueue()
greenQue = sensorQueue()


# class threadTimer:
# 	def __init__(self):
		















class buttonToggle:
	def __init__(ledColour,onMsg,offMsg):
		ledColour.onMsg = onMsg
		ledColour.offMsg = offMsg
		ledColour.state = False

	def toggleState(ledColour):
		ledColour.state = not ledColour.state
	def reset(ledColour):
		ledColour.state = False
	def curMessage(self):
		if self.state == True:
			return self.onMsg
		else: 
			return self.offMsg

led = buttonToggle("1","0")
relay = buttonToggle("a","b")


def getPost(app, name):
    try:
        user = request.form[name]
        return True
    except:
        return False








app = Flask(__name__)

@app.route("/changeRGB")
def rgbChange():
	red = request.args.get("red")
	green = request.args.get("green")
	blue = request.args.get("blue")

	app.logger.info(red)
	app.logger.info(green)
	app.logger.info(blue)


	redQue.add(red)
	greenQue.add(green)
	blueQue.add(blue)

	return ''

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
	


	r = int(redQue.get())
	g = int(greenQue.get())
	b = int(blueQue.get())

	r = f'{r:03}'
	g = f'{g:03}'
	b = f'{b:03}'



	commandString = ''	
	commandString+= led.curMessage()
	commandString+= relay.curMessage()

	commandString+= str(r)
	commandString+= str(g)
	commandString+= str(b)

	# if led.tate:
	# 	commandString += led.onMsg
	# else:
	# 	commandString += led.offMsgs
	# app.logger.info(commandString)
	return commandString

@app.route("/",methods = ["POST","GET"])
def home():

	if request.method == "POST":
		getPost(app, "led-button")
		if (getPost(app, "led-button")):
			app.logger.info("bruhLEDChungus")
			led.toggleState()
		elif (getPost(app, "sendRGB")):
			app.logger.info("rgbChungus")
		elif (getPost(app, "waterSend")):
			app.logger.info("waterChungus")


    # relay.toggleState()
		return render_template("interface.html")
	else:
		return render_template("interface.html")
app.run(host='0.0.0.0', port= 8090,debug=True)