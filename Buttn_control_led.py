import RPi.GPIO as GPIO    	# Default library to contol GPIO pins of raspberry pi
import time					# python library for adding delay dunctions

GPIO.setmode(GPIO.BOARD)	# this function set the naming convention of the gpio pins 

GPIO.setup(8, GPIO.OUT)		# this function makes the given pin(8) as a output pin
GPIO.setup(7, GPIO.IN, pull_up_down= GPIO.PUD_UP)	# this function makes the given pin(8) as a input pin and an input Pull_up

while True:
	if GPIO.input(7)== 0:							# this part checks the button is pressed or not
		print("Led pussed")							# if pressed then this block will execute 
		GPIO.output(8, True)						# this function change the GPIO voltage to +5 volts 
		print("Led On")								# ptints a message
		time.sleep(.5)								# this function dives a delay of .5 sec. you can change the value and (1 = 1 sec)


	else:											# otherwise nothing will happens 
		GPIO.output(8, False)						# this function change the GPIO voltage to 0 volts
		print("Led Off")							# ptints a message
		time.sleep(.5)								# this function dives a delay of .5 sec. you can change the value and (1 = 1 sec)