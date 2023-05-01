# Dependencies
from machine import Pin, PWM
import time

servo = PWM(Pin(15))
servo.freq(100)

duty_unsorted = int((4/80)*65535)
duty_90_from_unsorted = int((12/80)*65535)
duty_test = int((12/80)*65535)

servo.duty_u16(duty_test)