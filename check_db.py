import sqlite3

conn = sqlite3.connect('./pybo.db')

c = conn.cursor()

c.execute("SELECT * FROM answer")
# c.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(c.fetchall())
print(c.fetchone())


