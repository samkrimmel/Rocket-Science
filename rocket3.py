#Sam Krimmel
#3/15/18
#rocekt3.py

from ggrocket import Rocket, Planet
from math import radians, sqrt, log
from ggmath import InputButton, Timer, Slider

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

vmaxre = Ftotal*tburn/mp*log((me+mp)/me)
print("Predicted final velocity (Rocket Equation), vmax: ", vmaxre, "m/s")

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

def GetMass():
    global RocketStarted
    if RocketStarted:
        return me+mp*(tbrun-BurnTime)/tburn
    else:
        return me+mp
        
tz = Slider((10,300), 0, 5, 0, positioning="physical")

start = InputButton((10,400), "START", StartRocket, positioning="physical", size=15)

rocket = Rocket(earth, thrust=GetThrust, mass=GetMass, timezoom=tz)
earth.run(rocket)
