#Sam Krimmel
#3/14/18
#rocket1.py - first rocket program

from ggrocket import Rocket, Planet
from ggame import *

data = {}
data['thrust']=0

def thrust():
    return data['thrust']


earth = Planet(color=(0x9aa2af), radius=1737400, planetmass=73480000000000000000000, viewscale=0.00002)
rocket = Rocket(earth, altitude=0, velocity=0, timezoom=0.5, thrust = thrust)

def upThrust(event):
    data['thrust']+=0.2
    
def downThrust(event):
    data['thrust']-=0.2

App.listenKeyEvent('keydown', 'w', upThrust)
App.listenKeyEvent('keydown', 's', downThrust)

earth.run(rocket)