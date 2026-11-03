# HC-SR04: trig GPIO 7, echo GPIO 6.
# VIGTIGT: Kontroller at echo kun er 3,3 V på dit fysiske print.
from machine import Pin, time_pulse_us
from time import sleep_us, sleep

trig = Pin(7, Pin.OUT)
echo = Pin(6, Pin.IN)

def afstand_cm():
    trig.off()
    sleep_us(2)
    trig.on()
    sleep_us(10)
    trig.off()
    tid = time_pulse_us(echo, 1, 30000)
    if tid < 0:
        return None
    return tid * 0.0343 / 2

while True:
    print('Afstand i cm:', afstand_cm())
    sleep(0.5)
