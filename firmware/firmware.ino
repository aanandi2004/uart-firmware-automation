// int trigPin = 13;    // Sensor trig pin is connected to Arduino 13
// int echoPin = 11;    // Sensor echo pin connected to Arduino 11
// float pingTime;      // Time for ping to hit target and return 
// float distanceCm;
// int ledPin = 5;      // FIX: Changed from 7 to 5. Ensure your wire matches!
// int buttonPin = 6;   // Pushbutton connected to pin 6

// void setup() {
//   Serial.begin(9600);
  
//   // Ultrasonic Sensor Pins
//   pinMode(trigPin, OUTPUT);
//   pinMode(echoPin, INPUT);
  
//   // Peripherals Configuration
//   pinMode(ledPin, OUTPUT);
//   pinMode(buttonPin, INPUT_PULLUP); // Internal pull-up resistor (Active-LOW button)
// }

// void loop() {
//   // Check if the PC has sent any data over the serial interface
//   if (Serial.available() > 0) {
    
//     // Read until newline character for immediate Python compatibility
//     String command = Serial.readStringUntil('\n');
    
//     // Trim off any hidden whitespace, carriage returns (\r), or stray characters
//     command.trim();
    
//     // 1. COMMAND: READ
//     if (command.equalsIgnoreCase("READ")) {
//       distanceCm = readDistance(); // Use helper function
      
//       Serial.print("Distance: ");
//       Serial.print(distanceCm);
//       Serial.println(" cm");
//     }
    
//     // 2. COMMAND: LED_ON
//     else if (command.equalsIgnoreCase("LED ON")) {
//       //digitalWrite(ledPin, HIGH); // Reverted to digitalWrite for pure 5V maximum rail
//       analogWrite(ledPin , 255);
//       Serial.println("LED IS ON");
//     }
    
//     // 3. COMMAND: LED_OFF
//     else if (command.equalsIgnoreCase("LED OFF")) {
//       digitalWrite(ledPin, LOW);
//       Serial.println("LED IS OFF");
//     }
    
//     // 4. COMMAND: BUTTON_STATUS
//     else if (command.equalsIgnoreCase("BUTTON STATUS")) {
//       if (digitalRead(buttonPin) == LOW) {
//         Serial.println("PRESSED");
//       } else {
//         Serial.println("RELEASED");
//       }
//     }
    
//     // 5. COMMAND: STATUS (Aggregated System Diagnostic)
//     else if (command.equalsIgnoreCase("STATUS")) {
//       // Get the latest distance reading dynamically
//       distanceCm = readDistance();

//       // Output LED State (Works perfectly now with digitalWrite)
//       if (digitalRead(ledPin) == HIGH) {
//         Serial.print("LED: ON");
//       } else {
//         Serial.print("LED: OFF");
//       }
      
//       Serial.print(" | ");
      
//       // Output Button State
//       if (digitalRead(buttonPin) == LOW) {
//         Serial.print("BUTTON: PRESSED");
//       } else {
//         Serial.print("BUTTON: RELEASED");
//       }

//       Serial.print(" | ");

//       // Output Distance State
//       Serial.print("DISTANCE: ");
//       Serial.print(distanceCm);
//       Serial.println(" cm");
//     }
    
//     // 6. COMMAND: VERSION
//     else if (command.equalsIgnoreCase("VERSION")) {
//       Serial.println("V1.3.0 (2026-06-25)");
//     }
    
//     // Fallback for unknown inputs (e.g., "ABC")
//     else {
//       Serial.print("UNKNOWN COMMAND: ");
//       Serial.println(command);
//     }
//   }
// }

// // Helper function to isolate ultrasonic sensor triggering and calculation
// float readDistance() {
//   digitalWrite(trigPin, LOW); 
//   delayMicroseconds(2);       
//   digitalWrite(trigPin, HIGH); 
//   delayMicroseconds(10); 
//   digitalWrite(trigPin, LOW); 
  
//   float pingtime = pulseIn(echoPin, HIGH); 
//   return (pingtime * 0.0343) / 2.0;
// }

int trigPin = 13;
int echoPin = 11;

int ledPin = 5;
int buttonPin = 6;

float distanceCm;

void setup() {

  Serial.begin(9600);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
}

float readDistance() {

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);

  return (duration * 0.0343) / 2.0;
}

void loop() {

  if (digitalRead(buttonPin) == LOW) {

    digitalWrite(ledPin, HIGH);

    distanceCm = readDistance();

    Serial.print("Distance: ");
    Serial.print(distanceCm);
    Serial.println(" cm");

    delay(100);
  }

  else {

    digitalWrite(ledPin, LOW);
  }
}