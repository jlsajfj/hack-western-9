#!/usr/bin/env python3
import serial
import random
import sys
import spin

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        print('loop')
        number = ser.read()
        if number != b'':
            if int.from_bytes(number, byteorder='big') == 1:
                print("Threshold reached for 1")
                spin.open_door()
            elif int.from_bytes(number, byteorder='big') == 2:
                pass
                #print("Threshold reached for 2")
            
            ser.reset_input_buffer()