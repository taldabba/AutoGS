from flask import Flask, render_template, request, redirect


class buttonToggle:
	def __init__(ledColour,onMsg,offMsg):
		ledColour.onMsg = onMsg
		ledColour.offMsg = offMsg
		ledColour.state = False

	def toggleState(ledColour):
		ledColour.state = not ledColour.state
	def reset(ledColour):
		ledColour.state = False









@app.route("/",methods = ["POST","GET"])
def home():
	if request.method == "POST":



		return render_template("interface.html")
	else:
		return render_template("interface.html")	










app = Flask(__name__)
if __name__ =="__main__":
	app.run(port=8082,debug = True)