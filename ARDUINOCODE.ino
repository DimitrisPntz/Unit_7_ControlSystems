const int CLASS_PINS[] = {13, 12, 11, 10, 9, 8, 7, 6, 5, 4};

// Have this command to not send a billion messages to the python program
bool CommandSent = false;
int LastPin = 3;

void TurnOnLights() {
  for (int i = 0; i < 11; i++) {
    digitalWrite(CLASS_PINS[i], HIGH);
  }
}

void TurnOffLights() {
  for (int i = 0; i < 11; i++) {
    digitalWrite(CLASS_PINS[i], LOW);
  }
}

void TurnOnLight(const int ClassIndex){
  digitalWrite(ClassIndex, HIGH);
  LastPin = ClassIndex;
}

void setup() {
  // Set Up Serial Connection
  Serial.begin(9600);

  // Set up each class pin as an output
  for (int i = 0; i < 11; i++) {
    pinMode(CLASS_PINS[i], OUTPUT);
  }
}

void loop() {
  if(Serial.available() > 0){
    String msg = Serial.readString();

    if(msg == "ON"){
      TurnOnLights();
    }else if(msg == "OFF"){
      TurnOffLights();
    }

    if(msg.startsWith("OPEN LIGHT ")){
      //Turn off Last Light
      digitalWrite(LastPin, LOW);

      // Code to extract the Pin Number to turn on
      int LastSpace = msg.lastIndexOf(" ");
      String PinValue = msg.substring(LastSpace + 1);
      int PinNumber = PinValue.toInt();

      TurnOnLight(PinNumber);
      Serial.println("Opened Pin " + String(PinNumber));
    }

    if(msg == "EXIT"){
      Serial.println("EXIT");
      TurnOffLights();
    }
  }  
}
