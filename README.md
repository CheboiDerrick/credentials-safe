# Credential Safe

## By [Derrick Cheboi](https://github.com/CheboiDerrick/)

## Description
Credential safe is a terminal run python application that enables a user to save their credentials for different sites in their safes (accounts). A single user has a safe (account) where their credentials are stored and protected by a password.

## Application Behaviour
These are the behaviours/features that the application implements for use by a user.

A user should be able to:
* Create an account with their details - username and password
* Store their existing login credentials
* Generate a password  or enter their own password for a new credential/account
* View all the credentials stored in their safe.

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Start the main menu | **In terminal: $./main.py** | Welcome, choose an option: na-Create New User Account, li-Log In, ex-Exit |
| Display prompt for creating an account | **Enter: ca** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: li** | Enter your username and password |
| Display credential management menu| **Successful login** | Choose an option: cc - Create Credential, sc - Show all storedCredentials, dc - Delete Credential, ex - exit |
| Display prompt for creating a credential | **Enter: cc** | Enter the site name, your username and password |
| Display a list of stored credentials | **Enter: sc** | Prints a list of saved credentials |
| Display prompt to delete a stored credential | **Enter: dc** | Enter the site name of the credential to delete. |
| Exit application | **Enter: ex** | Exit the current navigation stage |

## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/CheboiDerrick/credentials-safe
        $ cd credentials-safe

## Running the Application
* To run the application, in your terminal:

        $ chmod +x main.py
        $ ./main.py
        
## Testing the Application
* To run the tests for the class file:

        $ python3.8 unit_test.py
        
## Technologies Used
* Python -(3.8)

## License
[MIT](https://github.com/CheboiDerrick/credentials-safe/blob/main/LICENSE) 

&copy;2021
