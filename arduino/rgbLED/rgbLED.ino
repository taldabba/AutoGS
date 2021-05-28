int rgbLED (int powerLED, int redValue, int greenValue, int blueValue) {

  int redPin = 8;
  int greenPin = 9;
  int bluePin = 10;

  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  if (powerLED == 1) {
    analogWrite(redPin, redValue);
    analogWrite(greenPin, greenValue);
    analogWrite(bluePin, blueValue);
  }
  
  else {
    analogWrite(redPin, 0);
    analogWrite(greenPin, 0);
    analogWrite(bluePin, 0);
  }
}

void setup() {
  
}




  int r = 1;
//  int g = 1;
//  int b = 1;
void loop() {



  r+=1;
  // g+=1;
  // b+=1;

  rgbLED(1, r, g, b);
  
  delay(500);

}
