#include <Servo.h>

int incomingByte = 0; 
const int LaserPin = 8;

Servo sx; // Servo to control X axis
Servo sy; // Servo to control Y axis

byte coords[2];
int xdeg = 90; // Servo position on X axis
int ydeg = 90; // Servo position on Y axis

void setup() {
  // put your setup code here, to run once:

  // Start communication on the Serial Console.
  Serial.begin(9600); // 9600 baud rate
  // Initialize the Servo Motors
  sx.attach(9);
  sy.attach(10);

  sx.write(xdeg);
  sy.write(ydeg);

  // Control the LaserPin
  pinMode(LaserPin, OUTPUT);
  // Turn it off by default.
  digitalWrite(LaserPin, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    
    // This means we're sending coordinate data
    if (incomingByte == 'C') {
      // Read co-ordinates
      Serial.readBytes(coords, 2);
      // Update motors accordingly.
      sx.write((int)coords[0]);
      sy.write((int)coords[1]);

    } else if (incomingByte == 'H') {
      // Turn on our Laser
      digitalWrite(LaserPin, HIGH);
    } else if (incomingByte == 'L') {
      // Turn off our Laser
      digitalWrite(LaserPin, LOW);
    } else {
      // ignore everything else
    }
    
    Serial.println(incomingByte);
    Serial.flush();
  }
}
