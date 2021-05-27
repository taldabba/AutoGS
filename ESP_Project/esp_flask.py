from flask import Flask,render_template, request, redirect, url_for
 
queue = []


class espcommand:
	def __init__(self):
		pass

	# def turnOnLed






app = Flask(__name__)

@app.route('/helloesp')
def helloHandler():
	temperature = request.args.get("temperature")
	humidity = request.args.get("humidity")
	soilMoisturePercent = request.args.get("soilMoisturePercent")
	return f'Hello ESP8266, from Flask -- temperature={temperature}, humidity={humidity}, soilMoisturePercent={soilMoisturePercent} '

@app.route('/espcommands')
def commands():
	return '1'

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
app.run(host='0.0.0.0', port= 8090,debug=True)