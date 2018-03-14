import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, 11, 13, 15, GPIO.OUT)

while true:
    a = input("Enter 1 or 2")
    if a is 1 :
        GPIO.output(10, True)
        GPIO.output(11, False)
    else:
        GPIO.output(13, True)
        GPIO.output(15, False)