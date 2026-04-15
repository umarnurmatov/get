import RPi.GPIO as GPIO


DAC_DRANGE_V = 3.3
DAC_DEPTH = 8
dac_pins = [16, 20, 21, 25, 26, 17, 27, 22]


class R2R_DAC:
	def __init__(self, pins, drange, verbose = False):
		self.pins = pins
		self.drange = drange
		self.verbose = verbose
		
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.pins, GPIO.OUT, initial=0)


	def set_voltage(self, voltage):
		num = 0
		if not (0.0 <= voltage <= self.drange) and self.verbose:
			print(f'Voltage out of DAC dynamic range [0.0,{self.drange}]V, 0.0V set')
		else:
			num = int(voltage / self.drange* 2**DAC_DEPTH)

		self.set_num(num)

	def set_num(self, num):
		bits = [int(bit) for bit in bin(num)[2:].zfill(DAC_DEPTH)]
		GPIO.output(self.pins, bits)

	def deinit(self):
		GPIO.output(self.pins, 0)
		GPIO.cleanup()
		
		


if __name__ == "__main__":
	dac = R2R_DAC(dac_pins, 3.183, True)

	try:
		while True:
			try:
				voltage = float(input("Enter voltage [V]:"))
				dac.set_voltage(voltage)
			except ValueError:
				print("Try again")
	finally:
		dac.deinit()

