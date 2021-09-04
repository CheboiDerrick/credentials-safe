import random
import string
class Credential:
    credentials_list=[]
    def __init__(self,sitename,username,password):
        self.sitename=sitename
        self.username=username
        self.password=password

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
        Function to generate an 8 character password for a credential
        '''
        random_pass=''.join(random.choice(char) for _ in range(size))
        return random_pass

    @classmethod
    def display_credentials(cls):
        return  cls.credentials_list
