__author__ = 'Codengine'

import unicodecsv

def read_company_list(file_name):
    contents = []
    f = open(file_name,'r')
    lines = f.readlines()
    f.close()
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

def read_basic_profiles(file_name='basic_profiles.csv'):
    contents = []
    f = open(file_name,'r')
    lines = f.readlines()
    f.close()
    for index,line in enumerate(lines):
        data_array = line.split(',')
        company_name = data_array[0]
        profile_name = data_array[1]
        profile_link = data_array[2]
        contents += [{'company_name':company_name,'profile_name':profile_name,'profile_url':profile_link}]
    return contents


def write_basic_profiles(company_name,profiles,file_name='basic_profiles.csv'):
    data_rows = []
    for profile in profiles:
        data_rows += [
            [company_name,profile['name'],profile['profile_url']]
        ]
    with open(file_name, 'a') as fp:
        a = unicodecsv.writer(fp, delimiter=',')
        a.writerows(data_rows)

def write_full_profile(profile,file_name='full_profiles.csv'):
    row = []
    row += [profile['target_company_name']]
    row += [profile['full_name']]
    row += [profile['current_company']]
    row += [profile['title']]
    #row += [profile['company_duration'].replace('&#8211;','-')]
    row += [profile['profile_link']]

    temp2 = []
    for company in profile['past_companies']:
        temp = []
        for key,value in company.items():
            temp += [key+':'+value.replace('&#8211;','-')]
        temp2 += [';'.join(temp)]
    row += ['|'.join(temp2)]

    with open(file_name,'a') as ap:
        a = unicodecsv.writer(ap,delimiter=',')
        a.writerow(row)
    print 'Written into the file.'