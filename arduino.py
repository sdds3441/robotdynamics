import cv2
import numpy as np
import serial
import time
import threading

outputs = 0
First = True
past_input=0
distance=[]
sec=0
def timer():
    global sec
    sec += 1

    timers = threading.Timer(1, timer)
    timers.start()

   # if sec == 3:
      #  timers.cancel()

def pid(kp, ki, kd, input_data, goal):
    global First
    global past_input
    global outputs
    if First:
        outputs = 0
        past_input = 0
    input_diff = input_data - past_input
    error = goal - input_data
    outputs += ki * error
    if 30 < outputs:
        outputs = 30
    elif outputs < -30:
        outputs = -30
    output_data = kp * error
    output_data += outputs - kd * input_diff
    if 30 < output_data:
        output_data = 30
    elif output_data < -30:
        output_data = -30

    if First:
        First = False
    input_data=past_input
    return output_data


py_serial = serial.Serial(

    # Window
    port='COM6',

    # 보드 레이트 (통신 속도)
    baudrate=9600,
)

while True:
    if sec == 0:
        timer()
    time.sleep(0.01)

    if py_serial.readable():
        # 들어온 값이 있으면 값을 한 줄 읽음 (BYTE 단위로 받은 상태)
        # BYTE 단위로 받은 response 모습 : b'\xec\x97\x86\xec\x9d\x8c\r\n'
        response = py_serial.readline()
        response=response[:len(response) - 1].decode()
        # 디코딩 후, 출력 (가장 끝의 \n을 없애주기위해 슬라이싱 사용)
        print(response)
        distance.append(float(response))
        key = cv2.waitKey(1) & 0xFF  # 키보드 입력을 무한 대기, 8비트 마스크 처리
        print(sec)

    if sec==30: # 'q' 또는 'esc'이면 종료
        np.savetxt("dataset//dist.csv", distance, delimiter=",", fmt="%.5f")
        exit()
        break





