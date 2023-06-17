import RPi.GPIO as GPIO     # 라즈베리파이 GPIO 관련 모듈을 불러옴
from time import sleep      #time 라이브러리의 sleep함수 사용

def servoSet():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)      # GPIO 핀들의 번호를 지정하는 규칙 설정

    ### 이부분은 아두이노 코딩의 setup()에 해당합니다
    servo1_pin = 25                   # 서보1 핀은 라즈베리파이 GPIO 12번핀으로
    servo2_pin = 8                    # 서보2 핀은 라즈베리파이 GPIO 7번핀으로
    servo3_pin = 16                  
    servo4_pin = 20                  

    GPIO.setup(servo1_pin, GPIO.OUT)  # 서보1 핀을 출력으로 설정
    GPIO.setup(servo2_pin, GPIO.OUT)  # 서보2 핀을 출력으로 설정
    GPIO.setup(servo3_pin, GPIO.OUT)
    GPIO.setup(servo4_pin, GPIO.OUT)
    
    servo1 = GPIO.PWM(servo1_pin, 50)  # 서보1 핀을 PWM 모드 50Hz로 사용
    servo2 = GPIO.PWM(servo2_pin, 50)  # 서보2 핀을 PWM 모드 50Hz로 사용
    servo3 = GPIO.PWM(servo3_pin, 50)
    servo4 = GPIO.PWM(servo4_pin, 50)

    servo1.start(0)  # 서보1의 초기값을 0으로 설정
    servo2.start(0)  # 서보2의 초기값을 0으로 설정
    servo3.start(0)
    servo4.start(0)
    
    servo = [servo1, servo2, servo3, servo4]
    
    return servo   

def servo1(servo1):
    servo1.ChangeDutyCycle(7)
    sleep(16)
    servo1.ChangeDutyCycle(12)
    sleep(2)
    
def servo2(servo2):
    servo2.ChangeDutyCycle(11)
    sleep(13)
    servo2.ChangeDutyCycle(6)
    sleep(2)

def servo3(servo3):
    servo3.ChangeDutyCycle(8)
    sleep(10)
    servo3.ChangeDutyCycle(3)
    sleep(2)

def servo4(servo4):
    servo4.ChangeDutyCycle(3)
    sleep(8)
    servo4.ChangeDutyCycle(7)
    sleep(2)

### 이부분은 반드시 추가해주셔야 합니다.
# finally:                                # try 구문이 종료되면
def servoClean():
    GPIO.cleanup()                      # GPIO 핀들을 초기화

