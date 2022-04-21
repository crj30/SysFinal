import sqlite3 as sql

conn = sql.connect("database.db")

conn.execute("CREATE TABLE inventory (name TEXT, desc TEXT, quantity TEXT, checkinDate TEXT)")

conn.close()

print("Table Created Successfully")