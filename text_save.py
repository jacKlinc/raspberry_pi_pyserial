import serial
import string
import csv

print ("Starting... ")
## Serial setup
ser = serial.Serial(port = '/dev/ttyS0', # ttyS0 is for the RPi 3
                    baudrate = 19200,
                    parity = serial.PARITY_NONE,
                    stopbits = serial.STOPBITS_ONE,
                    bytesize = serial.EIGHTBITS,
                    timeout = 100)

print ("Connected")
x = open("/home/pi/New.txt", "a")

while True:  
    data = ser.readline().strip() # Storing incoming data from serial channel to variable "data" and stripping string  
    x.write(data)
    x.close()