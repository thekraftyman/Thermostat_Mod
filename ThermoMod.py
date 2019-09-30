# ThermoMod.py
# The main program for the thermostat modification for the dorm
# By: Adam Kraft
from servo import *
from thermometer import *
import time
'''
To be used in conjunction with the DS18B20 Digital temperature sensor and the
Tower Pro SG90 servo

Pins used:
    Servo:
        17 for PWM
        a 5v pin
        a ground pin

Tutorials:
    http://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/
    https://pimylifeup.com/raspberry-pi-temperature-sensor/
    https://www.electronicshub.org/raspberry-pi-servo-motor-interface-tutorial/
'''

# Specify Global Variables
temps = [70,75]
# -----------------------------------------------------------------------------
# Setup:
trange = range(temps[0],temps[1]+1)
servo = Servo()
# -----------------------------------------------------------------------------
# Define some functions
def hotter():
    # servo.move_left() # when turning left turns the unit on
    servo.move_right() # when turning right turns the unit on

def colder():
    # servo.move_right() # when turning right turns the unit on
    servo.move_left() # when turning left turns the unit on

def neutral():
    servo.move_middle()

if __name__ == '__main__':
    while True:
        temp = get_temp()
        if temp in trange:
            neutral()
        elif temp<trange[0]:
            colder()
        else:
            hotter()
        time.sleep(60)
