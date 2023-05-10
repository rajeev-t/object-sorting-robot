from machine import Pin
import time

switch = Pin(28, Pin.IN)

while True:
    print(switch.value())
    time.sleep(0.5)