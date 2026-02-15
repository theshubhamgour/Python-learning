# Check if the username or passweord meets certain criteria

username = input("Enter your username: ") # this should be admin
password = input("Enter your password: ") # this should be pass

if username == "admin" and password == "pass":
    print("Access granted.")
else:
    if username != "admin":
        print("Invalid username.")
    if password != "pass":
        print("Invalid password.")
