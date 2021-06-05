'''
CircuitPython code to jiggle the mouse 
'''

import board
import neopixel
import usb_hid
from time import sleep
from adafruit_hid.mouse import Mouse

HOW_LONG = 180                # How long between jiggles in seconds

mouse = Mouse(usb_hid.devices)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixels.brightness = 0.02

while True:
    pixels.fill((0, 255, 0))  # Green LED show's working
    sleep(HOW_LONG)                # Wait HOW_LONG
    pixels.fill((255, 0, 0))  # Red LED before when jiggling
    mouse.move(10, 10)
    mouse.move(-5, 5)
    mouse.move(-10, -10)
    mouse.move(5, 5)
    sleep(1)                  # So the light is seen
