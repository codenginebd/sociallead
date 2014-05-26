__author__ = 'Codengine'

from Browser import *
from LinkedInMain import *

login_cred_linkedin = {'email':'codenginebd@gmail.com','password':'lapsso065lapsso065'}

class Main:
    def __init__(self):
        pass
    def run(self):
        self.browser = Browser()
        self.linkedin_instance = LinkedIn()
        self.linkedin_instance.Authorize(self.browser,login_cred_linkedin)

Main().run()

