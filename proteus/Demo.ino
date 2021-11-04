#include <Wire.h> 

int led = 9;

void setup()
{
	Serial.begin(9600);
 pinMode(led,OUTPUT);
}
String incomingByte ;
void loop()
{
    if (Serial.available() > 0) {

    incomingByte = Serial.readStringUntil('\n');

    if (incomingByte == "on") {

        digitalWrite(led,HIGH);
        Serial.write("Led on");

    }

    else if (incomingByte == "off") {

      digitalWrite(led,LOW);
      Serial.write("Led off");
    }

    else {

       Serial.write("invald input");

    }
  }

}
