"""
Here be sharks...

Remember this disables identifying as USB or REPL so it works on locked down devices (assuming the allow HID).
Insert and then press both touchpads to enable as HID only device. 

More here https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial#dont-lock-yourself-out-3096636-14
"""

import board
import touchio
from time import sleep
import storage
import usb_cdc

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

def disable():
    storage.disable_usb_drive()    # Disable USB storage
    usb_cdc.disable()              # Disable REPL

def enable():
    print("enable")

sleep(3)    # Without a pause, the system never detects both pads
if touch1.value and touch2.value:
    disable()
else:
    enable()
