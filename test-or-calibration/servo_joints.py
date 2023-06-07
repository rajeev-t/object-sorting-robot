# Dependencies
from machine import Pin, PWM
import time

servo = PWM(Pin(14))
servo.freq(50)

# move to standby, place links at a 90 angle
duty_standby = int((1/10)*65535)
duty_pickup = int((1/13)*65535)

duty_180 = int((1/20)*65535)

#servo.duty_u16(duty_standby)
#servo.duty_u16(duty_pickup)

# duty_45 = int((1/8)*65535)
#while True:
 #   servo.duty_u16(duty_pickup)
  #  time.sleep(2)
   # servo.duty_u16(duty_standby)
    #time.sleep(2)
    

#while True:
    #servo.duty_u16(duty_min)
    #time.sleep(5)
    #servo.duty_u16(duty_max)
    #time.sleep(5)