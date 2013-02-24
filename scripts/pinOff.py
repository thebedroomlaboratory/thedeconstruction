from time import sleep
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pin = 4
GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, False)
