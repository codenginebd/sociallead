
import urllib2
import json
import GlobalConstants
from Browser import *

class LIOauth:
    def __init__(self):
        self.app_key = GlobalConstants.app_key
        self.app_secret = GlobalConstants.app_secret
        self.browser = Browser()
    def get_access_token(self):
        self.browser.OpenURL(GlobalConstants.authorization_url)
        allowAccessButton = self.browser.FindElementByName("authorize")

        if not allowAccessButton:
            print 'Access button not found! There was an error. Please close the app and start again.'
            return
        emailInputBox = self.browser.FindElementByName("session_key")
        emailInputBox.send_keys(GlobalConstants.login_email)
        passwordInputBox = self.browser.FindElementByName("session_password")
        passwordInputBox.send_keys(GlobalConstants.login_password)
        allowAccessButton.click()
        page_url = self.browser.GetPageURL()
        print 'Page URL: %s' % page_url
        """ Now parse the page url. """
        #http://codenginebd.appspot.com/?code=AQSUeY-dXUmEoYT7Vu5Rl6sZ0lnDRMKnZxBnj_fntzEZfGv50vhx-LIDScdIIn9kIOQy_2HkPG2inTHM0_hXgI94jfWMFniI762_HziS-i_jL_baSio&state=STATE
        temp = page_url[page_url.index('code=')+5:]
        auth_code = temp[:temp.index('&state')]
        """ Now we got the oauth code. Request to get the access token. First form the access token url. """
        GlobalConstants.access_token_url = GlobalConstants.access_token_url.replace('__CODE__',auth_code)
        print 'Now the access token url is:'
        print GlobalConstants.access_token_url
        request = urllib2.Request(GlobalConstants.access_token_url)
        request.get_method = lambda: 'POST'
        http_obj = urllib2.urlopen(request)
        page = http_obj.read()
        print page
        """ Now we got the json response. Need to parse the access token from the page content. """
        json_data = json.loads(page)
        access_token = json_data.get('access_token')
        if access_token:
            people_search_url = GlobalConstants.people_search_url.replace('__COMPANY_NAME__','Commlink').replace('__OAUTH2_ACCESS_TOKEN_URL__',access_token)
            self.browser.OpenURL(people_search_url)

