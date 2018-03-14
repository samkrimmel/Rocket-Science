#Sam Krimmel
#3/14/18
#escapeVelocity.py

from ggrocket import Rocket, Planet
from math import radians, sqrt
from ggame import Slider

tz = Slider((10,400), 0, 5, 0, positioning="physical")

Re = 6.371E6
Me = 5.972E24
G = 6.674E-11

earth = Planet(viewscale=0.01)
Ve=sqrt(2*Me*G/Re)
print("Predicted escape velocity is ", Ve, "m/s")
rocket = Rocket(earth, heading=radians(90), directiond=90, velocity=Ve, timezoom=1, timezoom=tz)


earth.run(rocket)
