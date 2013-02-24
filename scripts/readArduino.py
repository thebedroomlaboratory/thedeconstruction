from time import sleep
from sys import exit
import serial
from thermo2 import insertRow
import GPIOUtil

#print "Setting up USB serial connection"
serialFromArduino = serial.Serial("/dev/ttyACM0",9600)
serialFromArduino.flush()
#print "Ready to read!"
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
switchCount=0
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
#			print tempString
#			print values
			tempString = ""
			posInVal = 0
			posOfVal = 1
			insertRow(values)
			values  = [ 1, 0.0, None, 0, None ]
			if (GPIOUtil.isOn()):
				if (switchCount < 20):
					switchCount += 1
				
			if ((temperature < 18) and (heatingOn == False)):
				tempLow += 1
				tempHigh = 0
				tempRight = 0
				if (tempLow > 10):
					GPIOUtil.turnOn()
					heatingOn = True
#					print "Turning heating on"
			elif ((temperature > 22) and (heatingOn == True)):
				tempHigh += 1
				tempLow = 0
				tempRight = 0
				if (tempHigh > 10):
					GPIOUtil.turnOff()
					heatingOn = False
#					print "Turning heating off"
			elif (heatingOn == True):
				tempRight += 1
				tempHigh = 0
				tempLow = 0
				if (tempRight > 20):
					GPIOUtil.turnOff()
					heatingOn = False
#					print "Turning heating off"
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
#			print tempString
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
