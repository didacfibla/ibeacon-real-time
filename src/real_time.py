# This is a working prototype. DO NOT USE IT IN LIVE PROJECTS
from utils import ScanUtility
import bluetooth._bluetooth as bluez  # pip install pybluez
from utils import KalmanFilter
import numpy
from matplotlib.pylab import *
import matplotlib.animation as animation


raw_rssi = [0]
filtered_rssi = [0]

filtro = KalmanFilter.KalmanFilter(0.001, 2)

# Coger datos de BLE y guardarlos en gData
def getData():

	global raw_rssi
	global filtered_rssi

	# Set bluetooth device. Default 0.
	dev_id = 0
	try:
		sock = bluez.hci_open_dev(dev_id)
		print("\n *** Looking for BLE Beacons ***\n")
		print("\n *** CTRL-C to Cancel ***\n")

	except:
		print("Error accessing bluetooth")

	ScanUtility.hci_enable_le_scan(sock)
	# Scans for iBeacons
	try:
		while True:
			returned_list = ScanUtility.parse_events(sock, 10)
			for item in returned_list:
				if item["minor"] == 30:
					rssi_actual = item["rssi"]
					raw_rssi.append(rssi_actual)
					rssi_filtrado=valor_filtrado=filtro.filter(rssi_actual)
					filtered_rssi.append(rssi_filtrado)

	except KeyboardInterrupt:
		pass

# Configuramos y lanzamos el hilo encargado de leer datos del serial
dataCollector = threading.Thread(target=getData, args=())
dataCollector.start()


# RAW data
gData = []
gData.append([0])
gData.append([0])

# Filter data
fData = []
fData.append([0])
fData.append([0])

# Setup figure and subplots
f0 = plt.figure(num=0, figsize=(12, 8))
ax01 = subplot2grid((2, 2), (0, 0))
ax02 = subplot2grid((2, 2), (0, 1))
ax03 = subplot2grid((2, 2), (1, 0), colspan=2, rowspan=1)
ax04 = ax03.twinx()

# Set titles of subplots
ax01.set_title('Señal RSSI RAW')
ax02.set_title('Señal RSSI con filtro Kalman')
ax03.set_title('RSSI RAW vs RSSI con filtro Kalman')

# set y-limits
ax01.set_ylim(-70, -30)
ax02.set_ylim(-70, -30)
ax03.set_ylim(-70, -30)
ax04.set_ylim(-70, -30)

# sex x-limits
ax01.set_xlim(0, 200)
ax02.set_xlim(0, 200)
ax03.set_xlim(0, 200)
ax04.set_xlim(0, 200)

# Turn on grids
ax01.grid(True)
ax02.grid(True)
ax03.grid(True)

# set label names
ax01.set_xlabel("t")
ax01.set_ylabel("RSSI(dBm)")
ax02.set_xlabel("t")
ax02.set_ylabel("RSSI(dBm)")
ax03.set_xlabel("t")
ax03.set_ylabel("RSSI(dBm)")
ax04.set_ylabel("RSSI(dBm)")

# Data Placeholders
rssi_filtrado = numpy.zeros(0)
rssi_raw = numpy.zeros(0)
num_muestras = numpy.zeros(0)

# set plots
p011, = ax01.plot(num_muestras, rssi_raw, 'r-', label="RSSI RAW", linewidth=2)

p021, = ax02.plot(num_muestras, rssi_filtrado, 'g-', label="RSSI filtrado", linewidth=2)

p031, = ax03.plot(num_muestras, rssi_raw, 'r-', label="RSSI RAW", linewidth=2)
p032, = ax04.plot(num_muestras, rssi_filtrado, 'g-', label="RSSI filtrado", linewidth=2)

# set lagends
ax01.legend([p011], [p011.get_label()])
ax02.legend([p021], [p021.get_label()])
ax03.legend([p031, p032], [p031.get_label(), p032.get_label()])

# Data Update
xmin = 0.0
xmax = 200
x = 0.0


def updateData(self):
	global x
	global rssi_filtrado
	global rssi_raw
	global num_muestras


	rssi_raw_temp = raw_rssi[-1]
	rssi_filtered_temp = filtered_rssi[-1]

	rssi_raw=append(rssi_raw,rssi_raw_temp)
	rssi_filtrado=append(rssi_filtrado,rssi_filtered_temp)

	num_muestras = numpy.append(num_muestras, x)



	x = len(raw_rssi)

	p011.set_data(num_muestras, rssi_raw)

	p021.set_data(num_muestras, rssi_filtrado)

	p031.set_data(num_muestras, rssi_raw)
	p032.set_data(num_muestras, rssi_filtrado)

	if x >= xmax - 1.00:
		p011.axes.set_xlim(x - xmax + 1.0, x + 1.0)
		p021.axes.set_xlim(x - xmax + 1.0, x + 1.0)
		p031.axes.set_xlim(x - xmax + 1.0, x + 1.0)
		p032.axes.set_xlim(x - xmax + 1.0, x + 1.0)

	return p011, p021, p031, p032


# interval: draw new frame every 'interval' ms
# frames: number of frames to draw
simulation = animation.FuncAnimation(f0, updateData, blit=False, interval=50, repeat=False)

# Uncomment the next line if you want to save the animation
# simulation.save(filename='sim.mp4',fps=30,dpi=300)

plt.show()

