# Dependencies
from machine import Pin, ADC, PWM
import time

# IR Sensor Pinouts - Detect height @ which robot can drop an object
ir0 = Pin(3, Pin.IN)
ir1 = Pin(4, Pin.IN)
ir2 = Pin(5, Pin.IN)

# User Inputs
butt_mass = Pin(6, Pin.IN)
butt_color = Pin(7, Pin.IN)

# Variables
bin_dex = -1  # initialize marker for bin number
MASS_TOL = const(100)  # Tolerance for object mass; will change

# Base servo's angles - correlates to center of unsorted ramp and bins
BASE_POS0 = const(1500)
BASE_POS1 = const(2500)
BASE_POS2 = const(4500)
BASE_POS3 = const(6500)

base = PWM(Pin(14))
base.freq(50)

# Four-bar's angles
PICKUP_POS = const(0)
ROTATE_POS = const(180)

crank = PWM(Pin(15))
crank.freq(50)

# current to BJT base or relay, air pump will not be controlled (only powered by rail)
valve = Pin(0, Pin.OUT)

ir_list = [ir0, ir1, ir2]

base_pos = [BASE_POS0, BASE_POS1, BASE_POS2, BASE_POS3]
foba_pos = [PICKUP_POS, ROTATE_POS]

limit = 1  # initializing limit sensor status; functions like push button
mass = 0  # ^
color = 0 # ^


# real-time sorting; bins are not hard-coded
masses = []
colors = []

user_input = 0 # still needs to be programmed - IR remote
time_ref = time.ticks_ms()
# User Input Functions
# Determine mode based on button inputs; parameters are BUTTONS, not button values
def user_choose(mass_in, color_in):
    output_mode = ""
    if mass_in.value() == color_in.value():
        # Print error on LCD, don't do anything
        pass
    
    elif mass_in.value() == 0 and color_in.value() != 0:
        output_mode = "MASS"
    # Color Sort
    elif mass_in.value() != 0 and color_in.value() == 0:
        output_mode = "COLOR"
    time_ref = time.ticks_ms()
    return output_mode
    
# LCD Functions
        
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

    # print(bin_dex)
    return bin_dex

# 4-Bar Movements

def engage(bin_num): # in progress
    if bin_num != -1:
        pass
    else:
        pass
    return False

def rotate(bin_num):
    index = bin_num + 1
    rotation = crank.duty_u16(base_pos[index])
    return rotation


while True:
    if limit == 1:
        mass = ADC(26).read_u16() # pressure pad input
        color = 0 # (yet to setup i2c connection for color sensor; identified library to use)

        sort(user_input, MASS_TOL, mass, color)
        rotate(-1)
    

        # incomplete
