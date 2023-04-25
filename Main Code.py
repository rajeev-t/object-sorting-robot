# Import Statements
from machine import Pin, ADC
import time

# Sensor Pinouts
ir0 = Pin(3, Pin.IN)
ir1 = Pin(4, Pin.IN)
ir2= Pin(5, Pin.IN)

# Variables
bin_dex = 0
MASS_TOL = const(100)
SERVO_POT0 = const(50)
SERVO_POT1 = const(100)
SERVO_POT2 = const(160)
FORWARD_POT = const(0)
BACKWARD_POT = const(180)

ir_list = [ir0, ir1, ir2]
bin_pots = [SERVO_POT0, SERVO_POT1, SERVO_POT2]
four_bar_pots = [FORWARD_POT, BACKWARD_POT]
recorded_masses = []
# Functions


# Sort function outputs bin_dex
# Remove mass_reading parameter for programming
def sort(mode, tol, mass_reading):
    output_index = -1
    if mode == "MASS":
        if not recorded_masses:
            recorded_masses.append(mass_reading)
            output_index = recorded_masses.index(mass_reading)
        else:
            for x in recorded_masses:
                if abs(x - mass_reading) <= tol:
                    output_index = recorded_masses.index(x)
            if output_index == -1:
                recorded_masses.append(mass_reading)
                output_index = recorded_masses.index(mass_reading)
    elif mode == "COLOR":
        # FIRST MOVE BLOCK TO COLOR SENSOR POSITION (if color sensor isn't mounted on ramp)
        sensor_RGB = [sensor.red(), sensor.green(), sensor.blue()]
        output_index = sensor_RGB.index(max(sensor_RGB))
    #print(output_index)
    return output_index
# 4-Bar Movements
def retract():
    # 
    return False
def move_to_bin(index):
    #
    return False
# Move servo to original position & shut power off to unnecessary components
def reset():
    return False
sort("MASS", MASS_TOL, 100)
sort("MASS", MASS_TOL, 1000)
sort("MASS", MASS_TOL, 120)
sort("MASS", MASS_TOL, 900)
print(recorded_masses)
reset()
#while True:
    


   