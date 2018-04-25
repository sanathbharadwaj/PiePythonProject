import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

while true:
    a = input("Enter 1 or 2")
    if a is 1 :
        GPIO.output(31, True)
        GPIO.output(33, False)
        
    else:
        GPIO.output(35, True)
        GPIO.output(15, False)