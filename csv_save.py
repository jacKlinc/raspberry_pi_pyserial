import datetime
import csv
import serial
import string

print ("Starting... ")
serialData = serial.Serial(port = '/dev/ttyS0', # ttyS0 is for the RPi 3
                    baudrate = 19200,
                    parity = serial.PARITY_NONE,
                    stopbits = serial.STOPBITS_ONE,
                    bytesize = serial.EIGHTBITS,
                    timeout = 100)

with open('MyCSV.csv', 'w') as file: # with is a better way to access a file 
    write = csv.writer(file)
    write.writerow([' ', 'UPV', 'A. Bailey', 'J. Harding', 'P. Malone'])
    write.writerow([' ']) # adds a blank row
    write.writerow([' ', 'Date', 'Wind Direction', 'Wind Speed', 'Voltage', 'Current', 'Power'])
    write.writerow([' ']) # adds a blank row
    
    while True:  
        data = serialData.readline().strip() # Storing incoming data from serial channel to variable "data" and stripping string
        print(data)
        time1 = datetime.datetime.now()
        time1.strftime("%A %d %b  %y %H") # strftime: date formatting
        write.writerow([' ', time1, data])

