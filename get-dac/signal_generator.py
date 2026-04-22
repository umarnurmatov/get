import numpy as np
from scipy import signal
import time

def get_sin_wave_ampl(freq, time):
	return (np.sin(2*np.pi*freq*time)+1)/2

def get_trig_wave(freq, time):
	return (signal.sawtooth(4*np.pi*freq*time,0.5)+1)/2

def wait_for_sampling_period(smpl_freq):
	"""
	smpl_freq in Hz
	"""

	time.sleep(1/smpl_freq)
