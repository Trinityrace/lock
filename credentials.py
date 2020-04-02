import random
import math
import pyperclip
import string

class Credentials(object):
    """
    Class that generates new instances of credentials
    """
        
    def __init__(self,platform,username,password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            paltform: New user platform.
            username : New user username.
            password: New contact password.
            
        '''
        self.platform = platform
        self.username = username
        self.password = password


    #pass


