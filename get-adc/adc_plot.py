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


def plot_smpl_period(time):
	distrib = [time[i+1]-time[i] for i in range(len(time)-1)]
	plt.figure()
	plt.hist(distrib)
	plt.xlim(0.06)
	plt.show()
