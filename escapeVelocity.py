#Sam Krimmel
#3/14/18
#escapeVelocity.py

from ggrocket import Rocket, Planet
from math import radians, sqrt

Re = 6.371E6
Me = 5.972E24
G = 6.674E-11

Ve=sqrt(2*Me*G/Re)
print("Predicted escape velocity is ", Ve, "m/s")

earth = Planet(viewscale=0.01)
rocket = Rocket(earth, heading=radians(90), directiond=90, velocity=Ve, timezoom=2)
earth.run(rocket)
