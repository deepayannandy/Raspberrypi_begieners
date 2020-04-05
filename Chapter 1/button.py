import RPi.GPIO as GPIO    	# Default library to contol GPIO pins of raspberry pi
import time					# python library for adding delay dunctions

GPIO.setmode(GPIO.BOARD)	# this function set the naming convention of the gpio pins 

GPIO.setup(7, GPIO.IN, pull_up_down= GPIO.PUD_UP)	# this function makes the given pin(8) as a input pin and an input Pull_up

while True:
	if GPIO.input(7)== 0:							# this part checks the button is pressed or not
		print("Led pussed")							# if pressed then this block will execute 
		time.sleep(.5)
	else:											# otherwise nothing will happens 
		pass