#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Codengine'

import sqlite3
import sys

class DBHandler:
    def __init__(self):
        try:
            self.connection = sqlite3.connect('sqlitedb.db')
            print 'Creating tables.'
            self.create_tables()
            print 'Tables created.'
        except Exception,msg:
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
        tables = """
            create table last_searched_company
            (
                id int auto_increment not null primary key,
                company_index int,
                company_name text
            );
            create table full_profile_index
            (
                id int auto_increment not null primary key,
                profile_index = int,
                company_name text
            );
        """
        if self.connection:
            cur = self.connection.cursor()
            cur.execute(tables)
            cur.close()

    def update_last_searched_company(self,company_index,company_name):
        pass

    def get_last_searched_company_index(self):
        pass

    def update_last_crawled_profile_index(self,index,company_name):
        pass

    def get_last_crawled_profile_index(self):
        pass

    def close(self):
        if self.connection:
            self.connection.close()
