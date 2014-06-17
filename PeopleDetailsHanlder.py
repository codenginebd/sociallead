__author__ = 'Codengine'

from time import sleep
from random import randint

from Browser import *
from linkedin import LinkedInParser
import CSVFileHandler
from Authenticator import *
from DBHandler import *

class PeopleDetailsHanlder(Authenticator):
    def __init__(self,file_name='output.csv'):
        #print 'Initializing People Details Handler...'
        self.db = DBHandler()

    def handle(self):
        self.browser = Browser()
        self.parser = LinkedInParser()
        self.basic_profiles = CSVFileHandler.read_basic_profiles()
        super(PeopleDetailsHanlder,self).hanlde_login(self.browser)

        last_crawled_profile = self.db.get_last_crawled_profile_index()

        print 'Last crawled profile index %s' % str(last_crawled_profile)

        self.basic_profiles = self.basic_profiles[last_crawled_profile:]

        for i,basic_profile in enumerate(self.basic_profiles):
            profile_link = basic_profile['profile_url']
            self.browser.OpenURL(profile_link)
            page = self.browser.GetPage()
            profile = self.parser.ParseUserProfile(page)
            modified_profile = {
                'target_company_name':'',
                'full_name':'',
                'current_company':'',
                'company_duration':'',
                'title':'',
                'past_companies':[],
                'profile_link':''
            }
            if profile:
                modified_profile['full_name'] = profile['general_info']['full_name'] if profile['general_info'].get('full_name') else ''
                modified_profile['title'] = profile['general_info']['heading'] if profile['general_info'].get('heading') else ''
                modified_profile['target_company_name'] = basic_profile['company_name']
                modified_profile['profile_link'] = basic_profile['profile_url']

                #past_companies = profile['general_info']['past_company'] if profile['general_info'].get('past_company') else ''

                working_experiences = profile['works_and_education']['working_experience']

                past_experiences = []
                #current_company = ''
                current_companies = []

                for index,each_experience in enumerate(working_experiences):
                    duration = each_experience.get('time')
                    if not 'Present' in duration:
                        past_experiences += [each_experience]
                    else:
                        #current_company = each_experience
                        current_companies += [each_experience]

                #if current_company:
                #    modified_profile['current_company'] = current_company.get('company_name') if current_company.get('company_name') else ''
                #    modified_profile['title'] = current_company.get('title') if current_company.get('title') else ''
                #    modified_profile['company_duration'] = current_company.get('time') if current_company.get('time') else ''
                temp_companies = []
                if current_companies:
                    for j,company in enumerate(current_companies):
                        company_info = ''
                        company_info += company.get('company_name') if company.get('company_name') else ''
                        company_info += ';'
                        company_info += company.get('title') if company.get('title') else ''
                        company_info += ';'
                        company_info += company.get('time').replace('&#8211;','-') if company.get('time') else ''
                        temp_companies += [company_info]

                modified_profile['current_company'] = '|'.join(temp_companies)

                modified_profile['past_companies'] = past_experiences

                CSVFileHandler.write_full_profile(modified_profile)

            self.db.update_last_crawled_profile_index(i+last_crawled_profile+1)

            time_to_sleep = randint(5,25)
            print 'Sleeping %s seconds.' % str(time_to_sleep)
            sleep(time_to_sleep)

        self.browser.Close()

#PeopleDetailsHanlder().handle()

