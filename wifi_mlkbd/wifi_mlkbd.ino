/*
/opt/arduino-1.5.8/arduino --board arduino:sam:arduino_due --port /dev/ttyACM3 --upload  micropro3_wifi_mlkbd.ino
Real micropro3 on IDE - use /opt/arduino-1.6.5-r5/arduino  



Todo
o

*/

#include "DHT.h"
#include "Adafruit_Sensor.h"


#define LED_PIN 13
#define RESET 12

#define DHTPIN 2 // We have connected the DHT to Digital Pin 2
#define DHTTYPE DHT22 // This is the type of DHT Sensor (Change it to DHT11 if you're using that model)

String retMsg = "";	
int firstTime = 1;

int device;
int code;
int value;
char msg[64];

void setup()
{

    Serial.begin(115200);
    Serial1.begin(9600);
    Serial.println("Starting");

	// CH_PD	Chip Power Down
    pinMode(LED_PIN, OUTPUT);
    digitalWrite(LED_PIN, HIGH);

	// Reset	
    pinMode(RESET, OUTPUT);
    digitalWrite(RESET, HIGH);

  	Keyboard.begin();

	//Serial.print("\nAT\r\n");
	//Serial1.print("AT\r\n");
	espSend("AT\r\n");
 
	espSend("\nAT+RST\r\n");
 
	espSend("\nAT+CIPMUX=1\r\n");

	espSend("\nAT+CIPSERVER=1,8888\r\n");


}

void loop()
{

  	char* chDevice;
  	char* chCode;
  	char* chValue;

	if(checkOutput())
	{
		Serial.print("retMsg is ");
		Serial.println(retMsg);
		if (retMsg.indexOf("+IPD,") == -1)
		{
			Serial.println("Not a data message");
		}
		else
		{
			retMsg = retMsg.substring(retMsg.indexOf(':') + 1);
			Serial.println(retMsg);
      		sscanf(retMsg.c_str(), "%d %d %d", &device, &code, &value);
		
			Serial.println(device);
			Serial.println(code);
			Serial.println(value);
		
      		if (device == 0)
      		{
        		if (value >0)
        		{
		  		
      				Serial.print("Key Press and Release ");
      				Serial.println(code);
          			Keyboard.press(code);
          			Keyboard.release(code);
        		}
  		
        		else
        		{
      				Serial.print("Key Release - do nothing ");
      				Serial.println(code);
          			Keyboard.press(code);
          			Keyboard.release(code);
        		}
      		}


		}

	}
	delay(100);
}


void espSend(char *ATCmd)
{

	Serial.print(ATCmd);
	Serial1.print(ATCmd);
	delay(1000);
	checkOutput();


}

int checkOutput()
{
	retMsg = "";
	int retVal = 0;

	int count = 0;

	while (count++ < 5)
	{
		while (Serial1.available())
		{
			byte b = Serial1.read();
			//Serial.write(b);
			retMsg.concat(char(b));
			retVal = 1;
		}
		delay(5);
	}
	//Serial.print("checkOutput returns: ");
	//Serial.println(retMsg);
	Serial.print(retMsg);
	return retVal;
}

