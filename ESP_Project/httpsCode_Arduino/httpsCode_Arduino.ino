#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
 
void setup () {
 
  Serial.begin(115200);
  WiFi.begin("unit2803", "platinum2803n2");
 
  while (WiFi.status() != WL_CONNECTED) {
 
    delay(1000);
    Serial.println("Connecting..");
 
  }
  Serial.println("Connected to WiFi Network");
 
}
 
void loop() {
 
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
 
  delay(10000);    //Send a request every 10 seconds
} 
