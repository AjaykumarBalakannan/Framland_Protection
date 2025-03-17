#define CAYENNE_PRINT Serial
#include <CayenneMQTTESP8266.h>
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2); 
#define k1 D7
#define relay D0
#define relay1 D5 
unsigned int m=0,act=0,val,val1,val2,val3,val4;
String inputString = ""; 
unsigned char a[200];
#include <Servo.h>
int pos;
Servo myservo; // create servo object to control a servo

char ssid[] = "IOT";
char wifiPassword[] = "123456789";

// Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
char username[] = "fdf71b20-396a-11ed-baf6-35fab7fd0ac8";
char password[] = "233ae3064bcccff9196799e7acfa064456a23af2";
char clientID[] = "58ce1c60-396b-11ed-bf0a-bb4ba43bd3f6";
void voice1()
{
  digitalWrite(k1,HIGH);
  delay(3000);
  digitalWrite(k1,LOW);
}

void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600);
  Wire.begin();
  lcd.init(); //Init the LCD
  lcd.backlight(); //Activate backlight     
  lcd.home();  
  lcd.setCursor(0,0);
  lcd.print("ANIMAL DETECTION");
  delay(3000);
  lcd.clear();
  pinMode(k1,OUTPUT);
  pinMode(relay,OUTPUT);
  pinMode(relay1,OUTPUT);
  digitalWrite(k1,HIGH);
  digitalWrite(relay,HIGH);
  digitalWrite(relay1,HIGH);
  myservo.attach(D6); 
   Cayenne.begin(username, password, clientID, ssid, wifiPassword);
}
CAYENNE_IN(V0)
{
  if(getValue.asInt()==1)  
  {
    Serial.println("hi");
    pos=pos+10;
    myservo.write(pos); // tell servo to go to position in variable 'pos' 
    delay(15);
  }
}
CAYENNE_IN(V1)
{
  if(getValue.asInt()==1)  
  {
       pos=pos-10;
       myservo.write(pos); // tell servo to go to position in variable 'pos' 
      delay(15);
  }
}
CAYENNE_IN(V2)
{
  if(getValue.asInt()==1)
  {
    digitalWrite(relay1,LOW);
  }
  else
  {
       digitalWrite(relay1,HIGH);
  }
}
void loop() {
while(Serial.available())
    {
        char data;
        data=Serial.read();
  
        a[m]=data;
          if(a[0] == '*')
          {
            if(m<=1)
            {m++;}
          }
      }
      if(m > 1)
      {
        val = (a[1]-0x30);
    
        m=0;
      }
      delay(500); 


      Serial.print("val:");
      Serial.println(val);
if(val==1)
{
  voice1();
  digitalWrite(relay,LOW);
  digitalWrite(relay1,LOW);
  delay(4000);
  digitalWrite(relay,HIGH);
  digitalWrite(relay1,HIGH);
  lcd.setCursor(0,0);
  lcd.print("ELEPHANT DETECT");
  delay(3000);
  lcd.clear();
  val=0;
  digitalWrite(k1,HIGH);
}
  
  Cayenne.loop();
  for(pos = 0; pos <= 180; pos += 1) // goes from 0 degrees to 180 degrees 
  { // in steps of 1 degree 
    myservo.write(pos); // tell servo to go to position in variable 'pos' 
    delay(15); // waits 15ms for the servo to reach the position 
  } 
  for(pos = 180; pos>=0; pos-=1) // goes from 180 degrees to 0 degrees 
  {                                
    myservo.write(pos); // tell servo to go to position in variable 'pos' 
    delay(15); // waits 15ms for the servo to reach the position 
  }     
}
