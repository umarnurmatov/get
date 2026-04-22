import mcp4725 as mcp
import signal_generator as sg

AMP = 2
SIG_FREQ = 10
SMPL_FREQ = 1000


DAC_DRANGE_V = 4.95

if __name__ == "__main__":
	dac = mcp.MCP4725(DAC_DRANGE_V)
	t = 0

	try:
		while True:
			voltage = AMP * sg.get_trig_wave(SIG_FREQ,t)
			dac.set_voltage(voltage)
			t += 1/SMPL_FREQ
			sg.wait_for_sampling_period(SMPL_FREQ)
	finally:
		dac.deinit()

