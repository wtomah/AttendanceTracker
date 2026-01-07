def create_user(cur):
    print("Enter your user information")
    username = input("Username: ")
    password = input("Password: ")
    firstname = input("First Name: ")
    lastname = input("Last Name: ")

    name = f"{firstname} {lastname}"

    cur.execute(
        "INSERT INTO login (username, password) VALUES (?, ?)",
        (username, password)
    )

    user_id = cur.lastrowid

    cur.execute(
        "INSERT INTO timesheet (name, user_id, timePunchIn) VALUES (?, ?, NULL)",
        (name, user_id)
    )

    print("User created successfully!")
    return user_id


def login(cur):
    attempts = 5

    while attempts > 0:
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        cur.execute(
            "SELECT id FROM login WHERE username = ? AND password = ?",
            (username, password)
        )

        result = cur.fetchone()

        if result:
            print("Login Successful!")
            return result[0]  # return user_id
        else:
            attempts -= 1
            print(f"Invalid login. {attempts} attempts left.")

    return None
