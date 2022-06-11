import time
import hashlib
import psycopg2 as pg

user_input = ''

while user_input == '':
    user_input = input('input a password: ').strip()

hashed_password = hashlib.sha1(bytes(user_input, 'utf-8')).hexdigest().upper()

def check_pd(hashed_pass, plain_text):
    conn = pg.connect(database="database", user = "database",host='localhost' )
    cur = conn.cursor()
    cur.execute(f'select count from cracked_passwords where hash = \'{hashed_pass}\'')
    rows = cur.fetchall()
    if rows == []:
        return f'\npassword {plain_text} has not been cracked'
    else:
        count = rows[0][0]
        return f'\npassword {plain_text} has been cracked {count} times'

start=time.time()
print(check_pd(hashed_password,user_input))
print('\ntime taken: ' + str(time.time() - start) )
 
