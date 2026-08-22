username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "password123":
    print("Access granted!")
elif username == "user" and password == "userpass":
    print("Access granted!")
    print("Welcome, user!")
else:
    print("Access denied. Invalid username or password.")


    