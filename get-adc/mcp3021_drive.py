import smbus

class MCP3021:
	def __init__(self, drange, addr=0x4D, verbose = False):
		self.bus = smbus.SMBus(1)
		self.addr = addr
		self.verbose = verbose
		self.drange = drange
		self.depth = 10

	def get_num(self):
		data = self.bus.read_word_data(self.addr, 0)
		lsb = data >> 8
		msb = data & 0xFF
		num = (msb << 6) | (lsb >> 2)
		if self.verbose:
			print(f'{data} {msb} {lsb} {num}')

	def get_voltage(self):
		return self.get_num() * self.drange / 2**self.depth


	
	def __del__(self):
		self.bus.close()	

if __name__ == "__main__":
	adc = MCP3021(4.95)
	while True:
		try:
			print("{:.2f}V".format(adc.get_voltage()))
			time.sleep(1)
		finally:
			pass

