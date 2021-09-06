import random
import string
from user import User
class Credential():
    credentials_list=[]
    user_credentials_list = []
    def __init__(self,user_name,sitename,account_name,password):
        self.user_name=user_name
        self.sitename=sitename
        self.account_name=account_name
        self.password=password

    @classmethod
    def user_auth(cls,username,password):
        '''
        Method that takes in a username returns true if it matches a user in the users_list.

        Args:
            username: username of the user being searched
        Returns :
            User whose credentials match the entered credentials.
        '''
        for user in User.users_list:
            if (user.username == username and user.password == password):
                active_user=user.username
        return active_user

    def add_credential(self):
        Credential.credentials_list.append(self)

    def remove_credential(self):
        Credential.credentials_list.remove(self)

    @classmethod
    def find_credential(cls,sitename):
        for credential in Credential.credentials_list:
            if credential.sitename==sitename:
                return credential

    def generate_password(size=10, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        Function to generate a 10 character password for a specific site
        '''
        random_pass=''.join(random.choice(char) for _ in range(size))
        return random_pass

    @classmethod
    def display_credentials(cls,username):
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == username:
                user_credentials_list.append(credential)
        return user_credentials_list

    @classmethod
    def delete_credential(cls,sitename):
        for credential in Credential.credentials_list:
            if credential.sitename==sitename:
                message=f'Your {credential.sitename} of username {credential.account_name} and password {credential.password} has been successfully deleted'
                Credential.credentials_list.remove(credential)
                return message
