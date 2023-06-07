from machine import Pin, PWM
import time
from lcd import my_lcd

servo_j = PWM(Pin(2))
servo_j.freq(50)
servo_b = PWM(Pin(3))
servo_b.freq(75)

duty_standby = int((1/6.7)*65535)
duty_pickup = int((1/9.4)*65535)
duty_unsorted = int((4/80)*65535)
#duty_90_from_unsorted = int((10.25/80)*65535)
duty_second = int((8/80)*65535)
duty_first = int((6.5/80)*65535)
duty_third = int((9.3/80)*65535)

duty_init = int((1/8)*65535)

t = 2
t2 = 8

time.sleep(5)

#servo_j.duty_u16(duty_init)
#time.sleep(t)
my_lcd.standby()
servo_j.duty_u16(duty_standby)
time.sleep(t)
servo_b.duty_u16(duty_unsorted) #init
time.sleep(t)

my_lcd.picking()
servo_j.duty_u16(duty_pickup) #pickup
time.sleep(t)
servo_j.duty_u16(duty_standby)
time.sleep(t)

my_lcd.green()
servo_b.duty_u16(duty_first) #green
time.sleep(t)
servo_j.duty_u16(duty_pickup)
time.sleep(t2)
servo_j.duty_u16(duty_standby)
time.sleep(t)

my_lcd.standby()
servo_b.duty_u16(duty_unsorted) #base
time.sleep(t)
servo_j.duty_u16(duty_pickup)
time.sleep(t)
servo_j.duty_u16(duty_standby)
time.sleep(t)

my_lcd.red()
servo_b.duty_u16(duty_second) #red
time.sleep(t)
servo_j.duty_u16(duty_pickup)
time.sleep(t2)
servo_j.duty_u16(duty_standby)
time.sleep(t)

my_lcd.standby()
servo_b.duty_u16(duty_unsorted) #base
time.sleep(t)
servo_j.duty_u16(duty_pickup)
time.sleep(t)
servo_j.duty_u16(duty_standby)
time.sleep(t)

my_lcd.green()
servo_b.duty_u16(duty_first) #green
time.sleep(t)
servo_j.duty_u16(duty_pickup)
time.sleep(t2)
servo_j.duty_u16(duty_standby)
time.sleep(t)

my_lcd.standby()
servo_b.duty_u16(duty_unsorted) #base
time.sleep(t)
servo_j.duty_u16(duty_pickup)
time.sleep(t)
servo_j.duty_u16(duty_standby)
time.sleep(t)

my_lcd.blue()
servo_b.duty_u16(duty_third) #blue
time.sleep(t)
servo_j.duty_u16(duty_pickup)
time.sleep(t2)
servo_j.duty_u16(duty_standby)
time.sleep(t)

my_lcd.standby()
servo_b.duty_u16(duty_unsorted) #base
time.sleep(t)
servo_j.duty_u16(duty_pickup)
time.sleep(t)
servo_j.duty_u16(duty_standby)
time.sleep(t)

my_lcd.blue()
servo_b.duty_u16(duty_third) #blue
time.sleep(t)
servo_j.duty_u16(duty_pickup)
time.sleep(t2)
servo_j.duty_u16(duty_standby)
time.sleep(t)

my_lcd.standby()
servo_b.duty_u16(duty_unsorted) #base
time.sleep(t)
servo_j.duty_u16(duty_pickup)
time.sleep(t)
servo_j.duty_u16(duty_standby)
time.sleep(t)

my_lcd.red()
servo_b.duty_u16(duty_second) #red
time.sleep(t)
servo_j.duty_u16(duty_pickup)
time.sleep(t2)
servo_j.duty_u16(duty_standby)
time.sleep(t)

my_lcd.standby()
servo_b.duty_u16(duty_unsorted) #fin
time.sleep(t)
servo_j.duty_u16(duty_standby)
time.sleep(t)