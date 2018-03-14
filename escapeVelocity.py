#Sam Krimmel
#3/14/18
#escapeVelocity.py

from ggrocket import Rocket, Planet
from math import radians, sqrt
from ggmath import Slider

earth = Planet(viewscale=0.01)

Re = 1.7374E6
Me = 7.35E22
G = 6.674E-11

Ve=sqrt(2*Me*G/Re)
print("Predicted escape velocity is ", Ve, "m/s")

tz = Slider((10,400), 0, 5, 0, positioning="physical")
rocket = Rocket(earth, heading=radians(90), directiond=90, velocity=Ve, timezoom=tz)


earth.run(rocket)
