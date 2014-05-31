__author__ = 'Codengine'

from bs4 import BeautifulSoup
from linkedin import *

###https://www.linkedin.com/profile/view?id=36379560&authType=NAME_SEARCH&authToken=Xu6Q&trk=api*a231405*s2393+07*
###https://www.linkedin.com/profile?viewProfile=&key=36379560&authToken=Xu6Q&authType=NAME_SEARCH&trk=api*a231405*s239307*
###Andrews Profile: https://www.linkedin.com/profile/view?id=12285308&authType=NAME_SEARCH&authToken=Xu6Q&trk=api*a231405*s2393+07*
### Another profile ID: 453613
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