import RPi.GPIO as GPIO

class PWM_DAC:
	def __init__(self, pin, freq, drange, verbose = False):
		self.pin = pin
		self.freq = freq
		self.drange = drange
		self.verbose = verbose
		
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.pin, GPIO.OUT, initial=0)
		self.pwm = GPIO.PWM(self.pin,freq)
		self.pwm.start(0)


	def set_voltage(self, voltage):
		duty = 0
		if not (0.0 <= voltage <= self.drange) and self.verbose:
			print(f'Voltage out of DAC dynamic range [0.0,{self.drange}]V, 0.0V set')
		else:
			duty = voltage / self.drange * 100

		self.set_duty(duty)

	def set_duty(self, duty):
		self.pwm.ChangeDutyCycle(duty)

	def deinit(self):
		self.pwm.stop()
		GPIO.cleanup()
		
		


if __name__ == "__main__":
	dac = PWM_DAC(12, 500, 3.290, True)

	try:
		while True:
			try:
				voltage = float(input("Enter voltage [V]:"))
				dac.set_voltage(voltage)
			except ValueError:
				print("Try again")
	finally:
		dac.deinit()

