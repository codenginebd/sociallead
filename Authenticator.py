__author__ = 'Codengine'

from time import sleep

linkedin_login_url = 'https://www.linkedin.com/uas/login?goback=&trk=hb_signin'

class Authenticator(object):
    def __init__(self):
        print 'Authenticator Initialized...'

    def hanlde_login(self,browser):
        f = open('login_cred.json','r')
        d = f.read()
        f.close()

        import json

        data = json.loads(d)

        self.login_cred_linkedin = data

        browser.OpenURL(linkedin_login_url)
        emailInputBox = browser.FindElementByName("session_key")
        if not emailInputBox:
            print 'Email text box not found!'
            return
        password_input_box = browser.FindElementByName('session_password')
        if not password_input_box:
            print 'Password text box not found!'
            return
        signin_button = browser.FindElementByName('signin')
        if not signin_button:
            print 'Sign In button not found!'
            return
        emailInputBox.send_keys(self.login_cred_linkedin['email'])
        password_input_box.send_keys(self.login_cred_linkedin['password'])
        signin_button.click()
        sleep(4)
