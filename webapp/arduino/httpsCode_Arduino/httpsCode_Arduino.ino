#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include <SPI.h>
#include <string.h>
#include <Adafruit_NeoPixel.h>

#include "DHTesp.h"
#ifdef ESP32l,.
#pragma message(THIS EXAMPLE IS FOR ESP8266 ONLY!)
#error Select ESP8266 board.
#endif
#define numberOfLED 60
#define ledPin 4

//int numberOfLED = 60;
//int ledPin = 6;

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(numberOfLED, ledPin, NEO_GRB + NEO_KHZ800);

int relayPin = 5;
DHTesp dht;
//LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);

void setup () {


 
  Serial.begin(115200);
  pixels.begin(); 
  pixels.show();
  pixels.setBrightness(50);
  
  dht.setup(16, DHTesp::DHT22); //dht setup
//  lcd.begin(16,2);//lcd setup
  pinMode(BUILTIN_LED, OUTPUT);//led setup
  pinMode(relayPin,OUTPUT);
  //wifi setup
  WiFi.begin("BELL043", "4DCC2A9CAC27"); 
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

void displayRGB(int r,int g,int b){
    for (int i = 0; i < numberOfLED; i++) {
      pixels.setPixelColor(i, pixels.Color(r,g,b));
      pixels.show();}
      
}



void sendToWebserver(int temperature, int humidity, int soilMoisturePercent) {
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
 
    HTTPClient http;  //Declare an object of class HTTPClient
    WiFiClient wifi;
    http.begin(wifi,"http://192.168.2.67:5000/helloesp?temperature=" + String(temperature) + "&humidity=" + String(humidity) + "&soilMoisturePercent=" + String(soilMoisturePercent)); //Specify request destination

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
    http.begin(wifi,"http://192.168.2.67:5000/espcommands"); //Specify request destination

    int httpCode = http.GET(); //Send the request
 
    if (httpCode > 0) { //Check the returning code
 
      payload = http.getString();   //Get the request response payload      
 
    }else Serial.println("An error ocurred");
 
    http.end();   //Close connection 
  }

  return payload;
  
}

void parsePayload(String payload){
  Serial.println(payload);
//  Serial.println("Red = " + payload.substring(2,5));
//  Serial.println("Blue = " + payload.substring(5,8));
//  Serial.println("Green = " + payload.substring(8,11));

  String redValueStr = payload.substring(2,5);
  String greenValueStr = payload.substring(5,8);
  String blueValueStr = payload.substring(8,11);
  
  int redValue = redValueStr.toInt();
  int greenValue = greenValueStr.toInt();
  int blueValue = blueValueStr.toInt();

  


  
  if (payload.substring(0,1) == "1"){
    
    digitalWrite(BUILTIN_LED,HIGH);
    displayRGB(redValue,greenValue,blueValue);    
  }
  else{
    digitalWrite(BUILTIN_LED,LOW);
    displayRGB(0,0,0); 
  }
  
  if (payload.substring(1,2) == "a"){
//    Serial.println("relay on");
    digitalWrite(relayPin,LOW);
  }
    
  
  else{
    digitalWrite(relayPin,HIGH);
//    Serial.println("relay off");
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
