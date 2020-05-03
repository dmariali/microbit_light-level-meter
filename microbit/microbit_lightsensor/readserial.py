import os
import serial

ser = serial.Serial('/dev/ttyACM0', 115200)
ser.flushInput() 


def updateContext ():
    temp = 0
    location = ""
    context = {'temps': temp, 'locations': location }

    while True:
        try:
            ser_bytes = ser.readline()
            var_list = str(ser_bytes).split(',')

            temp=int (var_list[0].strip("b\'"))
            print('Temp: ', temp)
            context['temps'] = temp

            location = var_list[1].split(' ', 1)[0]
            print("location: ", location)
            context['locations'] = location

            return context;

        except:
            print("Keyboard Interrupt")
            break


