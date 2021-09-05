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
	print('Welcome to your credentials safe dashboard')
	while True:
		print(' ')
		print("*"*60)
		print("-"*60)
		print('Use these codes to navigate: \n na-New Account Creation \n li-Log In \n ex-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'ex':
			break

		elif short_code == 'na':
			print("*"*60)
			print("-"*60)
			print(' ')
			print('To create a new account:')
			username = input('Enter your user name - ').strip()
			password = input('Enter your password - ').strip()
			save_user(create_user(username,password))
			print(" ")
			print(f'New safe created for: {username}. Your password is: {password}. Keep it safe for you will need it for subsequent logins')#Notification of new account creation

		elif short_code == 'li':
			print("-"*60)
			print(' ')
			print('Enter your username and password to login:')
			username = input('Enter your user name - ').strip()
			password = str(input('Enter your password - '))
			user_exists = verify_user(username,password)

			if user_exists == username:
				print(" ")
				print(f'Welcome {username}. Please choose an option to continue.')
				print(' ')
				while True:
					print("*"*60)
					print("-"*60)
					print('Use the following codes for credentials management: \n cc-Create a Credential \n sc-Show Saved Credentials \n dc-Delete Credential \n ex-Exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*60)
					if short_code == 'ex':
						print(" ")
						print(f'See you soon {username}, meanwhile your secret is safe with us')
						break
					elif short_code == 'cc':
						print(' ')
						print('Kindly provide us with your credential details:')
						sitename = input('Enter site\'s name- eg-Twitter ').strip()
						account_name = input('Enter your account\'s name - The username on this site ').strip()
						while True:
							print(' ')
							print("-"*60)
							print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							print("-"*60)
							if psw_choice == 'ep':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif psw_choice == 'gp':
								password = generate_password()
								break
							elif psw_choice == 'ex':
								break
							else:
								print('Oops! Wrong option entered. Try again.')
						save_credential(create_credential(username,sitename,account_name,password))
						print(' ')
						print(f'Credential Created: Site Name: {sitename} - Account Name: {account_name} - Password: {password}')
						print(' ')
					elif short_code == 'sc':
						print(' ')
						if display_credentials(username):
							print('This is a list of credentials in your safe')
							print(' ')
							for credential in display_credentials(username):
								print(f'Site Name: {credential.sitename} - Account Name: {credential.account_name} - Password: {credential.password}')
							print(' ')	
						else:
							print(' ')
							print("There are no credentials saved with this account. Create a credential first")
							print(' ')
					else:
						print('Oops! Wrong option entered. Try again.')

			else: 
				print(' ')
				print('Oops! Wrong details entered. Try again or Create an Account.')		
		
		else:
			print("-"*60)
			print(' ')
			print('Oops! Wrong option entered. Try again.')

if __name__ == '__main__':
	main()