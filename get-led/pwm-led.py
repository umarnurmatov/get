import RPi.GPIO as GPIO
import time

led = 26
state = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
pwm = GPIO.PWM(led, 200)
duty = 0
pwm.start(duty)

while True:
	pwm.ChangeDutyCycle(duty)
	time.sleep(.05)
	
	duty = (duty+1) % 100
