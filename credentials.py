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

   
    