 class User:
    users_list=[]
    def __init__(self,username,password):
        self.username=username
        self.password=password
    
    def add_user(self):
        User.users_list.append(self)

    def remove_user(self):
        User.users_list.remove(self)
        
    @classmethod
    def user_login(cls,username,password):
        for user in cls.users_list:
            if user.username==username and user.password==password:
                return True

