from math import sin, cos, pi
from pylx16a.lx16a import *
import time
from home import home

LX16A.initialize("/dev/tty.usbserial-10", 0.1)

try:
    servo1 = LX16A(1)
    servo2 = LX16A(2)
    servo3 = LX16A(3)
    servo4 = LX16A(4)
    servo5 = LX16A(5)
    servo6 = LX16A(6)
    servo7 = LX16A(7)
    servo8 = LX16A(8)
    servo1.set_angle_limits(0, 240)
    # servo2.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

    
offsets = [5, -7, -29, 2, -27, -5, 12, 27]

t = 0
while True:
    servo1.move(18*sin(20*t) + 160+offsets[0])
    servo2.move(18*cos(20*t) + 80+offsets[1])
    
    servo7.move(-18*sin(20*t) + 80+offsets[6])
    servo8.move(-18*cos(20*t) + 160+offsets[7])
    
    servo3.move(18*sin(20*t+pi) + 160+offsets[2])
    servo4.move(18*cos(20*t+pi) + 80+offsets[3])
    
    servo5.move(-18*sin(20*t+ pi) + 80+offsets[4])
    servo6.move(-18*cos(20*t+ pi) + 160+offsets[5])

    time.sleep(0.1)
    t += 0.1
    
    