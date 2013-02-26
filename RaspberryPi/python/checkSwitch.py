# Script to break the functionality of setting and reading
# GPIO pins into functions. 

import RPi.GPIO as GPIO

def turnOn():
	# Set GPIO4 high
        pin=4
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, True)
        return

def turnOff():
	# Set GPIO4 Low
        pin = 4
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)
        return

def isOn():
	# Read the state of the button on GPIO6 and return the state
	# as a boolean value
        pin=6
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN)
        if(GPIO.input(pin)):
                return True
        else:
                return False

if(isOn()):
	print 'Switch ON'
else:
	print 'Switch OFF'
