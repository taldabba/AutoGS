from flask import Flask, redirect, url_for, render_template, request
import logging

app = Flask(__name__)

def getPost(app, name):
    try:
        user = request.form[name]
        return True
    except:
        return False



@app.route("/changeRGB")
def rgbChange():
	red = request.args.get("red")
	green = request.args.get("green")
	blue = request.args.get("blue")

	return 'bruh'




@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        getPost(app, "led-button")
        if (getPost(app, "led-button")):
            app.logger.info("bruhLEDChungus")
        elif (getPost(app, "sendRGB")):
            app.logger.info("rgbChungus")
        elif (getPost(app, "waterSend")):
            app.logger.info("waterChungus")

        return render_template("interface.html")
    else:
        return render_template("interface.html")




if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)