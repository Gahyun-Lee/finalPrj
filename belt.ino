#define MOTOR_A1 9
#define MOTOR_A2 10

int move = 1;
int stop = 0;
// int same = 0;

void setup()
{
    Serial.begin(9600);
    pinMode(A0,INPUT);
    pinMode(MOTOR_A1,OUTPUT);
    pinMode(MOTOR_A2,OUTPUT);
}

void loop()
{
    unsigned int vr = map(analogRead(A0), 0, 1023, 0, 511);

    if(Serial.available()) {
      char data = Serial.read();
      if(data == 's')
        move = 0;
      // else if(data == 'ts')
      //   same = 1;
      // else if(data == 'tm')
      // {
      //   move = 1;
      //   same = 0;
      // }
    }

    if(move == 1)
    {  
      if(vr < 256)
      {
          analogWrite(MOTOR_A1, 255-vr);
          analogWrite(MOTOR_A2, 0);
          // Serial.print("front -");
          // Serial.println(255-vr);
      }
      else
      {
          analogWrite(MOTOR_A1, 0);
          analogWrite(MOTOR_A2, vr-256);
          // Serial.print("back -");
          // Serial.println(vr-256);

      }
      delay(1);
      if(stop == 1) {
        delay(7000);
        Serial.begin(9600);
        stop = 0;
      }
    }
    else if(move == 0) { //stop
      if(vr < 256)
      {
          analogWrite(MOTOR_A1, 0);
          analogWrite(MOTOR_A2, 0);
          // Serial.print("front -");
          // Serial.println(255-vr);
      }
      else
      {
          analogWrite(MOTOR_A1, 0);
          analogWrite(MOTOR_A2, 0);
          // Serial.print("back -");
          // Serial.println(vr-256);

      }
      if (move == 0)
      {
        delay(4000);
        move = 1;
        stop = 1;
        Serial.end();
      }
    }
}
