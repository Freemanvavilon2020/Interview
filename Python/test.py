import sqlite3

conn  = sqlite3.connect('test_base.db')
cur = conn.cursor()
conn.commit()
conn.close()
