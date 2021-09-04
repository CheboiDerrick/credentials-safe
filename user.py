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
        
    @classmethod
    def user_exist(cls,username):
        '''
        Method that takes in a username returns true if it matches a user in the users_list.

        Args:
            username: username of the user being searched
        Returns :
            Contact of person that matches the number.
        '''
        for user in cls.users_list:
            if user.username==username:
                return True

    def correct_password(cls,password):
        for user in cls.users_list:
            if user.password==password:
                return True

