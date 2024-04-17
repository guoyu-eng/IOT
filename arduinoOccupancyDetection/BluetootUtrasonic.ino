/***************************************************************************
* Sketch Name: arduino_bluetooth
* Description: Arduino(S) - Raspberry(M) - BLE 
* Parameters: PIR output
* Return: AT commands
* Copyright: Following code is written for educational purposes by Cardiff University.
* Modified: 03/03/2020 (by Hakan KAYAN)
***************************************************************************/

#include <SoftwareSerial.h>   //Software Serial Port
#include "Ultrasonic.h"

// Connect your Bluetooth Module to D8

#define RxD         8
#define TxD         9
 
#define PIR_ULTRASONIC_RANGER 3
 
SoftwareSerial blueToothSerial(RxD,TxD);

Ultrasonic ultrasonic(3);
 
void setup()
{
    Serial.begin(4800);
    while(!Serial){
    ;
    }
    Serial.print("Started\n");
    pinMode(PIR_ULTRASONIC_RANGER, INPUT);
    pinMode(RxD, INPUT);
    pinMode(TxD, OUTPUT);
    
    setupBlueToothConnection();
    Serial.flush();
    blueToothSerial.flush();
}
 
void loop()
{
    char buf [32];    
    char recvChar;
    static unsigned char state = 0;
    if(blueToothSerial.available()>0){
    char a = blueToothSerial.read();
    Serial.print(a);
    }
    long RangeInInches;
    long RangeInCentimeters;

 Serial.println("The distance to obstacles in front is: ");
 RangeInInches = ultrasonic.MeasureInInches();
 blueToothSerial.println(RangeInInches);
 delay(25000);
}
 
/***************************************************************************
* Function Name: setupBlueToothConnection
* Description:  initilizing bluetooth connction
***************************************************************************/
void setupBlueToothConnection()
{ 
  blueToothSerial.begin(9600);
  
  blueToothSerial.print("AT");
  delay(2000); 
  
  blueToothSerial.print("AT+BAUD4");
  delay(2000);
 
  blueToothSerial.print("AT+ROLES");
  delay(2000); 
  
  blueToothSerial.print("AT+NAMEObjRecg");   // set the bluetooth name as "Slave" ,the length of bluetooth name must less than 12 characters.
  delay(2000);
  
  blueToothSerial.print("AT+AUTH1"); 
  delay(2000);
 
  blueToothSerial.flush();
  Serial.print("Finished\n");
}
