import random

class User():
    '''
    class for new user credentials and login info.
    '''
    users_list =[] # empty users list

    def __init__(self,name,email,pin):
        self.name = name
        self.email = email
        self.pin = pin
    pass
