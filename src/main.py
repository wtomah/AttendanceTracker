from database import get_connection, create_tables
from auth import login, create_user, forgot_password
from menu import menu

def intro(cur):
    choice = input("Log In, Create User or Forgot Password (1/2/3): ")

    if choice == "1":
        user_id = login(cur)
        if user_id:
            menu(cur, user_id)

    elif choice == "2":
        user_id = create_user(cur)
        menu(cur, user_id)
    elif choice == "3":
        forgot_password(cur)
    

def main():
    conn = get_connection()
    create_tables(conn)
    cur = conn.cursor()

    while True:
        intro(cur)
        conn.commit()

if __name__ == "__main__":
    main()




