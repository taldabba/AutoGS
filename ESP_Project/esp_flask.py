from flask import Flask,request
 
app = Flask(__name__)
 
@app.route('/helloesp')
def helloHandler():
	temperature = request.args.get("temperature")
	humidity = request.args.get("humidity")
	soilMoisturePercent = request.args.get("soilMoisturePercent")
	return f'Hello ESP8266, from Flask -- temperature={temperature}, humidity={humidity}, soilMoisturePercent={soilMoisturePercent} '
 
app.run(host='0.0.0.0', port= 8090,debug=True)