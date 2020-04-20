#! shebang
# chmod +x run.py

import string
import random

from users import User
from credentials import Credentials

def create_login(name,email,pin):
    '''
    '''
    new_user= User(name,email,pin)
    return new_user


# if __name__ == '__main__':
#     main()