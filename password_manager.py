
import hashlib
import getpass
import re

def options():
    while True: 
        choice = input("Enter 1 if you are a new user\nEnter 2 if you are an existing user\nEnter 0 to exit: ")
        if choice =='1':
            register()
        elif choice =='2':
            log_in()
        elif choice =='3':
            find_password()
        elif choice =='0':
            print('EXIT!')
            break
        else:
            print("Invalid value.")

def register():

    username = input('Enter username: ')
    # getpass.getpass() prints a prompt then reads input from the user
    password = getpass.getpass('Enter your password: ')
    
    while True:
        if password_checker(password) == True:
            print("Your password is strong")
            break
        else:
            print("Your password is weak. try again")
            new_password = getpass.getpass('Enter new password: ')
            password = new_password

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # add the key-value pair : username-encrypted_password to the dicionary1
    password_manager[username] = hashed_password
    print("Congrats! Your account has been sucessfully created.")


def password_checker(password):
    # password: length: 8-20, at least 1 num, lower case , uppercase, special character.
    # Repeated matches: 
    checker = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W){8,16}$'

    if re.fullmatch(checker, password):
        print("Pass the test")
        return True
    else: 
        print("Fail! Try stronger password.")
        return False


def log_in():
    username = input("Enter your username: ")
    password = getpass.getpass('Enter your password: ')
    encrypted_password = hashlib.sha256(password.encode()).hexdigest()
    print(encrypted_password)
    if username in password_manager.keys():
        if password_manager[username] == encrypted_password:
           print("Login sucessful")
    else:
        print("Username or password is incorrect. Try again!")
    

if __name__ == "__main__":
    # a dictionary holds key-value pair : username-password hash
    password_manager = {}
    options()
    print(password_manager)
