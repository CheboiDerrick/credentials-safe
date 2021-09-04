 class User:
    users_list=[]
    def __init__(self,username,password):
        self.username=username
        self.password=password
    
    def add_user(self):
        User.users_list.append(self)
        