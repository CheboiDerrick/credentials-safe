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
        self.assertEqual(len(User.users_list),2)
    
    def test_remove_user(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_user.add_user()
        test_contact = User("Alpha King","alpha77") # new contact
        test_contact.add_user()

        self.new_user.remove_user()# Deleting a contact object
        self.assertEqual(len(User.users_list),1)

if __name__ == '__main__':
    unittest.main()