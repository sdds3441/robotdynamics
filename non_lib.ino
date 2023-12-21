#include <Servo.h>

const int servoPin = 9;                          //서보의 핀번호

float Kp = 5;                //P게인 값
float Ki = 0;                  //I게인 값 
float Kd = 3;                  //D게인 값
double Setpoint, Input, Output, ServoOutput, error, OutputSum,dInput;                                       
float lastInput=0;
float duration, distance;

Servo myServo;                                     //서보 객체 생성, 초기화


int echoPin = 5;                 //초음파 핀번호 설정
int trigPin = 4;

void setup() {
  Serial.begin(9600);                  //시리얼 통신 초기화
  myServo.attach(servoPin);            //서보모터 핀번호 설정

  Input = readPosition();             //막대 위의 공의 위치를 측정값 함수 호출
  
  //초음파 센서 설정
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);                                                                  

}

void loop() {
  Setpoint = 18;                         //막대 중앙 위치(Set Point를 15cm로 설정)
  Input = readPosition();                //공의 위치 측정                            
  dInput=Input-lastInput;
  error=Setpoint-Input;
  OutputSum+=Ki*error;
  if (30<OutputSum)
  {
    OutputSum=30;
  }
  if (OutputSum<-30)
  {
    OutputSum=-30;
  }
  Output=Kp*error;
  Output+=OutputSum-Kd*dInput;
  if (30<Output)
  {
    Output=30;
  }
  if (Output<-30)
  {
    Output=-30;
  }
  lastInput=Input;
  
  
   Serial.println(Input);  

  ServoOutput=80+Output;                //서보모터의 각도 설정(100도는 서보모터가 수평을 이루었을 때 각도) 
  myServo.write(ServoOutput);            //서보모터에게 값 전달
}


float readPosition() {
  delay(40);                             //딜레이 설정 

  //초음파 센서 거리 측정 부분
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(2);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH); 
  distance = ((float)(340 * duration) / 10000) / 2;  


  if(distance > 30) {                   //공의 측정거리가 30cm 이상일 경우 최대 30으로 설정
    distance=30;
  }

           //시리얼 모니터로 공의 거리 출력

  return distance;                      //측정값 반환
}
