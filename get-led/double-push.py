import RPi.GPIO as GPIO
import time

leds = [16, 12, 25, 17, 27, 23, 22, 24]
sleep_time = 0.2
num = 0
up = 9
down = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(down, GPIO.IN)
GPIO.setup(up, GPIO.IN)
GPIO.output(leds, 0)

def dec2bin(value):
	return [int(element) for element in bin(value)[2:].zfill(8)]

while True:
	up_st = GPIO.input(up)
	down_st = GPIO.input(down)
	changed = False

	if up_st and down_st:
		num = 2**len(leds)-1
		changed = True

	elif up_st:
		num = min(num+1, 2**len(leds) - 1)
		changed = True

	elif down_st:
		num = max(num-1, 0)
		changed = True


	if changed:
		print(num, dec2bin(num))
		time.sleep(sleep_time)
		GPIO.output(leds, dec2bin(num))

		
