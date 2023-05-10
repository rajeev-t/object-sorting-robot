from machine import Pin, PWM
import time

ir = Pin(19, Pin.IN)

while True:
    print(ir.value())
    time.sleep(1) 