'''
Here be sharks...
Remember this disables identifying as USB or REPL so it works on locked down devices (assuming the allow HID).
More here https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial#dont-lock-yourself-out-3096636-14
'''

import storage
import usb_cdc

storage.disable_usb_drive()    # Disable USB Drive
usb_cdc.disable()              # Disable REPL
