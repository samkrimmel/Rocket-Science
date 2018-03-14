#Sam Krimmel
#3/14/18
#rocket1.py - first rocket program

from ggrocket import Rocket, Planet

earth = Planet()
rocket = Rocket(earth, altitude=50)
earth.run(rocket)
