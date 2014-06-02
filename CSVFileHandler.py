__author__ = 'Codengine'

import unicodecsv

def read_company_list(file_name):
    contents = []
    f = open(file_name,'r')
    lines = f.readlines()
    for index,line in enumerate(lines):
        if index == 0:
            continue
        line_split = line.split(',')
        contents += [
            {
                'full_name':line_split[0],
                'name2':line_split[1],
                'name3':line_split[2],
                'address1':line_split[3],
                'address2':line_split[4],
                'tel':line_split[5],
                'fax':line_split[6],
                'email':line_split[7],
                'web':line_split[8],
                'region':line_split[9]
            }
        ]
    return contents

def write_profiles(company_name,profiles,file_name='output.csv'):
    data_rows = []
    for profile in profiles:
        data_rows += [
            [company_name,profile['name'],profile['profile_url']]
        ]
    with open(file_name, 'a') as fp:
        a = unicodecsv.writer(fp, delimiter=',')
        a.writerows(data_rows)