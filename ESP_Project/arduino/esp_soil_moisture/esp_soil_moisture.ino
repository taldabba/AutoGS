#include <Wire.h>
#include <SPI.h>




const int AirValue = 654;   //you need to replace this value with Value_1
const int WaterValue = 305;  //you need to replace this value with Value_2
const int SensorPin = A0;
int soilMoistureValue = 0;
int soilMoisturePercent=0;



void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:
  soilMoistureValue = analogRead(SensorPin);  //put Sensor insert into soil
  soilMoisturePercent = map(soilMoistureValue, AirValue, WaterValue, 0, 100);

  Serial.println(soilMoisturePercent);
  
  delay(0);
  

}
