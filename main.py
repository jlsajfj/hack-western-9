#!/usr/bin/env python3
import serial
import random
import sys
import spin


SPIN_COUNT = 10

motor_direction = input('select motor direction a=anticlockwise, c=clockwise: ')

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        number = ser.read()
        if number != b'':
            if int.from_bytes(number, byteorder='big') == 1:
                print("Threshold reached for 1")
                
                if(motor_direction == 'c'):
                    print('motor running clockwise\n')
                    spin.cw(SPIN_COUNT)

                elif(motor_direction == 'a'):
                    print('motor running anti-clockwise\n')
                    spin.ccw(SPIN_COUNT)

            elif int.from_bytes(number, byteorder='big') == 2:
                pass
                #print("Threshold reached for 2")