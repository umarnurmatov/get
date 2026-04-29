import r2r_adc
import adc_plot
import time
import sys

total_time = 0
if len(sys.argv) >= 2:
	total_time = int(sys.argv[1])
	print('Experiment duration: ', total_time)
else:
	raise RuntimeError

v_arr = []
t_arr = []

adc = r2r_adc.R2R_ADC(3.3)

start = time.time()
while time.time() - start <= total_time:
	v_arr.append(adc.get_sc_voltage())
	t_arr.append(time.time() - start)

adc_plot.plot_v_vs_time(t_arr, v_arr, 3.5)
