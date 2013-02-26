# Script which reads and prints all of the data received over
# USB from the Arduino

from time import sleep
from sys import exit
import serial
from thermo2 import insertRow

print "Setting up USB serial connection"
serialFromArduino = serial.Serial("/dev/ttyACM0",9600)
serialFromArduino.flush()
print "Ready to read!"
startup = True
posInVal = 0
posOfVal = 1
values = [ 5, 0.0, None, 0, None ]
tempString = ""
tempFloat = 0.0
while True:
    try:
        val = serialFromArduino.read()
        print(val)

    except KeyboardInterrupt: 
        exit()
