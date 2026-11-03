# Board: ESP32-S3-WROOM-1 (N8R8) – LED = GPIO 5
from machine import Pin
from time import sleep

led = Pin(5, Pin.OUT)
while True:
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)
