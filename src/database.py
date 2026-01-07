import sqlite3

def get_connection():
    conn = sqlite3.connect('timesheet.db')
    return conn

def create_tables(conn):
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS timesheet
            (name VARCHAR(255) NOT NULL,
            user_id INTEGER, 
            timePunchIn DATE 
            )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS login
            (username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            id INTEGER PRIMARY KEY AUTOINCREMENT)''')
    

    conn.commit()