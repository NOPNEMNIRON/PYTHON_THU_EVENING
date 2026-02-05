import sqlite3

def dbCon_employee():
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            position TEXT,
            salary INTEGER
        )
    """)
    conn.commit()
    return conn