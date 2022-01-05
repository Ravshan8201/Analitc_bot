import sqlite3
conn = sqlite3.connect('user_list.sqlite')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS COMMON(
TG_ID INTEGER ,
Lang INTEGER ,
F_name STRING,
Pho_num INTEGER,
Place STRING
)''')
first_insert4 = '''
INSERT INTO COMMON VALUES ('{}','{}','{}','{}','{}')
'''
conn.commit()