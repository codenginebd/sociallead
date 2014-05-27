__author__ = 'Codengine'

from Browser import *
from linkedin import *

login_cred_linkedin = {'email':'codenginebd@gmail.com','password':'lapsso065lapsso065'}

class Main:
    def __init__(self):
        pass
    def run(self):
        self.lioauth = LIOauth()
        self.lioauth.get_access_token()

Main().run()

#https://www.linkedin.com/uas/oauth2/authorization?response_type=code&client_id=75zsaemfpnjp6v&scope=r_network&state=STATE &redirect_uri=http://codenginebd.appspot.com
#AQTVuOJLirb2v0rwkSSy8AomTUT_mdrNRpQXaxO31e8n7XB19RivE1k3Q7Q2546XaXFGY6Uxf3wh4SZeLcRK4Dwh6HjxAdDwCZ5cFlYeFApyzt5fc9o&state=STATE+

#https://www.linkedin.com/uas/oauth2/accessToken?grant_type=authorization_code&code=AQTVuOJLirb2v0rwkSSy8AomTUT_mdrNRpQXaxO31e8n7XB19RivE1k3Q7Q2546XaXFGY6Uxf3wh4SZeLcRK4Dwh6HjxAdDwCZ5cFlYeFApyzt5fc9o&redirect_uri=http://codenginebd.appspot.com/&client_id=75zsaemfpnjp6v&client_secret=S4u1DCShnHk4se4f

