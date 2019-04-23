from pyHue import Bridge
from os import environ

if environ.get('USERNAME') is not None:
  bridge = Bridge(ip='10.0.0.10', username='cblkV1H24kZy6g3VniKRK4-78mx3I4T7dJZHFXVZ')

  # get_lights()
  # get_light(1)
  bridge.set_light(1, "true")

else:
  bridge = Bridge(ip='10.0.0.10')