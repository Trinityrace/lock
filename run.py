#! shebang
# chmod +x run.py
# ./run.py
#!/usr/bin/env python3.6

import string
import random

from users import User
from credentials import Credentials


#create user
def create_login(name,email,pin):
    '''
    Function to create new User
    '''
    new_user = User(name,email,pin)
    return new_user

#save user
def save_user(User):
    '''
    function to save user
    '''
    user.save_user()

#delete user
def del_user(user):
    '''
    function to delete user
    '''
    user.delete_user()

#find user
def find_user(user):
    '''
    function to find user by number and returns the user
    '''
    return User.find_by_name(name)

#user exists
def check_existing_user(user):
    '''
    function to check if user exists with that username and return
    a boolean
    '''
    return User.user_exist(name)

#displaying all credentials
def display_users():
    '''
    function to return saved credentials
    '''
    return User.display_users()


def main():
    print("Hello Welcome to your credentials list. What is your name?")
            user_name = input()

            print(f"Hello {user_name}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : cc - create a new credentials, dc - display credentials, fc -find a credentials, ex -exit the credentials list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New User")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()


                            save_user(create_user(name,email,pin)) # create and save new user.
                            print ('\n')
                            print(f"New USer {name}  created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_users():
                                    print("Here is a list of all your credentials")
                                    print('\n')

                                    for user in display_users():
                                            print(f"{user.name} .....{user.email}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the username you want to search for")

                            search_user = input()
                            if check_existing_user(search_user):
                                    search_user = find_user(search_user)
                                    print(f" {search_user.name}")
                                    print('-' * 20)

                                    # print(f"Phone number.......{search_user.phone_number}")
                                    print(f"Email address.......{search_user.email}")
                            else:
                                    print("That user does not exist")

                    elif short_code == "ex":s
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")




# if __name__ == '__main__':
#     main()