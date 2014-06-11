sociallead
==========

The purpose of this project is to find all people's who either working in a particular company or worked in the past. We have a list of company with some additional info. Now for each company we need to find the people's under that company who have worked or are working now. The final output will be full_profiles.csv file. 

The program has two part basically:
In the first part it uses advance search to find people under a company. So now we have a list of people with their profile links. The list is now saved in basic_profiles.csv file.

Technical
=========

We used Python2.7.6,sqlite database,selenium module,phantomjs/chromedriver, BeautifulSoup, regex, unicodecsv module.

Main.py is the main entry file.

The sqlite database is used to keep track where the program is now on the list so that it can resume later if some failure occur.

Installation Instructions
=========================
First install python2.7.6 either 32/64 bit depending on your pc. Then install all required modules are bundled with the program. So only python need to be installed and it's path need to be set up on the environment variable's path.


How to use
===========
cd to the project directory in cmd. Run the command python Main.py.

Now the program will give a menu. Please input an option. 

-r for reset. -s for start, -q for exit the program.
