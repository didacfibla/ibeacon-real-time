# This is a working prototype. DO NOT USE IT IN LIVE PROJECTS
from utils import ScanUtility
import bluetooth._bluetooth as bluez #pip install pybluez
import sys
import bottleneck as bn #pip3 install bottleneck
import matplotlib.pyplot as plt
import numpy as np

def rollavg_bottlneck(a,n): #a es la lista de rssi
	np_array_movil = np.array(bn.move_mean(a, window=n,min_count = None))
	np_round = np.around(np_array_movil, 2)
	return list(np_round)

# Set bluetooth device. Default 0.
dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print("*** Looking for BLE Beacons ***")
	print("*** CTRL-C to Cancel ***")
except:
	print("Error accessing bluetooth")

ScanUtility.hci_enable_le_scan(sock)

# Scans for iBeacons
try:

	lista_rssi=[]

	while True:

		returnedList = ScanUtility.parse_events(sock, 10)
		for item in returnedList:


			if item["minor"] == 58:
				rssi_actual = item["rssi"]
				lista_rssi.append(rssi_actual)
				print(len(lista_rssi))

				if len(lista_rssi) == 50:
					lista_media_movil = rollavg_bottlneck(lista_rssi, 3)
					print(lista_media_movil)
					
					plt.plot(lista_rssi,'-', label="RSSI Original", color='r', lw=2)
					plt.plot(lista_media_movil,'-', label="Media movil", color='b', lw=2)

					plt.ylabel("RSSI(dBm)")
					plt.xlabel("Num. muestras")

					plt.yticks(np.arange(-80, -30, 2))
					plt.xticks(np.arange(0,205,5))
					
					plt.legend()
					plt.grid()						
					plt.show()

					sys.exit(0)

except KeyboardInterrupt:
	pass


