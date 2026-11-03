# Knappen på GPIO 11 er aktiv lav (tryk = 0). LED på GPIO 5.
from machine import Pin
from time import sleep_ms

led = Pin(5, Pin.OUT)
knap = Pin(11, Pin.IN, Pin.PULL_UP)
while True:
    led.value(1 if knap.value() == 0 else 0)
    sleep_ms(20)
