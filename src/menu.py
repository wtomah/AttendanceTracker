from datetime import datetime

def menu(cur, user_id):

    print("Welcome to the Attendance App")

    print("1. Check Timesheet ")
    print("2. Show Profile")
    print("3. Punch In")
    print("4. Log Out")
    print("5. Exit")

    option = int(input("Select an option: "))

    if option == 1:
        for row in cur.execute('SELECT * FROM timesheet'):
            print(row)

    elif option == 2:
        cur.execute("""
                SELECT timesheet.name, login.username, timesheet.user_id
                FROM timesheet
                JOIN login ON timesheet.user_id = login.id
                WHERE login.id = ?
            """, (user_id,))
        print(cur.fetchone())

        menu_option = input("Would you like to return to menu? (y/n)")

        if menu_option == 'y':
            menu(cur, user_id)
        else:
            quit()
        


    elif option == 3:
        punchInTime = datetime.now()

        cur.execute("""UPDATE timesheet 
                    SET timePunchIn = ?
                    WHERE user_id = ?""", (punchInTime, user_id))
        
        menu(cur, user_id)
        


    elif option == 4:
        return
    
    elif option == 5:
        quit()