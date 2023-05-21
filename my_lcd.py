import utime

import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x3F
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    

def standby():
    print("Standby Mode")
    lcd.clear()
    lcd.move_to(4,0)
    lcd.putstr("Standby")
    utime.sleep(2)
    lcd.clear()
    
def light():
    print("Light Cube")
    lcd.move_to(4,0)
    lcd.putstr("Light")
    lcd.move_to(4,1)
    lcd.putstr("Cube")
    utime.sleep(2)
    lcd.clear()


def heavy():
    print("Heavy Cube")
    lcd.move_to(4,0)
    lcd.putstr("Heavy")
    lcd.move_to(4,1)
    lcd.putstr("Cube")
    utime.sleep(2)
    lcd.clear()
    
def red():
    lcd.clear()
    print("Red")
    lcd.move_to(4,0)
    lcd.putstr("Red")
    lcd.move_to(4,1)
    lcd.putstr("Cube")
    
def green():
    lcd.clear()
    print("Green")
    lcd.move_to(4,0)
    lcd.putstr("Green")
    lcd.move_to(4,1)
    lcd.putstr("Cube")
    
def blue():
    lcd.clear()
    print("Blue")
    lcd.move_to(4,0)
    lcd.putstr("Blue")
    lcd.move_to(4,1)
    lcd.putstr("Cube")

def error():
    lcd.clear()
    print("Error")
    lcd.move_to(4,0)
    lcd.putstr("Error")

def input():
    lcd.clear()
    lcd.move_to(4,0)
    lcd.putstr("MASS:L")  # indicates left button
    lcd.move_to(4,1)
    lcd.putstr("COLOR:R") # indicates right button

def picking():
    print("Picking up Cube")
    lcd.move_to(4,0)
    lcd.putstr("Picking up")
    lcd.move_to(4,1)
    lcd.putstr("Cube")
    utime.sleep(2)
    lcd.clear()

def testtime():
    standby()
    light()
    heavy()
    picking()
    red()
    utime.sleep(2)
    green()

testtime()