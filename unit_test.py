import unittest
from user import User
from credentials import  Credential

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the User class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Taylor Ford",'wolf77') # create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"Taylor Ford")
        self.assertEqual(self.new_user.password,"wolf77")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.users_list = []

    def test_add_user(self):
        '''
        test_save_contact test case to test if the contact object is saved into
        the contact list
        '''
        self.new_user.add_user() # saving the new contact
        self.assertEqual(len(User.users_list),1)

    def test_add_multiple_users(self):
        '''
        test_add_multiple_users to check if we can save multiple user
        objects to our users_list
        '''
        self.new_user.add_user()
        test_contact = User("Alpha King","alpha77") # new contact
        test_contact.add_user()
        self.assertEqual(len(User.users_list),4)
    
    def test_remove_user(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_user.add_user()
        test_contact = User("Alpha King","alpha77") # new contact
        test_contact.add_user()

        self.new_user.remove_user()# Deleting a contact object
        self.assertEqual(len(User.users_list),1)


class TestCredential(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("Taylor Ford","twitter","t_ford","ford101") # create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.user_name,"Taylor Ford")
        self.assertEqual(self.new_credential.sitename,"twitter")
        self.assertEqual(self.new_credential.account_name,"t_ford")
        self.assertEqual(self.new_credential.password,"ford101")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credentials_list = []

    def test_add_credential(self):
        '''
        test_save_contact test case to test if the credential object is saved into
        the credentials list
        '''
        self.new_credential.add_credential() # saving the new contact
        self.assertEqual(len(Credential.credentials_list),1)

    def test_add_multiple_credentials(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_credential.add_credential()
        test_credential = Credential("Test","user","0712345678","test@user.com") # new contact
        test_credential.add_credential()
        self.assertEqual(len(Credential.credentials_list),2)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credentials_list = []

    def test_display_credentials(self):
        '''
        Test to check if the display_credentials method, displays the correct credentials.
        '''
        self.new_credential.add_credential()
        twitter = Credential("Taylor Ford","twitter","t_ford","ford101")
        twitter.add_credential()
        twitch = Credential("Alpha King","twitch","kingt","alpha77")
        twitch.add_credential()
        self.assertEqual(len(Credential.display_credentials(twitter.user_name)),2)

    def test_find_by_site_name(self):
        '''
        Test to check if the find_by_site_name method returns the correct credential
        '''
        self.new_credential.add_credential()
        instagram = Credential("Taylor Ford","instagram","t_ford","ford101")
        instagram.add_credential()
        credential_found = Credential.find_credential('instagram')
        self.assertEqual(credential_found,instagram)

    def test_user_auth(self):
        '''
        Function to test whether the login in function check_user works as expected
        '''
        self.new_user = User("Taylor Ford","ford77")
        self.new_user.add_user()
        user2 = User("Alpha King","alpha77")
        user2.add_user()

        for user in User.users_list:
            if user.username == user2.username and user.password == user2.password:
                active_user = user.username
            # return active_user
        self.assertEqual(active_user,Credential.user_auth(user2.username,user2.password))

if __name__ == '__main__':
    unittest.main()