#Sam Krimmel
#3/14/18
#rocket1.py - first rocket program

from ggrocket import Rocket, Planet

earth = Planet(viewscale=0.000018)
rocket = Rocket(earth, altitude=2000000, velocity=6900, timezoom=3)
earth.run(rocket)
