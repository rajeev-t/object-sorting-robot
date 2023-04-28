# Dependencies
from machine import Pin, PWM
import time

servo = PWM(Pin(15))
servo.freq(100)
duty_min = int((1/20)*65535)
duty_max = int((3/20)*65535)

while True:
    servo.duty_u16(duty_min)
    time.sleep(2)
    servo.duty_u16(duty_max)
    time.sleep(2)