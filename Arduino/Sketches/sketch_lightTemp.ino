//Sketch for the Deconstruction... Light and temperature sensor sending readings, with delimiters, over serial to Raspberry PI

int photocellPin = 0;     // the cell and 10K pulldown are connected to a0
int photocellReading;     // the analog reading from the analog resistor divider


int tempPin = 1;
//int tempReading;

void setup(void) {
  // We'll send information via the Serial monitor for the Raspberry PI
  Serial.begin(9600);   
}
 
void loop() {
  photocellReading = analogRead(photocellPin);  // Reads in the light reading
  delay(50);
  int tempReading = analogRead(tempPin); // Reads in the temp reading
float voltage = tempReading * 5.0; // converts the temp reading to voltage
 voltage /= 1024.0; 

  float temperatureC = (voltage - 0.5) * 100 ; // converts the reading to temperature in celcius
  int temperatureC1 = (temperatureC *10); // multiples by 10 to convert the reading to an int for serial transfer (it reads a char at a time and was easier this way
  Serial.print(temperatureC1);
  Serial.print("?"); // used ? as delimiter
 
  if (photocellReading < 10) { // This is to differenciate between dark,dim,light, bright and very bright, using a 1 char number.
    Serial.println(0);
  } else if (photocellReading < 25) {
    Serial.println(1);
  } else if (photocellReading < 50) {
    Serial.println(2);
  } else if (photocellReading < 100) {
    Serial.println(3);
  } else {
    Serial.println(4);
  }
  delay(10000);
}
