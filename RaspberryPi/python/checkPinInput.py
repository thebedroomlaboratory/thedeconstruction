# Script that takes a pin number as an argument and reads the
# value of a switch attached to that GPIO pin

from time import sleep
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

pin=int(sys.argv[1])
GPIO.setup(pin, GPIO.IN)
if(GPIO.input(pin)):
        print 'Switch On'
else:
        print 'Switch Off'
