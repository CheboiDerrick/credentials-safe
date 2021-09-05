from user import User
from credentials import Credential

def create_user(username,password):
	'''
	Function to create a new user account
	'''
	new_user = User(username,password)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	User.add_user(user)

def verify_user(username,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Credential.user_auth(username,password)
	return checking_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credential.generate_password()
	return gen_pass

def create_credential(user_name,sitename,accountname,password):
	'''
	Function to create a new credential
	'''
	new_credential=Credential(user_name,sitename,accountname,password)
	return new_credential

def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.add_credential(credential)

def display_credentials(username):
	'''
	Function to display credentials belonging to a user user
	'''
	return Credential.display_credentials(username)

def main():
	print(' ')
	print('Welcome to the credentials safe. \n This is your dashboard')
	while True:
		print(' ')
		print("*"*60)
		print('Enter a code below to manage  application: \n na-Create New Account \n li-Log In \n ex-Exit')
		short_code = input('Enter a code: ').lower().strip()
        
		if short_code == 'ex':
			break

        elif short_code == 'na':
            print("-"*60)
            print(' ')
            print('To create a new account:')
            username = input('Enter your first name - ').strip()
            password = input('Enter your password - ').strip()
            save_user(create_user(username,password))
            print(" ")
            print(f'New Account Created for: {username}. Your password is: {password}. Keep it safe for you will need it for subsequent logins')


if __name__ == '__main__':
	main()