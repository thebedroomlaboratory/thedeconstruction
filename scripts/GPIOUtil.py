import RPi.GPIO as GPIO

def turnOn():
	pin=4
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT)
    	GPIO.output(pin, True)
	return

def turnOff():
	pin = 4
	GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, False)
	return

def isOn():
	pin=17
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.IN)
	if(GPIO.input(pin)):
		return True
	else:
		return False
