# - * - coding: UTF-8 - * -

import time

from selenium import webdriver


class Browser:
    # def __init__(self):
        # try:
        	# self.browser = webdriver.Firefox() #self.browser = webdriver.PhantomJS("./phantomjs") #self.browser = webdriver.Firefox()
        	# self.browser.set_page_load_timeout(60)
        # except Exception,exp:
            # print "Webdriver open failed."

    def __init__(self,proxy_ip=None):
        try:
             if proxy_ip:
                service_args = ['--proxy=%s' % proxy_ip,'--proxy-type=http',]
                print service_args
                self.browser = webdriver.PhantomJS("./phantomjs")  #self.browser = webdriver.PhantomJS("./phantomjs",service_args=service_args) #self.browser = webdriver.Firefox()
                #proxy = Proxy({'proxyType': ProxyType.MANUAL,'httpProxy': proxy_ip})
                #self.browser = webdriver.Firefox()
                #self.browser = webdriver.Chrome()
             else:
                self.browser = webdriver.PhantomJS("./phantomjs")
            #self.browser = webdriver.PhantomJS("./phantomjs")
             self.browser.set_page_load_timeout(60)
             self.browser.set_script_timeout(60)
        except Exception,exp:
        	print "Webdriver open failed."

    def OpenURL(self,url):
        try:
            self.browser.get(url)
            return True
        except Exception,exp:
            return False


    def GetPage(self):
        try:
            self.page = self.browser.page_source
            encodedStr = self.page.encode("ascii","xmlcharrefreplace")
            return encodedStr
        except Exception,exp:
            return None
    def ClickElement(self,element):
        try:
            if element is not None:
                try:
                    element.click()
                    time.sleep(10)
                    return True
                except Exception,e:
                    print "Click Exception: "+str(e)
                    return False
        except Exception,exp:
            return False

    def TypeInto(self,text,element):
        try:
            element.send_keys(text)
        except Exception,msg:
            pass

    def ClearText(self,element):
        try:
            element.clear()
        except Exception,msg:
            print 'Text Clear Failed!'
            pass

    def FindElementByName(self,elementName):
        try:
            element = self.browser.find_element_by_name(elementName)
            return element
        except Exception,exp:
            return None

    def FindElementById(self,elementId):
        try:
            element = self.browser.find_element_by_id(elementId)
            return element
        except Exception,exp:
            return None

    def FindElementByClassName(self,elementClassName):
        try:
            element = self.browser.find_element_by_css_selector(elementClassName)
            return element
        except Exception,exp:
            return None

    def FindElementByText(self,text):
        try:
            element = self.browser.find_element_by_link_text(text)
            return element
        except Exception,msg:
            return None

    def ExecuteScriptAndWait(self,code):
        try:
            self.browser.execute_script(code)
            time.sleep(7)
        except Exception,exp:
            pass

    def GetPageURL(self):
        try:
            return self.browser.current_url
        except Exception,exp:
            return None

    def Close(self):
        try:
            self.browser.close()
        except Exception,exp:
            print "Browser closing failed."

    def scroll_to_pager_link(self):
        try:
            scrollto_pager_link = 'var el = document.getElementById("Y-N-ffs");el.scrollIntoView(true);'
            #scrollto_pager_link = 'var el = document.getElementsByClassName("pagination");el[0].scrollIntoView(true);'
            self.ExecuteScriptAndWait(scrollto_pager_link)
        except Exception,exp:
            print "Exception Inside page scroll. %s" % str(exp)






