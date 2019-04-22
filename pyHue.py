import requests
from os import environ

def main():
  if environ.get('USERNAME') is not None:
    URL = "http://10.0.0.10/api/" + environ['USERNAME'] + "/lights"
      
    # sending get request and saving the response as response object 
    r = requests.get(url = URL) 
      
    # extracting data in json format 
    data = r.json()
    print data
  else:
    print "Enviornmental variable USERNAME must be set. Use export USERNAME='your_username' to run."

if __name__ == "__main__":
    main()