import datetime
import serial
import string

print ("Starting... ")
# Serial setup
ser = serial.Serial(port = '/dev/ttyS0', # ttyS0 is for the RPi 3
                    baudrate = 19200, # these must match the Transmitting side's config
                    parity = serial.PARITY_NONE,
                    stopbits = serial.STOPBITS_ONE,
                    bytesize = serial.EIGHTBITS,
                    timeout = 100)

print ("Connected")

while True:
     for j in range(0,5 + 1):  
        if ser.inWaiting() > 0: # inWaiting returns number of bytes in input buffer
            data = ser.readline().strip() # takes entire line and strips string
            print(data)

