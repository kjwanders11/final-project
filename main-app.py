def print_menu():
    print("Welcome to our Final Project")
    print("What would you like to do?")
    print("1. Create a new project")
    print("2. View projects")
    print("3. Exit")
    user_input = input("Enter your choice: ")
    return user_input

def get_user_info():
    user_name = input("Enter your name: ")
    user_password = input("Enter your password: ")
    return user_name, user_password

print("This is our main project code")
print_menu()
uname, upassword = get_user_info()
