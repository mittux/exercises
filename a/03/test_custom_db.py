# TODO: Add testing framework; presently I am just eye-balling the output
from custom_db import CustomDB

def insert_values(db):
    db.insert(5, 'https://www.bbc.co.uk/news', 20161207, 7)
    db.insert(6, 'https://www.cnn.com', db.from_string_uk("25-12-2015"), 6)
    db.insert(7, 'https://www.theverge.com', db.from_string("1 Jan 2016"), 10)
    db.insert(8, 'https://www.guardian.com/uk', db.from_string_uk("8-12-2016"), 9)
    db.insert(9, 'https://www.theregister.co.uk', db.from_string_uk("15-12-2016"), 7)


custdb = CustomDB()
insert_values(custdb)
#custdb.query('SELECT * FROM CUSTOM_TABLE') # - works
#custdb.query('SELECT * FROM CUSTOM_TABLE WHERE date > 20160606') # - works
#custdb.query('SELECT * FROM CUSTOM_TABLE WHERE rating > 8') # - works
#custdb.query('SELECT * FROM CUSTOM_TABLE WHERE 6 < rating < 10') # - broken, not valid sql?
#custdb.query('SELECT * FROM CUSTOM_TABLE WHERE rating < 10 AND rating > 6') # - works
#custdb.query('SELECT * FROM CUSTOM_TABLE WHERE id IN (6,7)') # - works
custdb.query('SELECT * FROM CUSTOM_TABLE WHERE rating < 10 AND rating > 6 AND date > %s' % custdb.from_string('10 Dec 2016')) # - works!