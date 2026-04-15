import smbus

DAC_DEPTH = 12

class MCP4725:
	def __init__(self, drange, addr=0x61, verbose = True):
		self.bus = smbus.SMBus(1)
		self.addr = addr
		self.wm = 0x00
		self.pds = 0x00
		self.verbose = verbose
		self.drange = drange


	def set_voltage(self, voltage):
		num = 0
		if not (0.0 <= voltage <= self.drange) and self.verbose:
			print(f'Voltage out of DAC dynamic range [0.0,{self.drange}]V, 0.0V set')
		else:
			num = int(voltage / self.drange* 2**DAC_DEPTH)

		self.set_num(num)

	def set_num(self, num: int):

		if not (0 <= num < 2**DAC_DEPTH):
			print("Out of MCP4725 depth (12)")
			return
		
		byte_0 = self.wm | self.pds | num >> 8
		byte_1 = num & 0xFF
		self.bus.write_byte_data(self.addr, byte_0, byte_1)
		
		if self.verbose:
			print(f"Sent via I2C: [0x{(self.addr << 1):02X}, 0X{byte_0:02X}, 0x{byte_1:02X}]")

	
	def deinit(self):
		self.bus.close()	

if __name__ == "__main__":
	dac = MCP4725(4.95)

	try:
		while True:
			try:
				voltage = float(input("Enter voltage [V]:"))
				dac.set_voltage(voltage)
			except ValueError:
				print("Try again")
	finally:
		dac.deinit()

