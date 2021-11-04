#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
int led = 9;
int led2 = 10;

void setup()
{
  Serial.begin(9600);
  lcd.begin();
  lcd.backlight();
  pinMode(led,OUTPUT);
  pinMode(led2,OUTPUT);
}
String incomingByte ;
void loop()
{
    if (Serial.available() > 0) {

    incomingByte = Serial.readStringUntil('\n');

    if (incomingByte == "on") {
        lcd.clear();
        digitalWrite(led,HIGH);
        digitalWrite(led2,LOW);
        Serial.write("Led on");
        lcd.setCursor(0,0);
        lcd.print("LED on");
    }
    else if (incomingByte == "off") {
      lcd.clear();
      digitalWrite(led,LOW);
      digitalWrite(led2,HIGH);
      Serial.write("Led off");
      lcd.setCursor(0,0);
      lcd.print("LED off");
    }
    else {
       Serial.write("invald input");
    }
  }
}
