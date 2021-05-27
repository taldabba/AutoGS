#include "DHTesp.h"
#ifdef ESP32
#pragma message(THIS EXAMPLE IS FOR ESP8266 ONLY!)
#error Select ESP8266 board.
#endif

#include <Wire.h>
#include <SPI.h>
#include <LiquidCrystal_I2C.h>


const int AirValue = 654;   //you need to replace this value with Value_1
const int WaterValue = 305;  //you need to replace this value with Value_2
const int SensorPin = A0;
int soilMoistureValue = 0;
int soilMoisturePercent=0;

DHTesp dht;
LiquidCrystal_I2C lcd(0x27, 16, 2);
void setup()
{
  Serial.begin(115200);
  Serial.println();
  Serial.println("Status\tHumidity (%)\tTemperature (C)");
  // Autodetect is not working reliable, don't use the following line
  // dht.setup(17);
  // use this instead: 
  dht.setup(16, DHTesp::DHT22); // Connect DHT sensor to GPIO 5
  lcd.begin();
  lcd.setCursor(0,0);
  lcd.print("Hello");
}
void loop()
{
  delay(2000);
  float humidity = dht.getHumidity();
  float temperature = dht.getTemperature();

  soilMoistureValue = analogRead(SensorPin);  //put Sensor insert into soil
  soilMoisturePercent = map(soilMoistureValue, AirValue, WaterValue, 0, 100);


  Serial.print(dht.getStatusString());
  Serial.print("\t");
  Serial.print(humidity, 1);
  Serial.print("\t");
  Serial.print(temperature, 1);
  Serial.print("\t");
  Serial.println(soilMoisturePercent);
}
