import unittest
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
        self.assertTrue(self.new_user.users_auth("trinity","123"))

# #third test
#     def test_delete_user(self):
#         self.users_list()

if __name__ == '__main__':
    unittest.main()
