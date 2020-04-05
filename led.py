import RPi.GPIO as GPIO    	# Default library to contol GPIO pins of raspberry pi
import time					# python library for adding delay dunctions

GPIO.setmode(GPIO.BOARD)	# this function set the naming convention of the gpio pins 

GPIO.setup(8, GPIO.OUT)		# this function makes the given pin as a output pin

while True:
	GPIO.output(8, True)	# this function change the GPIO voltage to +5 volts 
	print("Led On")			# ptints a message
	time.sleep(1)			# this function dives a delay of 1 sec. you can change the value and (1 = 1 sec)

	GPIO.output(8, False)	# this function change the GPIO voltage to 0 volts
	print("Led Off")		# ptints a message
	time.sleep(1)			# this function dives a delay of 1 sec. you can change the value and (1 = 1 sec)