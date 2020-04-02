import unittest
from users import User

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

if __name__ == '__main__':
    unittest.main()
