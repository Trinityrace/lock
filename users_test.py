import unittest
import pyperclip

from users import User

#first test
class TestUser(unittest.TestCase):
    '''
    test class for users behaviours
    '''
    def setUp(self):
        '''
        setup method to run before each test case.
        '''
        self.new_user = User("trinity","trinity@gmail.com","123")#create credentials object

    def test_init(self):
        self.assertEqual(self.new_user.name,"trinity")
        self.assertEqual(self.new_user.email,"trinity@gmail.com")
        self.assertEqual(self.new_user.pin,"123")

# if __name__ == '__main__':
#     unittest.main()

#second test
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)

#test for authentication of user
    def test_user_auth(self):
        self.new_user.save_user()
        test_user=User("trinity","trinity@gmail.com","123")
        test_user.save_user()
        self.assertTrue(self.new_user.user_auth("trinity","123"))

# #test to copy email
#     def test_copy_email(self):
#         '''
#         Test to confirm that email been copied is from found user
#         '''
#         self.new_user.save_user()
#         User.copy_email("trinity@gmail.com")

#         self.assertEqual(self.new_user.email,pyperclip.paste())


    # def test_find_username(self):
    #     '''
    #     test to find User by username and display credentials
    #     '''
    #     self.new_user.save_user()
    #     test_user=User("twir","marqeez@gmail.com","0420")
    #     test_user.save_user()
    #     test_user2=User("pint","khalifa@gmail.com","420")
    #     test_user2.save_user()

    #     find_users=User.name("twir")
    #     self.assertEqual(find_users.name,test_user.name)



# #third test
#     def test_delete_user(self):
#         self.users_list()

if __name__ == '__main__':
    unittest.main()
