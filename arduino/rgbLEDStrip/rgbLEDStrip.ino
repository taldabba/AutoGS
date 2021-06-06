#include <ArduinoJson.h>
#include <Adafruit_NeoPixel.h>

String message = "";
bool messageReady = false;
int ledPin = 6;
int numberOfLED = 60;
 
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(numberOfLED, ledPin, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(115200);
  pixels.begin();
}

void loop() {

  
  String chungus = handleIndex();
  Serial.println(chungus);


}

void handleIndex() {
  DynamicJsonDocument doc(1024);
  double rgbLEDParse = 0;
  doc["type"] = "request";
  serializeJson(doc, Serial);
  boolean messageReady = false;
  String message = "";
  while (messageReady == false) {
    if (Serial.available()) {
      message = Serial.readString();
      messageReady = true;
    }
  }

  DeserializationError error = deserializeJson(doc, message);
  if (error) {
    Serial.print(F("deserializeJson() failed: "));
    Serial.println(error.c_str());
    return;
  }
  rgbLEDParse = doc["rgbLEDPrase"];
}
