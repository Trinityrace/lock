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






# if __name__ == '__main__':
#     main()