__author__ = 'Codengine'

import math
from random import randint
from time import sleep

from bs4 import BeautifulSoup
from Browser import *
import CSVFileHandler
from Authenticator import *
from DBHandler import *


linkedin_login_url = 'https://www.linkedin.com/uas/login?goback=&trk=hb_signin'
linkedin_advance_search_url = 'http://www.linkedin.com/vsearch/p?company=DECOMO&openAdvancedForm=true&companyScope=CP&locationType=Y&rsid=2165730371401558704154&orig=MDYS&pt=people&page_num=4'
login_cred_linkedin = {'email':'codenginebd@gmail.com','password':'lapsso065lapsso065'}
advance_search_link = 'https://www.linkedin.com/vsearch/p?company=__COMPANY_NAME__&openAdvancedForm=true&companyScope=CP&locationType=Y&rsid=2165730371401633387631&orig=ADVS&f_N=F,S&openFacets=N,G,CC&page_num=1&pt=people'

class PeopleSearchHandler(Authenticator):
    def __init__(self):
        self.db = DBHandler()

    def parse_profile_links(self,page):
        profiles = []
        soup = BeautifulSoup(page)
        result_container_ol_element = soup.find('ol',{'id':'results'})
        if result_container_ol_element:
            result_row_lis = result_container_ol_element.findAll('li',{'class':'mod'})
            if result_row_lis:
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
        super(PeopleSearchHandler,self).hanlde_login(self.browser)
        """ The crawler will perform search to get all 1st and 2nd degree connections of the current user. """
        #print  self.handle_advance_search('Commlink')
        company_list = CSVFileHandler.read_company_list('Linkedin_contacts_for_crawling_v001.csv')
        last_search_index = self.db.get_last_searched_company_index()

        print 'Last searched company index %s' % str(last_search_index)

        company_list = company_list[last_search_index:]
        for index,company in enumerate(company_list):
            company_name = company['full_name']
            search_result = self.handle_advance_search(company_name)
            if search_result:
                CSVFileHandler.write_basic_profiles(company_name,search_result)
            self.db.update_last_searched_company(index+last_search_index+1)
            time_to_sleep = randint(3,10)
            print 'Sleeping %s seconds.' % (str(time_to_sleep))
            sleep(time_to_sleep)
        self.browser.Close()



