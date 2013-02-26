# Main script for our project. It reads the sensor data in from the
# Arduino and processes the readings so that specific values and their
# delimiters can be parsed/handled. At the end of each line of sensor
# data, a newline character is detected. When this happens, the control
# logic for turning on and off the heating circuit runs. This logic also involves
# reading the button inputs from the website interface and the physical
# button on the thermostat and keeping them as interrupts.

from time import sleep
from sys import exit
import serial
import thermo2
import GPIOUtil

print "Setting up USB serial connection"
serialFromArduino = serial.Serial("/dev/ttyACM0",9600)
serialFromArduino.flush()
print "Ready to read!"
startup = True
posInVal = 0
posOfVal = 1
values = [ 1, 0.0, None, 0, None ]
tempString = ""
tempFloat = 0.0
temperature = 0.0
tempLow=0
tempHigh=0
tempRight=0
heatingOn=True
buttonCount=0
buttonOn=GPIOUtil.isOn()
buttonOverrideActive=False

webOn=False
webCount=0
webOverrideActive=False
while True:
    try:
        val = serialFromArduino.read()
#        print(val)
        if (val == '\n'):
		if (startup == True):
			startup = False
		elif (startup == False):
 			#print temp, light
			values [posOfVal] = int(tempString)
			print tempString
			print values
			tempString = ""
			posInVal = 0
			posOfVal = 1
			thermo2.insertRow(values)
			values  = [ 1, 0.0, None, 0, None ]
			tempFlag = GPIOUtil.isOn()
			if (tempFlag!=buttonOn and not(heatingOn)):
				print "button pressed"
				buttonOn = tempFlag
				GPIOUtil.turnOn()
				heatingOn = True
				thermo2.setWebFlag("1", "0")
				buttonCount = 0
				buttonOverrideActive=True
			if (thermo2.getWebFlag() != heatingOn and not(heatingOn)):
				print "web changed"
				webOn = thermo2.getWebFlag()
				GPIOUtil.turnOn()
				heatingOn=True
				thermo2.setWebFlag("1","2")
				webCount=0
				webOverrideActive=True
			if (buttonOverrideActive):
				if (buttonCount<10):
					buttonCount += 1
					print "button ", buttonCount
				else:
					buttonCount = 0
					buttonOverrideActive = False
			elif (webOverrideActive):
				if (webCount < 60):
					webCount += 1
				else:
					webCount = 0
					webOverrideActive= False
			elif ((temperature < 18) and (heatingOn == False)):
				tempLow += 1
				tempHigh = 0
				tempRight = 0
				if (tempLow > 10):
					GPIOUtil.turnOn()
					heatingOn = True
					thermo2.setWebFlag("1","1")
					print "Turning heating on"
			elif ((temperature > 22) and (heatingOn == True)):
				tempHigh += 1
				tempLow = 0
				tempRight = 0
				if (tempHigh > 10):
					GPIOUtil.turnOff()
					heatingOn = False
					thermo2.setWebFlag("0","1")
					print "Turning heating off"
			elif (heatingOn == True):
				tempRight += 1
				tempHigh = 0
				tempLow = 0
				if (tempRight > 20):
					GPIOUtil.turnOff()
					heatingOn = False
					thermo2.setWebFlag("0","1")
					print "Turning heating off"
			#print values
			#save to database
	elif (val == '\r'):
		i=0		
	elif (val == '?'):
		if (startup == False):
			tempFloat = float(int(tempString))
			tempFloat /= 10
			tempFloat -= 7
			temperature = tempFloat
			values [posOfVal] = tempFloat
			print tempString
			tempString = ""
			posInVal = 0
			posOfVal += 2
	else :
		if (startup == False):
			tempString += str(val)
#		print '@'
#		print pos
#		print val
		#print '\n'
#		print "Next Value"
#		val = 4
#		pos += 1
 #       else :
#		print "case3"
 #       sleep(2)
    except KeyboardInterrupt: 
        exit()
