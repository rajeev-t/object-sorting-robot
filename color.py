# More details can be found in TechToTinker.blogspot.com 
# George Bantique | tech.to.tinker@gmail.com

from machine import Pin
from machine import I2C
from tcs34725 import TCS34725
from time import sleep_ms

I2C_FREQ = const(400000)
#i2c_bus = I2C(1, sda=Pin(18, Pin.PULL_UP), scl=Pin(19, Pin.PULL_UP), freq=I2C_FREQ)
i2c_bus = I2C(0, sda=Pin(0), scl=Pin(1), freq=I2C_FREQ)

# print(i2c_bus.scan())

tcs = TCS34725(i2c_bus)

# # The following lines of code should be tested in the REPL:
# #
# # 1. To print the raw data:
# print('raw: {}'.format(tcs.read('raw')))
# #
# # 2. To print the RGB data:
# print('rgb: {}'.format(tcs.read('rgb')))
# #
# # 3. To print the RGB data in decimal form:
# print('dec: {}'.format(tcs.read('dec')))
# #
# # 4. To print the RGB data in hex form:
# print('hex: {}'.format(tcs.read('hex')))
# #
# # 5. To print the color temperature in ^Kelvin and
# #    the luminosity in lux
# print('lux: {}'.format(tcs.read('lux')))