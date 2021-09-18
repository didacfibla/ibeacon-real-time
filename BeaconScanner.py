# This is a working prototype. DO NOT USE IT IN LIVE PROJECTS
import time
import ScanUtility
import bluetooth._bluetooth as bluez #pip install pybluez
import statistics
import sys
import matplotlib.pyplot as plt
import numpy as np

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
lista_rssi=[]
contador=0
try:
    measuredPower = -60
    N=1

    # K es para establecer los limites
    K = 1.28
    while True:

        returnedList = ScanUtility.parse_events(sock, 10)
        for item in returnedList:
            item["distance:"] = 10 ** ((measuredPower - item["rssi"]) / (10 * N))

            if item["minor"] ==30:
                rssi_actual = item["rssi"]
                if len(lista_rssi)!=1000:
                    lista_rssi.append(rssi_actual)
                    #print(len(lista_rssi))
                else:
                    contador+=1
                    media = statistics.mean(lista_rssi)
                    print("Media: ",media)
                    lista_rssi.clear()
                    if contador==4:
                        sys.exit(0)


except KeyboardInterrupt:
    pass