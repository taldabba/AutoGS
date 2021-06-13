//int fromPi = 0;
String serialFrom;
int redPin = 10;
int greenPin = 12;
int bluePin = 11;

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


bool lightToggle = false;
void toggleBlinkLight(bool toggle,int pinNum)
{
   
   if (toggle == true)
   {
     digitalWrite(pinNum, HIGH);
   }
   else
   {
    /*digitalWrite(redPin, LOW);
    digitalWrite(greenPin, LOW);
    digitalWrite(bluePin, LOW);
    */
    digitalWrite(pinNum,LOW);
   } 
}

bool red_led = false;
bool green_led = false;
bool blue_led = false;


void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600);
 pinMode(redPin,OUTPUT);
 pinMode(greenPin,OUTPUT);
 pinMode(bluePin,OUTPUT);
}



void loop() 
{
  // put your main code here, to run repeatedly:

  serialFrom = checkSerial();
  
  
  //Serial.println("Hello");
  if (serialFrom == "a")
  { 
    

    
    /*if(red_led == false){
     digitalWrite(redPin,LOW);
     red_led = true;     
    }
    else{
      digitalWrite(redPin,HIGH);
      red_led = false;
    }
    */
  }

  

 
}
