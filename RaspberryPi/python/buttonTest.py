# Simple script to print the state of a switch which is
# attached to GPIO17 every second to the terminal. The
# heavy lifting is done in the GPIOUtil.py script in this
# directory.

import GPIOUtil
from time import sleep
while True:
	print GPIOUtil.isOn()
	sleep(1)
