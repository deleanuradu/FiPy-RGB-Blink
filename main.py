import pycom
import time

pycom.heartbeat(False)

while True:
    pycom.rgbled(0xFF0000)  # Red
    time.sleep(1)
    pycom.rgbled(0x00FF00)  # Green
    time.sleep(1)
    pycom.rgbled(0x0000FF)  # Blue
    time.sleep(1)
    pycom.rgbled(0x9933FF)  # Violet
    time.sleep(1)
    pycom.rgbled(0xFF8000)  # Orange
    time.sleep(1)
    pycom.rgbled(0xFFFFFF)  # White
    time.sleep(1)
    pycom.rgbled(0xFF3399)  # Pink
    time.sleep(1)
