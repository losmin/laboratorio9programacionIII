const int relePin = 2; // Pin del relé
const int ledVerdePin = 3; // Pin del LED verde
const int ledRojoPin = 4; // Pin del LED rojo

void setup() {
  pinMode(relePin, OUTPUT);
  pinMode(ledVerdePin, OUTPUT);
  pinMode(ledRojoPin, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') {
      digitalWrite(relePin, HIGH); // Activa el relé
      digitalWrite(ledVerdePin, HIGH); // Enciende el LED verde
      digitalWrite(ledRojoPin, LOW); // Apaga el LED rojo
    } else if (command == '0') {
      digitalWrite(relePin, LOW); // Desactiva el relé
      digitalWrite(ledVerdePin, LOW); // Apaga el LED verde
      digitalWrite(ledRojoPin, HIGH); // Enciende el LED rojo
    }
  }
}
