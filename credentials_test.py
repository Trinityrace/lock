import unittest
import random
import pyperclip

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

    def test_save_credentials(self):
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        '''
        does clean up after every test has run
        '''
        Credentials.credentials_list=[]

    def test_save_multiple_credentials(self):
        '''
        test to check whether we can save multiple credentials
        '''
        self.new_credential.save_credentials()
        test_credentials=Credentials("pinterest","khalifa","420")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        test to check deletion of credentials
        '''
        self.new_credential.save_credentials()
        test_credentials=Credentials("twitter","marqeez","0420")
        test_credentials.save_credentials()

        self.new_credential.delete_credentials #delete credential object
        self.assertEqual(len(Credentials.credentials_list),1)
    
    def test_find_username(self):
        '''
        test to find username and display credentials
        '''
        self.new_credential.save_credentials()
        test_credentials=Credentials("twitter","marqeez","0420")
        test_credentials.save_credentials()
        test_credentials2=Credentials("pinterest","khalifa","420")
        test_credentials2.save_credentials()

        find_creds=Credentials.find_cred("twitter")
        self.assertEqual(find_creds.platform,test_credentials.platform)

    def test_credentials_exist(self):
        '''
        test to check existance of credential
        '''
        self.new_credential.save_credentials()
        test_credentials=Credentials("snapchat","zaddy","doshi")
        test_credentials.save_credentials()

        credential_exist=Credentials.credentials_exist("zaddy")
        self.assertTrue(credential_exist)

    def test_display_credentials(self):
        '''
        test to display users credentials
        '''
        self.assertEqual(Credentials.credential_display(),Credentials.credentials_list)

    def test_generate_password(self):
        '''
        '''
        self.new_credential.save_credentials()
        generated_password =Credentials.generate_password(13)
        test_credentials =Credentials("reddit","doshi",generated_password)
        self.assertEqual(len(test_credentials.password),13)

if __name__ == '__main__':
    unittest.main()
