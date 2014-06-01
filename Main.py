__author__ = 'Codengine'

import math
from bs4 import BeautifulSoup
from Browser import *
from time import sleep

linkedin_login_url = 'https://www.linkedin.com/uas/login?goback=&trk=hb_signin'
linkedin_advance_search_url = 'http://www.linkedin.com/vsearch/p?company=DECOMO&openAdvancedForm=true&companyScope=CP&locationType=Y&rsid=2165730371401558704154&orig=MDYS&pt=people&page_num=4'
login_cred_linkedin = {'email':'codenginebd@gmail.com','password':'lapsso065lapsso065'}
advance_search_link = 'https://www.linkedin.com/vsearch/p?company=__COMPANY_NAME__&openAdvancedForm=true&companyScope=CP&locationType=Y&rsid=2165730371401633387631&orig=ADVS&f_N=F,S,A&openFacets=N,G,CC&page_num=1&pt=people'

class Main:
    def __init__(self):
        pass

    def parse_profile_links(self,page):
        profiles = []
        soup = BeautifulSoup(page)
        result_container_ol_element = soup.find('ol',{'id':'results'})
        result_row_lis = result_container_ol_element.findAll('li')
        for row in result_row_lis:
            h3_elem = row.find('h3')
            anchor_elem = h3_elem.find('a')
            profile_name = anchor_elem.text
            profile_link = anchor_elem['href']
            profiles += [{'name':profile_name,'profile_url':profile_link}]
        return profiles

    def handle_advance_search(self,company_name):
        profiles = []
        _advance_search_link = advance_search_link.replace('__COMPANY_NAME__',company_name)
        self.browser.OpenURL(_advance_search_link)
        page = self.browser.GetPage()
        """ Now parse the page count. """
        soup = BeautifulSoup(page)
        result_count_div = soup.find('div',{'id':'results_count'})
        result_count_elem = result_count_div.find('strong')
        result_count = result_count_elem.text
        if result_count:
            try:
                result_count = int(result_count)
            except Exception,msg:
                result_count = 0
        else:
            result_count = 0
        page_count = math.ceil(float(result_count)/10)
        page_counter = 0
        while True:
            page_counter += 1
            print 'Page counter: %s' % str(page_counter)
            """ Get all results with profile links. """
            page = self.browser.GetPage()
            #f = open('profile_detail_page.htm','w')
            ##f.write(page)
            #f.close()

            profiles += self.parse_profile_links(page)

            if page_counter >= page_count:
                print 'Limit reached! Exiting the while loop.'
                break
            self.browser.scroll_to_pager_link()
            """ Now find the next button on the pager links row. """
            next_element = self.browser.FindElementByText('Next >')
            if next_element:
                self.browser.ClickElement(next_element)
                #sleep(5)
        return profiles

    def run(self):
        self.browser = Browser()
        #self.linkedin_instance = LinkedIn()
        #self.linkedin_instance.Authorize(self.browser,login_cred_linkedin)
        self.browser.OpenURL(linkedin_login_url)
        print 'Logging in to linkedin.'
        emailInputBox = self.browser.FindElementByName("session_key")
        if not emailInputBox:
            print 'Email text box not found!'
            return
        password_input_box = self.browser.FindElementByName('session_password')
        if not password_input_box:
            print 'Password text box not found!'
            return
        signin_button = self.browser.FindElementByName('signin')
        if not signin_button:
            print 'Sign In button not found!'
            return
        emailInputBox.send_keys(login_cred_linkedin['email'])
        password_input_box.send_keys(login_cred_linkedin['password'])
        signin_button.click()
        sleep(4)
        print 'Login successful.'
        """ The crawler will perform search to get all 1st and 2nd degree connections of the current user. """
        #profile_link = 'http://www.linkedin.com/profile/view?id=10978536&authType=OUT_OF_NETWORK&authToken=Y7Ls&locale=en_US&srchid=2165730371401549148728&srchindex=1&srchtotal=52441&trk=vsrp_people_res_name&trkInfo=VSRPsearchId%3A2165730371401549148728%2CVSRPtargetId%3A10978536%2CVSRPcmpt%3Aprimary'
        #self.browser.OpenURL(profile_link)
        #page = self.browser.GetPage()
        #f = open('profile_detail_page.htm','w')
        #f.write(page)
        #f.close()
        print  self.handle_advance_search('Commlink')

Main().run()

