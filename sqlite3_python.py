import sqlite3
import time
import serial
import string
 
print ("Starting... ")
serialData = serial.Serial(port = '/dev/ttyS0', # ttyS0 is for the RPi 3
                           baudrate = 19200,
                           parity = serial.PARITY_NONE,
                           stopbits = serial.STOPBITS_ONE,
                           bytesize = serial.EIGHTBITS,
                           timeout = 100)
 
my_Db = sqlite3.connect('SQL_DB.db')
cursor_Obj = my_Db.cursor()

'''
when selecting stuff in a query, multiple rows are returned so the cursor
remembers where in the query you are
'''
 
# Storing data from port to database
while True:
    windSpeed, date = t
    time1 = datetime.datetime.now()
    windSpeed = serialData # serial variable read from COM port
    print('Date: {0} windSpeed = {1:0.2f}%'format(date, windSpeed))
    cursor_Obj.execute('INSERT INTO Table1 VALUES (?, ?)',
                    (time1, '{0} Wind Speed: ', windSpeed)# finish
    cursor_Obj.commit() # must commit after each
    t.sleep(1) # reads once a second<span    