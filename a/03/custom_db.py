import sqlite3
import datetime as dt

_DBFILE = 'custom.db'

class CustomDB(object):

    def __init__(self):
        self.conn = sqlite3.connect(_DBFILE)
        try:
            self.conn.execute('''DROP TABLE CUSTOM_TABLE;''')
        except:
            pass
        # TODO: add more try except blocks to catch sql errors
        self.conn.execute('''CREATE TABLE CUSTOM_TABLE
                      (id    integer primary key not null,
                      url   text,
                      date  integer not null,
                      rating integer not null);''')

    def insert(self, i, u, d, r):
        joined = ','.join(['\"%s\"' % i,
                           '\"%s\"' % u,
                           '\"%s\"' % d,
                           '\"%s\"' % r])
        inst = "insert into CUSTOM_TABLE (id, url, date, rating)\
                values("+joined+");";
        print(inst)
        self.conn.execute(inst)
        self.conn.commit()

    @staticmethod
    def from_string_uk(date_as_string):
        '''accepts uk-style dates and returns custom invariant date for DB'''
        d = dt.datetime.strptime(date_as_string, '%d-%m-%Y')
        return d.strftime('%Y%m%d') 

    @staticmethod
    def from_string(date_as_string):
        '''accepts 1 Jan 2016 and returns custom invariant date for DB'''
        d = dt.datetime.strptime(date_as_string, '%d %b %Y')
        return d.strftime('%Y%m%d') 

    @staticmethod
    def check_query_string():
        '''checks the validity of query string'''
        raise NotImplementedError
        # TODO: Why? error will be raised anyway for bad query

    def query(self, query_string):
        '''do a query with the provided valid SQL query string''' # Directly using SQL query strings!!!
        inst = query_string
        cur = self.conn.cursor()
        cur.execute(inst)
        #return list(cur.fetchall())
        for row in cur.fetchall():
            print(row)


