import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

m1a,m1b=8,7                     # defining motor pins

GPIO.setup(m1a,GPIO.OUT)        # set the motor pins as output
GPIO.setup(m1b,GPIO.OUT)        # set the motor pins as output

def forward():                  # rotate the motor clock wise
    GPIO.output(m1a,True)
    GPIO.output(m1b,False)

def backword():
    GPIO.output(m1a,False)      # rotate the motor anti clock wise
    GPIO.output(m1b,True)

def stop():
    GPIO.output(m1a,False)      # Stops the motor
    GPIO.output(m1b,False)
    
while True:     
    forward()
    time.sleep(1)
    stop()
    time.sleep(.5)
    backword()
    time.sleep(1)
    stop()
    time.sleep(.5)


