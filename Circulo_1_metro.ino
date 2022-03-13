//Motor A
int ENA = 10; //Izquierda 
int IN1 = 9;
int IN2 = 8;

//Motor B
int ENB = 5; //Derecha
int IN3 = 7;
int IN4 = 6;

void setup() {

  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
}

void loop() {

  //Recta
  analogWrite(ENA, 40);
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2, LOW);

  analogWrite(ENB, 78);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);

}
