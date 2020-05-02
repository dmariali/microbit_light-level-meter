import os
import serial

ser = serial.Serial('/dev/ttyACM0', 115200)
ser.flushInput() 

while True:
    try:
        ser_bytes = ser.readline()
        print(ser_bytes)
    except:
        print("Keyboard Interrupt")
        break
