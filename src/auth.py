import hashlib

def create_user(cur):
    hash_object = hashlib.sha256()
    print("Enter your user information")
    username = input("Username: ")
    password = input("Password: ")
    firstname = input("First Name: ")
    lastname = input("Last Name: ")

    hash_object.update(password.encode('utf-8'))

    hex_digest = hash_object.hexdigest()

    name = f"{firstname} {lastname}"

    cur.execute(
        "INSERT INTO login (username, password) VALUES (?, ?)",
        (username, hex_digest)
    )

    cur.connection.commit()

    user_id = cur.lastrowid

    print("User created successfully!")
    return user_id


def login(cur):
    attempts = 5

    while attempts > 0:
        hash_object = hashlib.sha256()


        username = input("Enter Username: ")
        password = input("Enter Password: ")

        hash_object.update(password.encode('utf-8'))
        hex_digest = hash_object.hexdigest()

        cur.execute(
            "SELECT id FROM login WHERE username = ? AND password = ?",
            (username, hex_digest)
        )

        result = cur.fetchone()

        if result:
            print("Login Successful!")
            return result[0]  # return user_id
        else:
            attempts -= 1
            print(f"Invalid login. {attempts} attempts left.")

    return None
