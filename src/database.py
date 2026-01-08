import sqlite3

def get_connection():
    conn = sqlite3.connect('timesheet.db')
    return conn

def create_tables(conn):
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS timesheet (
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        user_id INTEGER NOT NULL,
        punch_in TEXT NOT NULL,
        punch_out TEXT)""")

    cur.execute('''CREATE TABLE IF NOT EXISTS login
            (username VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            id INTEGER PRIMARY KEY AUTOINCREMENT)''')
    

    conn.commit()