import sqlite3

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
            id INTEGER AUTO INCREMENT PRIMARY KEY)''')

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

    cur.execute("INSERT INTO login (username, password, id) VALUES (?, ?, ?)", (username, password, id))

    login()


def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    cur.execute("SELECT * FROM login WHERE username = ? AND password = ?", (username, password))

    if cur.fetchall():
        menu()
    else:
        print("Username and/or password are invalid. Try again!")
        login()



def menu():

    print("Welcome to the Attendance App")

    print("1. Check Timesheet ")
    print("2. Show Profile")
    print("3. Check In/Check Out")
    print("4. Log Out")
    print("5. Exit")

    option = int(input("Select an option: "))

    if option == 1:
        for row in cur.execute('SELECT * FROM timesheet'):
            print(row)

    elif option == 2:

        info = cur.execute('SELECT timesheet.name, login.username, timesheet.id FROM timesheet' \
        ' INNER JOIN login ON timesheet.id=login.id WHERE login.username = ?', (username))

        print(info)

    elif option == 3:
        print("Are you checking in or checking out?")

    elif option == 4:
        login()
    
    elif option == 5:
        quit()

conn.commit()

intro()



conn.close()



