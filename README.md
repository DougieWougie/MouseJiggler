# MouseJiggler
Mouse Jiggler in CircuitPython for ATSAMD21 (M0) or Raspberry Pico

Requires CircuitPython [M0](https://circuitpython.org/board/neopixel_trinkey_m0/)/[Pico](https://circuitpython.org/board/raspberry_pi_pico/) higher than version 7.0.0 (support for code.py rather than rebuilding CircuitPython).
- [Adafruit Neo Trinkey (M0)](https://shop.pimoroni.com/products/adafruit-neo-trinkey-samd21-usb-key-with-4-neopixels)
- [Raspberry Pi Pico](https://shop.pimoroni.com/products/raspberry-pi-pico?variant=32402092294227)

The code is self explanatory but do make sure it works before adding `boot.py`! For the Pico, with no inputs, there's no choice but to fly in the face of the [advice](https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial#dont-lock-yourself-out-3096636-14]) from Adafruit and could lock you out.

Links to UF2 bootloader erase files for [M0](https://learn.adafruit.com/welcome-to-circuitpython/troubleshooting#old-way-for-non-express-boards-with-a-uf2-bootloader-gemma-m0-trinket-m0-2978463-43) and [Pico](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython?view=all#flash-resetting-uf2-3083182-8).

Worth reading this Adafruit [howto on customising USB devices](https://learn.adafruit.com/customizing-usb-devices-in-circuitpython) for more information.
