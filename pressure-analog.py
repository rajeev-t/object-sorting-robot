from machine import Pin, ADC
import time

adc = ADC(Pin(26))

while True:
    print(adc.read_u16())
    time.sleep(2)