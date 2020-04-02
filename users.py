# import random
import unittest

class User():
    '''
    class for new user credentials and login info.
    '''
    users_list =[] # empty users list

    def __init__(self,name,email,pin):
        self.name = name
        self.email = email
        self.pin = pin

    def save_user(self):
        User.users_list.append(self)
    
    def delete_user(self):
        User.users_list.remove(self)
    
    @classmethod
    def user_auth(cls,name,pin):
        '''
        This method returns a boolean True if the username and pin inputted
        matches those of a user in the users_list
        '''
        for User in cls.users_list:
            if User.name == name and User.pin == pin :
                return True
            else:
                return False

if __name__ == '__main__':
    unittest.main()


    pass
