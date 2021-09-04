 class User:
    """"
    Class that generates new instance of users
    """
    users_list=[] #Empty list for storing users

    def __init__(self,username,password):
        '''
        __init__ method defines properties for the user objects.

        Args:
            self.username=username
            self.password=password
        '''
        self.username=username
        self.password=password
    
    def add_user(self):
        '''
        add_user method adds user objects into users_list
        '''
        User.users_list.append(self)

    def remove_user(self):
        '''
        remove_user method removes a saved user from the users_list
        '''
        User.users_list.remove(self)
        
    

