import RPi.GPIO as GPIO
import time

led = 26
state = 0
period = 1.0
ptrans = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(ptrans, GPIO.IN)

while True:
	GPIO.output(led, not GPIO.input(ptrans))
	time.sleep(0.2)
