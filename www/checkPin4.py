from time import sleep
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pin = 4
print 'Setting up Pin 4'
GPIO.setup(pin, GPIO.OUT)
print 'Turning on pin 4'
GPIO.output(pin, TRUE)
print 'Done!'

sys.exit(0)
