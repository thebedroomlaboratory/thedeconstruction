# Script that takes a pin number as an argument and a boolean value as a
# second argument. The specified GPIO pin is set high or low based on the
# boolean value.

from time import sleep
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

pin=int(sys.argv[1])
input=int(sys.argv[2])
GPIO.setup(pin, GPIO.OUT)
if(input==1):
	GPIO.output(pin, True)
elif(input==0):
	GPIO.output(pin, False)

