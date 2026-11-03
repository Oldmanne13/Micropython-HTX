# Buzzer-net på GPIO 12. Eksemplet forudsætter en passiv buzzer.
# Hvis komponenten er aktiv, kræver den anden styring.
from machine import Pin, PWM
from time import sleep

buzzer = PWM(Pin(12), freq=880, duty_u16=0)
try:
    buzzer.duty_u16(4000)
    sleep(0.3)
finally:
    buzzer.duty_u16(0)
    buzzer.deinit()
