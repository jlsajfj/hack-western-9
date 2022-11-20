import RPi.GPIO as GPIO
from time import sleep

SLEEP_TIME = 0.002

#assign GPIO pins for motor
motor_channel = (29,31,33,35)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#for defining more than 1 GPIO channel as input/output use
GPIO.setup(motor_channel, GPIO.OUT)

def cw(n):
    for _ in range(n):
        GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
        sleep(SLEEP_TIME)
        GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
        sleep(SLEEP_TIME)
        GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
        sleep(SLEEP_TIME)
        GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
        sleep(SLEEP_TIME)

def ccw(n):
    for _ in range(n):
        GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
        sleep(SLEEP_TIME)
        GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
        sleep(SLEEP_TIME)
        GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
        sleep(SLEEP_TIME)
        GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
        sleep(SLEEP_TIME)

def open_door(direction = 'left'):
    if direction == 'left':
        cw(105)
        sleep(5)
        ccw(105)
    else:
        ccw(105)
        sleep(5)
        cw(105)

    sleep(2)
    return

if __name__=='__main__':
    open_door('left')
    sleep(2)
    open_door('right')
