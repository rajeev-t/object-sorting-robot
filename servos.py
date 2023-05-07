from machine import Pin, PWM
import time

servo_j = PWM(Pin(14))
servo_j.freq(50)
servo_b = PWM(Pin(15))
servo_b.freq(75)

duty_standby = int((1/6.7)*65535)
duty_pickup = int((1/8)*65535)
duty_unsorted = int((4/80)*65535)
duty_90_from_unsorted = int((10.25/80)*65535)

duty_init = int((1/8)*65535)

t = 2

#servo_j.duty_u16(duty_init)
#time.sleep(t)
servo_b.duty_u16(duty_unsorted)
time.sleep(t)
servo_j.duty_u16(duty_standby)
time.sleep(t)
servo_j.duty_u16(duty_pickup)
time.sleep(t)
servo_j.duty_u16(duty_standby)
time.sleep(t)
servo_b.duty_u16(duty_90_from_unsorted)
time.sleep(t)
servo_j.duty_u16(duty_pickup)
time.sleep(t)
servo_j.duty_u16(duty_standby)
time.sleep(t)
servo_b.duty_u16(duty_unsorted)