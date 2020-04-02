import unittest
from users import User

#first test
class TestCredentials(unittest.TestCase):
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

#third test
    def test_delete_user(self):
        self.users_list()

if __name__ == '__main__':
    unittest.main()
