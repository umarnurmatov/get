import matplotlib.pyplot as plt

def plot_v_vs_time(time, v, max_v):
	fig = plt.figure(figsize=(10,6))
	plt.plot(time, v)
	plt.title('V vs time')
	plt.xlabel('Time (s)')
	plt.ylabel('Voltage (V)')
	plt.ylim([0,max_v])
	plt.grid(True)
	plt.show()

