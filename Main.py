__author__ = 'Codengine'

from PeopleSearchHanlder import *
from PeopleDetailsHanlder import *

class Main:
    def __init__(self):
        self.people_search_handler = PeopleSearchHandler()
        self.people_details_handler = PeopleDetailsHanlder()

    def run(self):
        self.people_search_handler.run()
        self.people_details_handler.handle()

Main().run()