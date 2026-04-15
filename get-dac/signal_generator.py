import numpy as np
import time

def get_sin_wave_ampl(freq, time):
	return (np.sin(2*np.pi*freq*time)+1)/2

def wait_for_sampling_period(smpl_freq):
	"""
	smpl_freq in Hz
	"""

	time.sleep(1/smpl_freq)
