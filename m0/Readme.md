# M0 Version of the Mouse Jiggler

Wrote this for the Adafruit Neo Trinkey - needed a mouse jiggler to stop my work laptop from suggesting I'm not working when I'm actually just AFK. Working from home is great but being watched is annoying, especially when large amounts of my time are reading and researching.

Requires CircuitPython 7.0.0 or higher, as it uses the `boot.py` file to identify as an HID device. Not as cost effective as the Pico but it looks better, doesn't need a cable and has the ability to re-enable USB storage.

**Default behaviour enables both REPL and USB storage - swap `enable()/disable()` in `boot.py` if you want to avoid logging.**

Code is trivial - it  moves the mouse x and y axis a random distance and moves it back again. `HOW_LONG` is the variable in seconds for the delay.
