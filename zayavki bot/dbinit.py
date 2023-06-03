from cfg import *

#---------------------------------------------------------

def db_init():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
                   userid INTEGER
                   name TEXT
                   balance INTEGER
                   btc REAL
                   eth REAL
                   ltc REAL
                   status INTEGER     
               )""")
    conn.commit()
    conn.close()
