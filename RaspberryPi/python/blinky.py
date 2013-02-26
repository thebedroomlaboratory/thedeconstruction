# Script to make LEDs attached to GPIO7 and GPIO11
# flash on and off. sleep() is used to associate a
# delay with the flashing.

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
while 1:
     	GPIO.output(7, False)
     	sleep(1)
     	GPIO.output(7, True)
     	sleep(1)
     	GPIO.output(11, False)
	sleep(1)
	GPIO.output(11, True)
	sleep(1)


	 

