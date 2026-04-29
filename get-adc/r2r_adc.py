
import RPi.GPIO as GPIO
import time

class R2R_ADC:
	def __init__(self, drange, cmp_t = 0.01, verbose = False):
		self.drange = drange
		self.verbose = verbose
		self.cmp_t = cmp_t
		self.pins = [26, 20, 19, 16, 13, 12, 25, 11]
		self.cmp_pin = 21
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.pins, GPIO.OUT, initial=0)
		GPIO.setup(self.cmp_pin, GPIO.IN)

	def dac_set_num(self, num):
		depth = len(self.pins)
		bits = [int(bit) for bit in bin(num)[2:].zfill(depth)]
		GPIO.output(self.pins, bits)

	def seq_count_adc(self):
		width = len(self.pins)
		for i in range(2**width):
			self.dac_set_num(i)
			time.sleep(self.cmp_t)
			if GPIO.input(self.cmp_pin):
				break	

		return i-1

	def sar_adc(self):
		width = len(self.pins)
		l = 0
		r = 2**width-1
		while r > l:
			m = l + (r-l) // 2
			self.dac_set_num(m)
			time.sleep(self.cmp_t)
			if GPIO.input(self.cmp_pin):
				r = m
			else:
				l = m + 1
		return r-1


	def get_sar_voltage(self):
		depth = len(self.pins)
		return self.sar_adc() * self.drange/2**depth

	def get_sc_voltage(self):
		depth = len(self.pins)
		return self.seq_count_adc() * self.drange/2**depth
	
	def __del__(self):
		GPIO.output(self.pins, 0)
		GPIO.cleanup()

if __name__ == "__main__":
	adc = R2R_ADC(3.3)
	while True:
		try:
			print("{:.2f}V".format(adc.get_sar_voltage()))
		finally:
			pass
