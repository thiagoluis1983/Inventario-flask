import sqlite3 as sql

con = sql.connect ('form_db.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS users')

sql = '''CREATE TABLE "users" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "REGIONAL" TEXT,
    "CIDADE" TEXT,
    "LOCAL" TEXT,
    "DEVICE" TEXT,
    "TAG" TEXT,
    "USER" TEXT,
    "EMAIL" TEXT
    )'''

cur.execute(sql)
con.commit()
con.close()