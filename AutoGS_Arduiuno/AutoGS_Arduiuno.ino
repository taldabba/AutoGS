
#include <LiquidCrystal_I2C.h> 
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT22
#include <math.h>
DHT dht(DHTPIN, DHTTYPE);



String sensorStringLn1;
String sensorStringLn2;

int pumpPin  = 12;
int ledPin = 11;
String fromSerial;

const int wet = 480;
const int dry = 221;

LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);


char checkSerial()
{
  int fromPi;

  if(Serial.available()>0)
  {
    fromPi = Serial.read();
    //Serial.print("I recieved");
    //Serial.print(fromPi, DEC);
    return fromPi;
  }
}






void setup() {
  // put your setup code here, to run once
  pinMode(pumpPin, OUTPUT);
  pinMode(ledPin,OUTPUT);
  
  Serial.begin(9600);
  dht.begin();
  
  lcd.begin(16,2);
  lcd.setCursor(0,0);

}

void loop() {
  
  fromSerial = checkSerial();
  

  int sensorVal = analogRead(A0);
  int percentageHumidity = map(sensorVal, wet,dry,100,0);

  int h = dht.readHumidity();
  int t = dht.readTemperature();

  
  
  sensorStringLn1 = "TMP:" + String(t) + "%  HUM:" + String(h) +"%";
  sensorStringLn2 = "SL:" + String(percentageHumidity) + "%   WET";

 Serial.println(String(t)+String(h)+String(percentageHumidity))
  
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print(sensorStringLn1);
  lcd.setCursor(0,2);
  lcd.print(sensorStringLn2);
  
  


  if(fromSerial == "A"){
    Serial.println("ON");
    digitalWrite(pumpPin,HIGH);
  }
  else if (fromSerial == "a"){
    Serial.println("OFF");
    digitalWrite(pumpPin,LOW);
  }

  else if(fromSerial == "B"){
    digitalWrite(ledPin,HIGH);
  }
  else if(fromSerial == "b"){
    digitalWrite(ledPin,LOW);
  }
  
    delay(100);
}
