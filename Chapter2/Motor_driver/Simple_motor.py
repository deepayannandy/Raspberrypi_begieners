import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

m1a,m1b=8,7

GPIO.setup(m1a,GPIO.OUT)
GPIO.setup(m1b,GPIO.OUT)



def forward():
    GPIO.output(m1a,True)
    GPIO.output(m1b,False)



def backword():
    GPIO.output(m1a,False)
    GPIO.output(m1b,True)


    
def stop():
    GPIO.output(m1a,False)
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


