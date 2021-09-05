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