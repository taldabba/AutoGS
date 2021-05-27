#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

#include "DHTesp.h"
#ifdef ESP32
#pragma message(THIS EXAMPLE IS FOR ESP8266 ONLY!)
#error Select ESP8266 board.
#endif

#include <Wire.h>
#include <SPI.h>

DHTesp dht;

String getSensors(){

  //capcitive soil moisture variables
  const int AirValue = 654;   
  const int WaterValue = 305; 
  const int SensorPin = A0;
  int soilMoistureValue = 0;
  int soilMoisturePercent=0;
  
  float humidity = dht.getHumidity();
  float temperature = dht.getTemperature();

  soilMoistureValue = analogRead(SensorPin);  //put Sensor insert into soil
  soilMoisturePercent = map(soilMoistureValue, AirValue, WaterValue, 0, 100);

  String output = (String(humidity) + "\t"+ String(temperature) + "\t" +String(soilMoisturePercent));
  return output;  
}








 
void setup () {
 
  Serial.begin(115200);
 
  dht.setup(5, DHTesp::DHT22); //dht setup

  //wifi setup
  WiFi.begin("unit2803", "platinum2803n2"); 
  while (WiFi.status() != WL_CONNECTED) { 
    delay(1000);
    Serial.println("Connecting.."); 
  }

  
  Serial.println("Connected to WiFi Network"); 
}
 
void loop() {
  Serial.println(getSensors());
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
 
    HTTPClient http;  //Declare an object of class HTTPClient
    WiFiClient wifi;
    http.begin(wifi,"http://192.168.0.123:8090/helloesp"); //Specify request destination
 
    int httpCode = http.GET(); //Send the request
 
    if (httpCode > 0) { //Check the returning code
 
      String payload = http.getString();   //Get the request response payload
      Serial.println(payload);             //Print the response payload
 
    }else Serial.println("An error ocurred");
 
    http.end();   //Close connection
 
  }
 
  delay(2000);    //Send a request every 10 seconds
} 
