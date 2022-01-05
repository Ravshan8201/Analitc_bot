import sqlite3
conn = sqlite3.connect('user_list.sqlite')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS Users(
TG_ID INTEGER ,
Lang INTEGER ,
F_name STRING,
Service STRING,
Pho_num INTEGER,
Ser_Stage STRING,
Place STRING,
Stage STRING
)''')
first_insert = '''
INSERT INTO Users VALUES ('{}',' ',' ',' ',' ',' ',' ','{}')
'''

place_upd = '''
UPDATE Users
SET Place = '{}'
WHERE TG_ID = '{}'
'''
place_select = '''
SELECT Place
FROM Users
WHERE TG_ID = '{}'
'''

ser_upd = '''
UPDATE Users
SET Service = '{}'
WHERE TG_ID = '{}'
'''
ser_select = '''
SELECT Service
FROM Users
WHERE TG_ID = '{}'
'''


phone_upd = '''
UPDATE Users
SET Pho_num = '{}'
WHERE TG_ID = '{}'
'''
phone_select = '''
SELECT Pho_num
FROM Users
WHERE TG_ID = '{}'
'''

post_upd = '''
UPDATE Users
SET Post = '{}'
WHERE TG_ID = '{}'
'''
post_select = '''
SELECT Post
FROM Users
WHERE TG_ID = '{}'
'''

upd_name = '''
UPDATE Users
SET F_name = '{}'
WHERE TG_ID = '{}'
'''
name_select = '''
SELECT F_name
FROM Users
WHERE TG_ID = '{}'
'''

get_id = '''
SELECT TG_ID 
FROM Users
Where TG_ID = '{}'
'''
lang = '''
UPDATE Users
SET lang = '{}'
WHERE TG_ID = '{}'
'''
lang_select = '''
SELECT Lang
FROM Users
WHERE TG_ID = '{}'
'''

stagee  = '''
UPDATE Users
SET Stage = '{}'
WHERE TG_ID = '{}'
'''
stage = '''
SELECT Stage
FROM Users
WHERE TG_ID = '{}'
'''

s_s_upd  = '''
UPDATE Users
SET Ser_Stage = '{}'
WHERE TG_ID = '{}'
'''
s_s_select = '''
SELECT Ser_Stage
FROM Users
WHERE TG_ID = '{}'
'''