import sqlite3
conn = sqlite3.connect('user_list.sqlite')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS ADM(
TG_ID INTEGER ,
Lang INTEGER ,
F_name STRING,
Pho_num INTEGER,
Place STRING,
Ser_Stage INTEGER
)''')
first_insert3 = '''
INSERT INTO ADM VALUES ('{}','{}','{}','{}','{}','{}')
'''
Se_upd  = '''
UPDATE ADM
SET Ser_Stage  = '{}'
WHERE TG_ID = '{}'
'''
Se_select = '''
SELECT Ser_Stage
FROM ADM
WHERE TG_ID = '{}'
'''

town_upd  = '''
UPDATE ADM
SET Place  = '{}'
WHERE TG_ID = '{}'
'''
town_select = '''
SELECT Place
FROM ADM
WHERE TG_ID = '{}'
'''

tel_upd  = '''
UPDATE ADM
SET Pho_num  = '{}'
WHERE TG_ID = '{}'
'''
tel_select = '''
SELECT Pho_num
FROM ADM
WHERE TG_ID = '{}'
'''

nam_upd  = '''
UPDATE ADM
SET F_name  = '{}'
WHERE TG_ID = '{}'
'''
nam_select = '''
SELECT F_name
FROM ADM
WHERE TG_ID = '{}'
'''

lang_upd  = '''
UPDATE ADM
SET Lang = '{}'
WHERE TG_ID = '{}'
'''
lang_select = '''
SELECT Lang
FROM ADM
WHERE TG_ID = '{}'
'''

s_upd  = '''
UPDATE ADM
SET Ser_Stage = '{}'
WHERE TG_ID = '{}'
'''
s_select = '''
SELECT Ser_Stage
FROM ADM
WHERE TG_ID = '{}'
'''
sel_id = '''
SELECT TG_ID 
FROM ADM
Where TG_ID = '{}'
'''

conn.commit()
