from machine import Pin
import time

npn = Pin(19, Pin.OUT)

while True:
    npn.high()
    time.sleep(2)
    npn.low()
    time.sleep(2)