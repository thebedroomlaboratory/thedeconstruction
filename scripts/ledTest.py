import GPIOUtil
from time import sleep
while True:
	print GPIOUtil.turnOn()
	sleep(1)
	print GPIOUtil.turnOff()
	sleep(1)
