from datetime import datetime

def menu(cur, user_id):
    while True:
        print("\nWelcome to the Attendance App")
        print("1. Check Timesheet")
        print("2. Show Profile")
        print("3. Punch In")
        print("4. Punch Out")
        print("5. Log Out")
        print("6. Exit")

        try:
            option = int(input("Select an option: "))
        except ValueError:
            print("Please enter a number.")
            continue

        # Check Timesheet
        if option == 1:
            cur.execute("""
                SELECT punch_in, punch_out
                FROM timesheet
                WHERE user_id = ?
                ORDER BY punch_in DESC
            """, (user_id,))
            rows = cur.fetchall()

            if not rows:
                print("No punch history.")
            else:
                for punch_in, punch_out in rows:
                    print(f"In: {punch_in} | Out: {punch_out}")

        # Show Profile
        elif option == 2:
            cur.execute("SELECT username FROM login WHERE id = ?", (user_id,))
            print("Username:", cur.fetchone()[0])

        # Punch In
        elif option == 3:
            cur.execute("""
                SELECT id FROM timesheet
                WHERE user_id = ? AND punch_out IS NULL
            """, (user_id,))

            if cur.fetchone():
                print("You are already punched in.")
                continue

            punch_in_time = datetime.now().isoformat(timespec="seconds")

            cur.execute("""
            INSERT INTO timesheet (user_id, punch_in)
            VALUES (?, ?)
            """, (user_id, punch_in_time))


            print("Punched in at", punch_in_time)

        # Punch Out
        elif option == 4:
            punch_out_time = datetime.now().isoformat(timespec="seconds")

            cur.execute("""
                SELECT id FROM timesheet
                WHERE user_id = ? AND punch_out IS NULL
            """, (user_id,))

            row = cur.fetchone()

            if not row:
                print("You are not currently punched in.")
                continue

            cur.execute("""
                UPDATE timesheet
                SET punch_out = ?
                WHERE id = ?
            """, (punch_out_time, row[0]))

            print("Punched out at", punch_out_time)

        # Log Out
        elif option == 5:
            return

        # Exit
        elif option == 6:
            quit()

        else:
            print("Invalid option.")
