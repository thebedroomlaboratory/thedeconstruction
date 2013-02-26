# Loop a program which flashes an LED on GPIO4 for second on and a
# second off. The heavy lifting is done by the GPIOUtil.py script.

import GPIOUtil
from time import sleep
while True:
	print GPIOUtil.turnOn()
	sleep(1)
	print GPIOUtil.turnOff()
	sleep(1)
