import sqlite3
import random

conn = sqlite3.connect('timesheet.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS timesheet
            (name VARCHAR(255) NOT NULL,
            id INTEGER, 
            timePunchIn DATE, 
            timePunchOut DATE 
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS login
            (username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            id INTEGER PRIMARY KEY)''')

first_employee = ('William Tomah', 1, '2025-01-02 11:00:31', '2025-01-02 20:18:00')

username1, password1, id = "wtomah", "DallasFan1", 1

#cur.execute("INSERT INTO login (username, password, id) VALUES (?, ?, ?)", (username1, password1, id))

def intro():
    choice = int(input("Log In or Create User (1/2)"))
    if choice == 1:
        login()
    elif choice == 2:
        createUser()


def createUser():
    print("Enter your user information")
    username = input("Username: ")
    password = input("Password: ")
    id = random.randint(1,1000)

    cur.execute("INSERT INTO login (username, password, id) VALUES (?, ?, ?)", (username, password, id))

    login()


def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    cur.execute("SELECT * FROM login WHERE username = ? AND password = ?", (username, password))

    if cur.fetchall():
        menu()
    else:
        print("Try Again")


def menu():

    print("Welcome to the Attendance App")

    print("1. Check Timesheet ")
    print("2. Show Profile")
    print("3. Check In/Check Out")
    print("4. Exit")

    option = int(input("Select an option: "))

    if option == 1:
        for row in cur.execute('SELECT * FROM timesheet'):
            print(row)
    if option == 2:
        pass
    if option == 3:
        print("Are you checking in or checking out?")

    elif option == 4:
        login()

intro()

conn.commit()



conn.close()



