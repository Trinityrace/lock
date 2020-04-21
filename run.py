# #! shebang
# # chmod +x run.py
# # ./run.py
# #!/usr/bin/env python3.6

import string
import random
from users import User
from credentials import Credentials

def create_login(name,email,pin):
    """
    function to create a new account for password locker
    """
    new_user=User(name,email,pin)
    return new_user

def save_login(user):
    """
    Function to save user login details
    """
    user.save_login()

def create_existing_credentials(platform ,username , password):
    """
    function to create existing credentials accounts 
    """
    new_credential=Credentials(platform ,username , password)
    return new_credential

def save_credentials(credential):
    """
    function to save credentials
    """
    credential.save_credentials()

def delete_credential(credential):
    """
    function to delete credentials
    """
    credential.delete_credential()

def find_credential(appName):
    """
    function tofind credentials details
    """
    return Credentials.find_creds(appName)

def credential_exist(username):
    """
    function to check if a credential exist
    """
    return Credentials.credential_exist()

def display_credentials():
    """
    function that returns a list of credentials listed
    """
    return Credentials.credential_display()

def authenticate_user(username,pin):
    return User.users_auth(username,pin)

def generate_password(length):
    """
    Function which generates a random password
    Args:
        the desired password length
    """
    return Credentials.generate_password(length)

def main():
    print("hey there, welcome to password locker  ,we  can save your passwords safely for all your accounts and also generate new ones  but please first login ")

    while True:
        print(
            """
        Use the following short codes to manage your account 
            'lg' - Login 
            'xx' - Close app
            """)
        print("What would you like to do?")
        shortCode = input().lower()
        if shortCode == "lg":
            print("Do you have an account? Y or N")
            decision = input().lower()

            if decision.startswith("n"):
                email=input("enter your email :")
                name=input("enter your name :")
                
                password = input("Enter your pin: ")#can use get pass method to show its a password is being entered
               
                print("\n")
                print (f"CONGRATULATIONS, {name} YOUR ACCOUNT HAS BEEN CREATED")
                print("Sign into your new account")
                sign_in_name = input("Enter your name : ")
                sign_in_pin = input("Enter your pin : ")#get pass
                save_login(create_login(name,email,password))
                if authenticate_user(sign_in_name,sign_in_pin):
                    
                    print("SUCCESSFULLY SIGNED IN")  
                    print("\n")
                    pass
                else:
                    print("Oops, you entered the wrong username/pin, we have to do this again :(")
                    print("\n")
            else:
                sign_in_name = input("Enter your username: ")
                sign_in_pin = input("Enter your pin: ")
                if authenticate_user(sign_in_name,sign_in_pin):
                    
                    print("SUCCESSFULLY SIGNED IN")  
                    print("\n")
                    pass
                else:
                    print("Oops, you entered the wrong username/pin, we have to do this again :(")
                    print("\n")

            while True:
                if authenticate_user(sign_in_name,sign_in_pin):
                    print(  """
                            welcome to password locker
                            use the following commands:
                            'cc' - enables you to create an a credential
                            'dc' - displays the credentials you have saved
                            'fc' - helps you find a credential by its social name
                            'dl' - deletes a credential
                            'ex' - logs you out
                            'help' - helps a user around the app
                            """
                            )
                    print(f"{sign_in_name}, what task would you like to perform?")
                    key_word = input().lower()

                    if key_word == 'cc':
                        print("Save a new credential")
                        platform = input("Input social app name: ")
                        print("\n")
                        name = input("Input your username: ")
                        print("\n")
                        option = input("Would you wish to have Vault generate a password for you? Y or N ").lower()
                        if option.startswith("y"):
                            print()
                            desired_len = int(input("How long would you like your password to be? Provide number only. "))
                            password = generate_password(desired_len)
                        else:
                            print("\n")
                            password = input("Enter your password: ")

                        save_credentials(create_existing_credentials(platform,name,password))
                        print('\n')
                        print(f"NEW CREDENTIALS FOR {platform} CREATED!")
                        print("_"*50)
                        print('\n')

                    elif key_word == 'dc':

                        if display_credentials():
                            print("HERE ARE YOUR CREDENTIALS")
                            print('\n')

                            for credentials in display_credentials():
                                print(
                                    f"""
    --------------------------------------------------
            Platform --- {credentials.platform}               
            Username --- {credentials.username}                                
            Password --- {credentials.password}               
    --------------------------------------------------
                                """
                                )
                                print('\n')
                        else:
                            print('\n')
                            print("You dont seem to have any credentials saved yet")
                            print("_"*50)
                            print('\n')

                    elif key_word == 'fc':
                        print("Enter the username you want to search for")
                        print("\n")
                        platform_search = input()
                        if credential_exist(platform_search):
                            find_creds = find_credential(platform_search)
                            print(
                                f"""
    -------------------------------------------------------
        Platform --- {find_cred.platform}               
        Username --- {find_cred.username}                               
        Password --- {find_cred.password}               
    -------------------------------------------------------
                                """)
                            print("_"*50)
                        else:
                            print("The credential does not exist")

                    elif key_word == "dl":
                        print("Enter the platform whose credentials you'd like to delete")
                        platform_delete = input()
                        if credential_exist(platform_delete):
                            platform_creds = find_credential(platform_delete)
                            delete_credential(platform_creds)
                            print(f"CREDENTIALS FOR {platform_creds.username} ")
                        else:
                            print("The credential does not exist") 

                    elif key_word == "ex":
                        print(f"Have a nice day {sign_in_name}")
                        print("_"*50)
                        break
                
                else:
                    print("Oops, you entered the wrong username/pin, we have to do this again :(")
                    print("\n")
                    break

        elif shortCode == "xx":
            print("GOODBYE")
            break
        
        else:
            print("You have entered an unknown short code, please try again")

if __name__ == '__main__':
    main()