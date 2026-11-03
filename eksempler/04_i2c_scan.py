# I2C: SDA GPIO 8, SCL GPIO 9. Enheder skal være tilsluttet.
from machine import Pin, I2C

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=100000)
print('I2C-enheder:', [hex(a) for a in i2c.scan()])
