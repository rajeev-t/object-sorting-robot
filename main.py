# Dependencies
from machine import Pin, ADC, PWM
import time
import my_lcd

# User Inputs
butt_mass = Pin(6, Pin.IN)
butt_color = Pin(7, Pin.IN)

# Variables
bin_dex = -1  # initialize marker for bin number
MASS_TOL = const(500)  # Tolerance for object mass

# Base servo's angles - correlates to center of unsorted ramp and bins
BASE_POS0 = int((2/80)*65535)
BASE_POS1 = int((6.5/80)*65535)
BASE_POS2 = int((8/80)*65535)
BASE_POS3 = int((9.3/80)*65535)

base = PWM(Pin(3))
base.freq(75)

# Four-bar's angles
PICKUP_POS = int((1/6.7)*65535)
STANDBY_POS = int((1/9)*65535)

crank = PWM(Pin(2))
crank.freq(50)

# current to BJT base or relay, air pump will not be controlled (only powered by rail)
bjt = Pin(8, Pin.OUT)

base_pos = [BASE_POS0, BASE_POS1, BASE_POS2, BASE_POS3]
foba_pos = [PICKUP_POS, STANDBY_POS]

limit = 1 # initializing limit sensor status; functions like push button
mass = 0  # ^
color = 0 # ^

# real-time sorting; bins are not hard-coded
masses = []
colors = []

# Determine mode based on button inputs; parameters are BUTTONS, not button values
def user_choose(mass_in, color_in):
    output_mode = ""
    if mass_in.value() == color_in.value():
        my_lcd.error() # Print error on LCD, don't do anything
        pass
    elif mass_in.value() != 0 and color_in.value() == 0:
        output_mode = "MASS"
    elif mass_in.value() == 0 and color_in.value() != 0:
        output_mode = "COLOR"

    return output_mode
        
# Sort function outputs correct bin_dex
def sort(mode, tol, mass_reading, color_reading):
    bin_dex = -1

    if mode == "MASS":
        if not masses: # list is initially empty; records very first mass and assigns bin to that set of masses
            masses.append(mass_reading)
            bin_dex = masses.index(mass_reading)

        else: # after list is populated with at least 1 mass recording
            for x in masses:
                if abs(x - mass_reading) <= tol: # if under tolerance, object will go to same bin
                    bin_dex = masses.index(x)

            if bin_dex == -1:
                masses.append(mass_reading) # appends only if new mass set is detected
                bin_dex = masses.index(mass_reading)

    elif mode == "COLOR":
        sensor_RGB = [color_reading.red(), color_reading.green(), color_reading.blue()]
        bin_dex = sensor_RGB.index(max(sensor_RGB))

    return bin_dex

# 4-Bar Movements
def engage(pos):
    foba = base.duty_u16(foba_pos[pos])
    return foba

def rotate(bin_num):
    index = bin_num + 1
    rotation = base.duty_u16(base_pos[index])
    return rotation

# Code Function
time.sleep(3) # initial pause to prevent robot from acting before power supply turns on

while True:
    engage(0) # four-bar's standby position
    time.sleep(2)
    rotate(-1) # base's standby/unsorted position
    time.sleep(2)

    my_lcd.input()
    choice = user_choose(butt_mass, butt_color)

    if user_choose != "":
        limit = Pin(9, Pin.IN)
        time.sleep(2)

        if limit == 1:
            mass = ADC(26).read_u16() # pressure pad input
            color = 0 # (yet to setup i2c connection for color sensor; identified library to use)

            bin_dex = sort(choice, MASS_TOL, mass, color)

            engage(1)
            bjt.value(1) # pump activates
            time.sleep(4)

            engage(0) # object picked up
            time.sleep(2)

            rotate(bin_dex)
            time.sleep(2)

            engage(1)
            bjt.value(0) # pump deactivates
            time.sleep(10) # longer delay for suction to diengage

            # Returning to unsorted bin once sorting of one object is completed
            engage(0)
            time.sleep(2)
            rotate(-1)
            time.sleep(2)