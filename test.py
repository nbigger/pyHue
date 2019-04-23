from pyHue import Bridge
from os import environ

if environ.get('USERNAME') is not None:
  bridge = Bridge(ip='10.0.0.10', username=environ['USERNAME'])

  # get_lights()
  # get_light(1)
  bridge.set_light(1, "true")

else:
  print ("Enviornmental variable USERNAME must be set. Use export USERNAME='your_username' to run.")