from time import sleep
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
    
GPIO.output(4, True)

