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