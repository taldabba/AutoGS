#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include <SPI.h>
#include <string.h>

#include "DHTesp.h"
#ifdef ESP32
#pragma message(THIS EXAMPLE IS FOR ESP8266 ONLY!)
#error Select ESP8266 board.
#endif

int relayPin = 5;
DHTesp dht;
//LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);

void setup () {


 
  Serial.begin(115200);
   
  dht.setup(16, DHTesp::DHT22); //dht setup
//  lcd.begin(16,2);//lcd setup
  pinMode(BUILTIN_LED, OUTPUT);//led setup
  pinMode(relayPin,OUTPUT);
  //wifi setup
  WiFi.begin("NETGEAR42", "bluesky812"); 
  while (WiFi.status() != WL_CONNECTED) { 
    delay(1000);
    Serial.println("Connecting.."); 
  }

  Serial.println("Connected to WiFi Network"); 
}

//void displayLCD(int temperature, int humidity, int soilMoisturePercent) {
//  String sensorStringLn1 = "TMP:" + String(temperature) + "C  HUM:" + String(humidity) +"%";
//  String sensorStringLn2 = "SL:" + String(soilMoisturePercent) + "%";
//  lcd.clear();
//  lcd.setCursor(0,0);
//  lcd.print(sensorStringLn1);
//  lcd.setCursor(0,2);
//  lcd.print(sensorStringLn2);  
//}

void sendToWebserver(int temperature, int humidity, int soilMoisturePercent) {
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
 
    HTTPClient http;  //Declare an object of class HTTPClient
    WiFiClient wifi;
    http.begin(wifi,"http://10.0.0.246:8090//helloesp?temperature=" + String(temperature) + "&humidity=" + String(humidity) + "&soilMoisturePercent=" + String(soilMoisturePercent)); //Specify request destination

    int httpCode = http.GET(); //Send the request
 
    if (httpCode > 0) { //Check the returning code
 
      String payload = http.getString();   //Get the request response payload
//      Serial.println(payload);             //Print the response payload
 
    }else Serial.println("An error ocurred");
 
    http.end();   //Close connection
 
  }
}

String getFlaskCommands(){
  String payload;
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
 
    HTTPClient http;  //Declare an object of class HTTPClient
    WiFiClient wifi;
    http.begin(wifi,"http://10.0.0.246:8090//espcommands"); //Specify request destination

    int httpCode = http.GET(); //Send the request
 
    if (httpCode > 0) { //Check the returning code
 
      payload = http.getString();   //Get the request response payload      
 
    }else Serial.println("An error ocurred");
 
    http.end();   //Close connection 
  }

  return payload;
  
}

void parsePayload(String payload){
  Serial.println(payload.substring(1,2));
  if (payload.substring(0,1) == "1"){
    
    digitalWrite(BUILTIN_LED,HIGH);    
  }
  else if (payload.substring(0,1) == "0")  {
    digitalWrite(BUILTIN_LED,LOW);
  }
  
  if (payload.substring(1,2) == "a"){
    Serial.println("relay on");
    digitalWrite(relayPin,LOW);
  }
    
  
  else{
    digitalWrite(relayPin,HIGH);
    Serial.println("relay off");
  }

}




void loop() {
  const int AirValue = 654;   
  const int WaterValue = 305; 
  const int SensorPin = A0;
  int soilMoistureValue = 0;
  int soilMoisturePercent=0;
  
  int humidity = dht.getHumidity();
  int temperature = dht.getTemperature();
  soilMoistureValue = analogRead(SensorPin);  //put Sensor insert into soil
  soilMoisturePercent = map(soilMoistureValue, AirValue, WaterValue, 0, 100);

//  digitalWrite(relayPin,LOW);
//  displayLCD(temperature,humidity, soilMoisturePercent );
  sendToWebserver(temperature,humidity, soilMoisturePercent);
  parsePayload(getFlaskCommands());

  
  delay(2000);    //Send a request every 10 seconds
} 
