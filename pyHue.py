import requests
from os import environ

def get_lights():
  newURL = URL + environ['USERNAME'] + "/lights"
  print get(newURL)

def get_light(id):
  newURL = URL + environ['USERNAME'] + "/lights/" + str(id)
  print get(newURL)

def set_light(id, state):
  newURL = URL + environ['USERNAME'] + "/lights/" + str(id) + "/state"
  data = '{"on": ' + state + "}"

  r = requests.put(newURL, data = data) 
    
  response = r.text 
  print response

def get(URL):
  r = requests.get(url = URL) 
  return r.json();

def main():
  if environ.get('USERNAME') is not None:
    # get_lights()
    # get_light(1)
    set_light(1, "true")

  else:
    print "Enviornmental variable USERNAME must be set. Use export USERNAME='your_username' to run."

URL = "http://10.0.0.10/api/"

if __name__ == "__main__":
    main()