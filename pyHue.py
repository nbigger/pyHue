import requests
from os import environ

def get_lights():
  newURL = URL + environ['USERNAME'] + "/lights"
  print get(newURL)

def get_light(Id):
  newURL = URL + environ['USERNAME'] + "/lights/" + str(Id)
  print get(newURL)

def get(URL):
  r = requests.get(url = URL) 
  return r.json();

def main():
  if environ.get('USERNAME') is not None:
    # get_lights()
    get_light(1)

  else:
    print "Enviornmental variable USERNAME must be set. Use export USERNAME='your_username' to run."

URL = "http://10.0.0.10/api/"

if __name__ == "__main__":
    main()