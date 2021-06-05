"""Mouse Jiggler in CircuitPython for Raspberry Pico"""

import usb_hid
import board
import digitalio
from time import sleep
from adafruit_hid.mouse import Mouse
from random import randint

HOW_LONG = 180    # Pause between jiggles in seconds

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

mouse = Mouse(usb_hid.devices)

def blink(times):
    for each in range(times):
        led.value = False
        sleep(0.5)
        led.value = True
        print("Blink")

def jiggle():
    led.value = True
    for each in range(randint(1, 4)):
        x = randint(1, 50)
        y = randint(1, 50)
        mouse.move(x, y)
        mouse.move(-x, -y)
        blink(3)
    sleep(HOW_LONG)

while True:
    blink(3)
    jiggle()
    sleep(HOW_LONG)
