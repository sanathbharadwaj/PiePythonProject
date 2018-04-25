import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
#Define GPIO to use on Pi
GPIO_TRIGGER = 3
GPIO_ECHO    = 5
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)


# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo
while True:
    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER, False)

    # Allow module to settle
    time.sleep(0.5)

    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()

    while GPIO.input(GPIO_ECHO)==0:
        start = time.time()

    while GPIO.input(GPIO_ECHO)==1:
        stop = time.time()

    # Calculate pulse length
    elapsed = stop-start

    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * 34300

    # That was the distance there and back so halve the value
    distance = distance / 2

    print distance

    GPIO.output(31, True)
    GPIO.output(33, False)
    GPIO.output(35, True)
    GPIO.output(15, False)

    if distance < 5 :
        GPIO.output(31, False)
        GPIO.output(35, False)
        GPIO.output(15, False)
        GPIO.output(33, False)