#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Codengine'

import sqlite3
import sys

class DBHandler:
    def __init__(self):
        try:
            self.connection = sqlite3.connect('sqlite.db')
            #print 'Creating tables.'
            #self.drop_tables()
            self.create_tables()
            #print 'Tables created.'
        except Exception,msg:
            print msg
            self.connection = None
        if not self.connection:
            print 'DB connection Failed.'
            sys.exit(1)
        else:
            print 'Database connection successful.'
            cur = self.connection.cursor()
            cur.execute('SELECT SQLITE_VERSION()')

            data = cur.fetchone()

            print "SQLite version: %s" % data

    def create_tables(self):
        try:
            company_table = """
                create table if not exists last_searched_company
                (
                    company_index int,
                    company_name text
                );
            """

            profile_table = """
                create table if not exists full_profile_index
                (
                    profile_index int,
                    company_name text
                );
            """
            if self.connection:
                cur = self.connection.cursor()
                cur.execute(company_table)
                self.connection.commit()
                cur.execute(profile_table)
                self.connection.commit()
                cur.close()
        except Exception,msg:
            print msg

    def drop_tables(self):
        query = 'drop table if exists last_searched_company'
        cur = self.connection.cursor()
        cur.execute(query)
        self.connection.commit()
        query = 'drop table if exists full_profile_index'
        cur.execute(query)
        self.connection.commit()
        cur.close()

    def execute_query(self,query):
        cur = self.connection.cursor()
        cur.execute(query)
        self.connection.commit()
        cur.close()

    def execute_query_with_results(self,query):
        results = []
        cur = self.connection.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            results += [row]
        cur.close()
        return results

    def update_last_searched_company(self,company_index,company_name):
        query = "delete from last_searched_company;"
        self.execute_query(query)
        query = "insert into last_searched_company(company_index,company_name) values(%s,'%s')" % (str(company_index),company_name)
        self.execute_query(query)

    def delete_all_data(self):
        query = "delete from last_searched_company;"
        self.execute_query(query)
        query = "delete from full_profile_index;"
        self.execute_query(query)

    def get_last_searched_company_index(self):
        query = 'select * from last_searched_company limit 1'
        return self.execute_query_with_results(query)

    def update_last_crawled_profile_index(self,index,company_name):
        query = "delete from full_profile_index;"
        self.execute_query(query)
        query = "insert into full_profile_index(profile_index,company_name) values(%s,'%s')" % (str(index),company_name)
        self.execute_query(query)

    def get_last_crawled_profile_index(self):
        query = 'select * from full_profile_index limit 1'
        return self.execute_query_with_results(query)

    def close(self):
        if self.connection:
            self.connection.close()

#db = DBHandler()
#query = "delete from full_profile_index;"
#db.execute_query(query)
#db.update_last_searched_company(2,'Company')
#print db.get_last_searched_company_index()[0][0]

