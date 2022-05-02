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
    # Flash the LED with a half second gap
    for x in range(times):
        led.value = False
        sleep(0.5)
        led.value = True
        print(x)

def jiggle():
    # Move cursor a random x and y distance between 1 and 50 pixels then move it back
    for each in range(randint(1, 4)):
        x = randint(1, 50)
        y = randint(1, 50)
        mouse.move(x, y)
        mouse.move(-x, -y)
    sleep(HOW_LONG)

while True:
    led.value = True
    blink(3)
    jiggle()
