# Din til WS2812B-kæden er GPIO 10.
# ANTAL_PIXELS=3 er en eksempelværdi. Brug det rigtige antal fra printet.
from machine import Pin
from neopixel import NeoPixel
from time import sleep

ANTAL_PIXELS = 3
pixels = NeoPixel(Pin(10, Pin.OUT), ANTAL_PIXELS)
while True:
    for farve in ((20, 0, 0), (0, 20, 0), (0, 0, 20)):
        for i in range(ANTAL_PIXELS):
            pixels[i] = farve
        pixels.write()
        sleep(1)
