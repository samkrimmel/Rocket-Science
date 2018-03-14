#Sam Krimmel
#3/14/18
#rocket1.py - first rocket program

from ggrocket import Rocket, Planet

earth = Planet(color=(0x9aa2af), radius=1737400, planetmass=73480000000000000000000, viewscale=0.000018)
rocket = Rocket(earth, altitude=100000, velocity=1632, timezoom=3)
earth.run(rocket)
