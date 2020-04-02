import math
import random
import pyperclip
import string

class Credentials(object):
    """
    Class that generates new instances of credentials
    """

    credentials_list = [] #empty credentials list        
    def __init__(self,platform,username,password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            platform: New user platform.
            username : New user username.
            password: New user password.
            
        '''
        self.platform = platform
        self.username = username
        self.password = password

    #save_user method to append on credentials_list
    def save_credentials(self):
        '''
        save_credentials method saves objects into credentials_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        method o delete credentials
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_cred(cls,string):
        '''
        method to find crentials using platform name
        '''
        for Credentials in cls.credentials_list:
            if Credentials.platform == string:
                return Credentials

    @classmethod
    def credentials_exist(cls,username):
        '''
        '''
        for credentials in cls.credentials_list:
            if credentials.username == username:
                return True
            else:
              return False

    


pass


