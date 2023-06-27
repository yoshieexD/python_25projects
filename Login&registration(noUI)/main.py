class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

existing_users = [
    User(username="user1", password="pass1"),
    User(username="user2", password="pass2"),
    User(username="user3", password="pass3")
]


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in existing_users:
        if user.username == username and user.password == password:
            print("Login successful!")
            return

    print("Invalid username or password.")


def register():
    username = input("Enter a username: ")

    for user in existing_users:
        if user.username == username:
            print("Username already taken.")
            return

    password = input("Enter a password: ")

    existing_users.append(User(username=username, password=password))
    print("Registration successful!")


choice = input("Do you want to have an account? (login/register): ")

if choice.lower() == "login":
    login()
elif choice.lower() == "register":
    register()
else:
    print("Invalid choice.")