import pwm_dac
import signal_generator as sg

AMP = 2
SIG_FREQ = 10
SMPL_FREQ = 1000
PWM_FREQ = 5000


DAC_DRANGE_V = 3.290
PWM_PIN = 12

if __name__ == "__main__":
	dac = pwm_dac.PWM_DAC(PWM_PIN, PWM_FREQ, DAC_DRANGE_V, True)
	t = 0

	try:
		while True:
			voltage = AMP * sg.get_trig_wave(SIG_FREQ,t)
			dac.set_voltage(voltage)
			t += 1/SMPL_FREQ
			sg.wait_for_sampling_period(SMPL_FREQ)
	finally:
		dac.deinit()

