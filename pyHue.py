import requests as req

class Bridge(object):

  def __init__(self, ip, username=None):
    self.ip = ip
    self.url = "http://"+ip+"/api"
    self.username = username

    if self.username is None:
      self.authenticate()

    else:
      print ("Success. New bridge found at " + ip)

  def get_lights(self):
    path = "/lights"
    return self.request('GET', path, None)

  def get_light(self, id):
    path = "/lights/" + str(id)
    return self.request('GET', path, None)

  def set_light(self, id, state):
    path = "/lights/" + str(id) + "/state"
    data = '{"on": ' + state + "}"

    return self.request('PUT', path, data = data)

  def authenticate(self):
    data = '{"devicetype": "pyHue_user"}'
    response = self.request('POST', '', data)

    if 'error' in response[0]:
      description = response[0]['error']['description']
      raise Exception(description)

    elif 'success' in response[0]:
      self.username = response[0]['success']['username']

  def request(self, method, path, data):
    if self.username is not None:
      URL = self.url + self.username + path
    else:
      URL = self.url

    r = req.request(method=method, url=URL, data=data) 
    return r.json();