__author__ = 'Codengine'

from PeopleSearchHanlder import *
from PeopleDetailsHanlder import *
from DBHandler import *

class Main:
    def __init__(self):
        self.people_search_handler = PeopleSearchHandler()
        self.people_details_handler = PeopleDetailsHanlder()

    def reset(self):
        f = open('basic_profiles.csv','w')
        f.write('')
        f.close()

        f = open('full_profiles.csv','w')
        f.write('')
        f.close()

        db = DBHandler()
        db.drop_tables()
        db.close()

    def fresh_run(self):
        self.people_search_handler.run()
        self.people_details_handler.handle()

    def run_entry(self):
        while True:
            option = raw_input('Options: -r for reset the whole program \n -s start or resume the program\n -q to quit the program.\n\n')
            if option == '-r':
                self.reset()
                print 'Reset done!'
            elif option == '-s':
                self.fresh_run()
                print 'The program is done!'
                print 'The program is exiting now...'
                break
            elif option == '-q':
                print 'The program is exiting now...'
                break
            else:
                print 'Invalid option!'

Main().run_entry()