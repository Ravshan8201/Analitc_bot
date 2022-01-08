import sqlite3
conn = sqlite3.connect('user_list.sqlite')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS L_TABLE(
TG_ID INTEGER ,

USLUG STRING

)''')
first_insert5 = '''
INSERT INTO L_TABLE VALUES ('{}','{}')
'''