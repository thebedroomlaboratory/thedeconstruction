import GPIOUtil
from time import sleep
while True:
	print GPIOUtil.isOn()
	sleep(1)
