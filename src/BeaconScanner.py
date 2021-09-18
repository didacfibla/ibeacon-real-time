# This is a working prototype. DO NOT USE IT IN LIVE PROJECTS
import time
from utils import ScanUtility
import bluetooth._bluetooth as bluez #pip install pybluez

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

    while True:

        returnedList = ScanUtility.parse_events(sock, 10)
        for item in returnedList:
            print(item)


except KeyboardInterrupt:
    pass
