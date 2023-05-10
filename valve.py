from machine import Pin
import time

valve = Pin(13, Pin.OUT)

valve.high()