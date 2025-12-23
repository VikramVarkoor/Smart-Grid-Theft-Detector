void setup() {
  Serial.begin(115200);
}

void loop() {
  int sensorValue = analogRead(A0);
  
  // Simulate Voltage (Constant 230V) and Current (Mapped from Pot)
  float voltage = 230.0; 
  float current = (sensorValue / 1023.0) * 15.0; // Simulate 0-15 Amps
  float power = voltage * current; // Watts
  
  // Theft Detection Logic: If current exceeds 12A suddenly
  int theftAlert = (current > 12.0) ? 1 : 0;

  // Send data to Python: Power, Current, TheftStatus
  Serial.print(power);
  Serial.print(",");
  Serial.print(current);
  Serial.print(",");
  Serial.println(theftAlert);

  delay(100); // 10Hz Sampling
}