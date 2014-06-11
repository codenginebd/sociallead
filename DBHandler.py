#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Codengine'

class DBHandler:
    def __init__(self):
        pass

    def update_last_searched_company(self,company_index,company_name=None):
        f = open('current_state.json','r')
        data = f.read()
        f.close()
        import json
        data = json.loads(data)
        data['last_searched_company_index'] = company_index
        data = json.dumps(data)
        with open('current_state.json','w') as f:
            f.write(data)

    def delete_all_data(self):
        data = '{"last_searched_company_index":0,"last_crawled_profile_index":0}'
        with open('current_state.json','w') as f:
            f.write(data)

    def get_last_searched_company_index(self):
        f = open('current_state.json','r')
        data = f.read()
        f.close()
        import json
        data = json.loads(data)
        return data['last_searched_company_index']

    def update_last_crawled_profile_index(self,index,company_name=None):
        f = open('current_state.json','r')
        data = f.read()
        f.close()
        import json
        data = json.loads(data)
        data['last_crawled_profile_index'] = index
        data = json.dumps(data)
        with open('current_state.json','w') as f:
            f.write(data)

    def get_last_crawled_profile_index(self):
        f = open('current_state.json','r')
        data = f.read()
        f.close()
        import json
        data = json.loads(data)
        return data['last_crawled_profile_index']

    def close(self):
        #if self.connection:
        #    self.connection.close()
        pass

#db = DBHandler()
#query = "delete from full_profile_index;"
#db.execute_query(query)
#db.update_last_searched_company(2,'Company')
#print db.get_last_searched_company_index()[0][0]

