import sqlite3

conn = sqlite3.connect('timesheet.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS timesheet
            (name VARCHAR(255) NOT NULL,
            id INTEGER, 
            timePunchIn DATE 
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS login
            (username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            id INTEGER PRIMARY KEY AUTOINCREMENT)''')

first_employee = ('William Tomah', 1, '2025-01-02 11:00:31')

username1, password1, id = "wtomah", "DallasFan1", 1

cur.execute("INSERT INTO login (username, password, id) VALUES (?, ?, ?)", (username1, password1, id))

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
    firstname = input("First Name: ")
    lastname = input("Last Name: ")

    name = firstname + " " + lastname

    cur.execute("INSERT INTO login (username, password, id) VALUES (?, ?, ?)", (username, password, id))

    cur.execute("INSERT INTO timesheet (name, id, timePunchIn) VALUES (?, ?, ?)", (name, id))

    login()

def login():
    attempts = 5

    while attempts > 0:
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        cur.execute("SELECT * FROM login WHERE username = ? AND password = ?", (username, password))


        if cur.fetchall():
            print("Login Succesful!")
            attempts = 5
            menu()
            return
        else:
            attempts -= 1
            print(f"Username and/or password are invalid. You have {attempts} attempts left!")
            


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

        '''info = cur.execute('SELECT timesheet.name, login.username, timesheet.id FROM timesheet' \
        ' INNER JOIN login ON timesheet.id=login.id WHERE login.username = ?', (username))'''

        #print(info)

    elif option == 3:
        pass

    elif option == 4:
        login()
    
    elif option == 5:
        quit()

conn.commit()

intro()



conn.close()



