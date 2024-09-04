
'''
1. import libraries
- hashlib: provides a helper function for efficient hashing of a file
or file-like object. Return a digest object that has been updated with contents of file objetct. 
=> encrypt the password
- getpass library: to prompt a user for a password without echoing what they type on the screen. 

'''

import hashlib
import getpass

# a dictionary holds key-value pair : username-password hash
password_manager = {}

# prompt menu:
'''
def options():
    while True: 
        choice = input("Enter 1 if you are a new user\nEnter 2 if you are an existing user\nEnter 0 to exit: ")
        if choice =='1':
            register()
        elif choice =='2':
            log_in()
        elif choice =='0':
            print('EXIT!')
            break # need to fix this bug also
        else:
            print("Invalid value.")
'''


# create register():
def register():
    username = input('Enter username: ')
    # getpass.getpass() prints a prompt then reads input from the user
    password = getpass.getpass('Enter your password: ')
    # create a function called check_password: this function will
    # check the strong of password. if it is strong, hash it
    # else, ask user to create a stronger one
    # 
    encrypted_password = hashlib.sha256(password.encode()).hexdigest()
    # add the key-value pair : username-encrypted_password to the dicionary1
    password_manager[username] = encrypted_password
    print("Congrats! Your account has been sucessfully created.")

# create log_in():
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


def options():
    while True: 
        choice = input("Enter 1 if you are a new user\nEnter 2 if you are an existing user\nEnter 0 to exit: ")
        if choice =='1':
            register()
        elif choice =='2':
            log_in()
        elif choice =='0':
            print('EXIT!')
            break # need to fix this bug also
        else:
            print("Invalid value.")


    
if __name__ == "__main__":
    # a dictionary holds key-value pair : username-password hash
    password_manager = {}
    options()
    print(password_manager)
