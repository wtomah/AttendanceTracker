import datetime, sqlite3

conn = sqlite3.connect('timesheet.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS timesheet
            (name TEXT NOT NULL,
            id INTEGER, 
            timePunchIn DATE, 
            timePunchOut DATE 
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS login
            (username TEXT NOT NULL,
            password TEXT NOT NULL,
            id INTEGER)''')

first_employee = ('William Tomah', 1, '2025-01-02 11:00:31', '2025-01-02 20:18:00')

first_login = ('wtomah', '123', 1)

def login():
    pass

def menu():

    print("Welcome to the Attendance App")

    print("1. Check Timesheet ")
    print("2. Check In")
    print("3. Exit")

    option = int(input("Select an option: "))

    if option == 1:
        for row in cur.execute('SELECT * FROM Timesheet'):
            print(row)
    if option == 2:
        cur.execute("INSERT INTO timesheet (name, id, timePunchIn, timePunchOut) VALUES (?, ?, ?, ?)", first_employee)
    elif option == 3:
        exit()





conn.commit()


menu()


conn.close()



