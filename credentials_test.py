import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        '''
        setup method to run before each test case.
        '''
        self.new_credential = Credentials("instagram","trinity","123")#create credentials object

    def test_init(self):
        self.assertEqual(self.new_credential.platform,"instagram")
        self.assertEqual(self.new_credential.username,"trinity")
        self.assertEqual(self.new_credential.password,"123")

if __name__ == '__main__':
    unittest.main()
