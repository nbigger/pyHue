import requests as req

class Bridge(object):

  def __init__(self, ip, username):
    self.ip = ip
    self.url = "http://"+ip+"/api/"+username
    print ("new bridge at ip " + ip)

  def get_lights(self):
    path = "/lights"
    return self.request('GET', path, None)

  def get_light(self, id):
    path = environ['USERNAME'] + "/lights/" + str(id)
    return self.request('GET', path, None)

  def set_light(self, id, state):
    path = "/lights/" + str(id) + "/state"
    data = '{"on": ' + state + "}"

    return self.request('PUT', path, data = data) 
      
    # response = r.text 
    # return response

  def request(self, method, path, data):
    URL = self.url + path
    r = req.request(method=method, url=URL, data=data) 
    return r.json();