# Dependencies
from machine import Pin, PWM
import time

servo = PWM(Pin(15))
servo.freq(50)
duty_180 = int((1/20)*65535)
duty_135 = int((1/15)*65535)
duty_90 = int((1/10)*65535)
duty_45 = int((1/8)*65535)

servo.duty_u16(duty_45)

#while True:
    #servo.duty_u16(duty_min)
    #time.sleep(5)
    #servo.duty_u16(duty_max)
    #time.sleep(5)