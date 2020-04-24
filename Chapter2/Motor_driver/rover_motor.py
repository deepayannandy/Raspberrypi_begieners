import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

m1a,m1b,m2a,m2b=8,7,11,12

GPIO.setup(m1a,GPIO.OUT)
GPIO.setup(m1b,GPIO.OUT)
GPIO.setup(m2a,GPIO.OUT)
GPIO.setup(m2b,GPIO.OUT)


def forward():
    GPIO.output(m1a,True)
    GPIO.output(m1b,False)
    GPIO.output(m2a,True)
    GPIO.output(m2b,False)


def backword():
    GPIO.output(m1a,False)
    GPIO.output(m1b,True)
    GPIO.output(m2a,False)
    GPIO.output(m2b,True)

def right():
    GPIO.output(m1a,False)
    GPIO.output(m1b,True)
    GPIO.output(m2a,True)
    GPIO.output(m2b,False)

def left():
    GPIO.output(m1a,True)
    GPIO.output(m1b,False)
    GPIO.output(m2a,False)
    GPIO.output(m2b,True)

    
def stop():
    GPIO.output(m1a,False)
    GPIO.output(m1b,False)
    GPIO.output(m2a,False)
    GPIO.output(m2b,False)


while True:
    direc=input("Enter choice: ")
    if direc == "w":
        forward()
    elif direc == "s":
        backword()
    elif direc == "a":
        right()
    elif direc == "d":
        left()
    elif direc == "x":
        stop()


