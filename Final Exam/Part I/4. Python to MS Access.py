import sqlite3

conn = sqlite3.connect("school.db")
print("Connected to database successfully")
conn.close()
