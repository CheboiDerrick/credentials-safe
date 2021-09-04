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
    def display_credentials(self,sitename):
        for credential in Credential.credentials_list:
            if credential.sitename==sitename:
                return credential