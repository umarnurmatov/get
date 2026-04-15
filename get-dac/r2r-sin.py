import r2r_dac as r2r
import signal_generator as sg

AMP = 2
SIG_FREQ = 10
SMPL_FREQ = 250


DAC_DRANGE_V = 3.25
DAC_DEPTH = 8
dac_pins = [16, 20, 21, 25, 26, 17, 27, 22]

if __name__ == "__main__":
	dac = r2r.R2R_DAC(dac_pins, DAC_DRANGE_V, True)
	t = 0

	try:
		while True:
			voltage = AMP * sg.get_sin_wave_ampl(SIG_FREQ,t)
			dac.set_voltage(voltage)
			t += 1/SMPL_FREQ
			sg.wait_for_sampling_period(SMPL_FREQ)
	finally:
		dac.deinit()

