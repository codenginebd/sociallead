__author__ = 'Codengine'

from bs4 import BeautifulSoup
from linkedin import *

class LinkedIn:
    def __init__(self):
        print "Initializing LinkedIn..."
        self.parser = LinkedInParser()
    def get_profile_info(self,profile_link,page):
        linkedin_profile = self.parser.ParseUserProfile(page)
        """ Simplify the linkedin profile. """
        simplified_profile = {}
        simplified_profile['profile_link'] = profile_link
        simplified_profile['full_name'] = linkedin_profile['general_info']['full_name']
        simplified_profile['experiences'] = linkedin_profile['works_and_education']['working_experience']
        return simplified_profile
#f = open('profile_detail_page.htm','r')
#page = f.read()
#print LinkedIn().get_profile_info('',page)