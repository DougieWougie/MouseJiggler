"""CircuitPython code to jiggle the mouse"""

import board
import neopixel
import usb_hid
from time import sleep
from adafruit_hid.mouse import Mouse
from random import randint
from _pixelbuf import colorwheel

HOW_LONG = 180     # How long between jiggles in seconds

mouse = Mouse(usb_hid.devices)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=False)
pixels.brightness = 0.02

def multi():
    color = colorwheel(randint(1, 255))
    for cycle in range(4):
        for led in range(4):
            pixels[led] = 0
        pixels[cycle] = color
        pixels.show()
        sleep(0.1)

def green():
    pixels.fill((0, 255, 0))
    pixels.show()
    sleep(0.1)

def jiggle():
    for each in range(randint(1, 4)):
        x = randint(1, 50)
        y = randint(1, 50)
        mouse.move(x, y)
        mouse.move(-x, -y)

green()

while True:
    jiggle()
    multi()
    green()
    sleep(HOW_LONG)    # Wait HOW_LONG
