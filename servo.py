# servo.py
# By Adam Kraft
# meant for use with a raspberry pi to control a servo
import RPi.GPIO as GPIO
import time

# Specify some global variables
sPins = [17] #default pins

# setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(sPins[0], GPIO.OUT)

class Servo:
    '''
    1ms pulse for 0 degree (LEFT)
    1.5ms pulse for 90 degree (MIDDLE)
    2ms pulse for 180 degree (RIGHT)

    duty cycle for 0 degree = (1/20)*100 = 5%
    duty cycle for 90 degree = (1.5/20)*100 = 7.5%
    duty cycle for 180 degree = (2/20)*100 = 10%
    '''
    def __init__(self,pins=sPins):
        self.pins = pins
        self.start()
        self.angle = 90 #90 for neutral, 180 for right, 0 for left
        self.pos = 'mid'

    def start(self):
        self.p = GPIO.PWM(self.pins[0], 50) # GPIO 17 for PWM with 50Hz
        p.start(2.5)
        time.sleep(3)

    def d2p(self,angle):
        '''gets an angle between 0 and 180 and returns a duty cycle'''
        # 1ms -> 2ms
        # 0 degree -> 180 degree
        assert angle<=180 and angle>=0
        ms = 1 + (angle/180)
        return (ms/20)*100

    def rotate(self,angle,speed=10,sleep_time=0.01):
        '''rotates the servo to the given angle'''
        da = angle - self.angle
        if da == 0:
            pass
        else:
            step = 1 if da>0 else -1
            step *= speed
            for i in range(self.angle,angle,step):
                self.p.ChangeDutyCycle(i)
                time.sleep(sleep_time)
            self.angle = angle
            time.sleep(1)

    def reset(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(sPins[0], GPIO.OUT)
        self.start()

    def move_middle(self):
        if self.pos == 'mid':
            pass
        else:
            self.p.ChangeDutyCycle(7.5)
            self.angle = 90 # degrees
            self.pos = 'mid'
        time.sleep(0.5)

    def move_left(self):
        if self.pos == 'left':
            pass
        else:
            self.p.ChangeDutyCycle(5)
            self.angle = 0 # degrees
            self.pos = 'left'
        time.sleep(0.5)

    def move_right(self):
        if self.pos == 'right':
            pass
        else:
            self.p.ChangeDutyCycle(10)
            self.angle = 180 # degrees
            self.pos = 'right'
        time.sleep(0.5)

# --------------------- Test Functions -----------------------------------------

def stest():
    p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
    p.start(2.5) # Initialization
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    p.stop()
    GPIO.cleanup()

def test2():
    s = Servo()
    s.move_left()
    s.move_right()
    s.move_middle()
    s.reset()
    s.rotate(45)
    s.rotate(135)

if __name__ == '__main__':
    stest()
    time.sleep(2)
    test2()
