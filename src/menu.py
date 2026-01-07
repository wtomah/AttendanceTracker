def menu(cur, user_id):

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
        cur.execute("""
                SELECT timesheet.name, login.username
                FROM timesheet
                JOIN login ON timesheet.user_id = login.id
                WHERE login.id = ?
            """, (user_id,))
        print(cur.fetchone())

    elif option == 3:
        pass

    elif option == 4:
        return
    
    elif option == 5:
        quit()