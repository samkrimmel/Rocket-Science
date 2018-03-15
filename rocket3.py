#Sam Krimmel
#3/15/18
#rocekt3.py

from ggrocket import Rocket, Planet
from math import radians, sqrt, log
from ggmath import InputButton, Timer

earth = Planet(planetmass=0) 

RocketStarted = False
StartTime = None
BurnTime = 0

me = 25600
mp = 395700
F1D = 716000
N1D = 9

Ftotal = F1D*N1D
tburn = 180

vmax = Ftotal*tburn/(me+mp)
print("predicted final velocity (Newton's 2nd Law), vmax: ", vmax, "m/s")

def GetThrust():
    global BurnTime
    global RocketStarted
    if RocketStarted:
        BurnTime = rocket.shiptime - StartTime
        if BurnTime >= tburn:
            RocketStarted = False
            return 0
        else:
            return Ftotal
    else:
        return 0

def StartRocket():
    global RocketStarted
    global StartTime
    if not RocketStarted:
        RocketStarted = True
        StartTime = rocket.shiptime

tz = Slider((10,400), 0, 5, 0, positioning="physical")

start = InputButton((10,400), "START", StartRocket, positioning="physical", size=15)

rocket = Rocket(earth, thrust=GetThrust, mass=mp+me)
earth.run(rocket)
