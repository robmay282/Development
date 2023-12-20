import re # imported regular expressions to use for testing

# Robin Maynard
# Intro to Programming Fall 2023
# Project 1
# Due Date 12/1/23

'''
Project Description: Website Sign-Up
In this project, you will write a program that prompts a user to sign up for a website. The user must come up with a username and password, then log in using the username and password.
There are requirements for both the username and password. If either one doesn’t meet the requirements, print an appropriate error message and ask the username for a new username and password.
If they are both valid, store them as variables. Then ask the user to log in using the username and password they chose.
'''
# Print statement to inform the user of the username & password requirements.

print("You must follow these requirements when creating your account. \n"
                     "USERNAME REQUIREMENTS: \n"
                     "-Must start with a lowercase letter. \n" 
                     "-Only contain letters, numbers and underscores. \n\n" 
                     
                     "PASSWORD REQUIREMENTS:\n"
                     "-Contain at least 8 characters.\n"
                     "-Contain at least one uppercase letter.\n"
                    "-Contain at least one lowercase letter.\n"
                     "-Contain at least one digit.\n"
                     "-Contain at least one of these characters: !, ?, @, #, $, ^, &, *, _, -, \n"
                     "-Doesn't contain any spaces")


# Define print messages as variables

# Set invalid username error message as a variable
invalid_username = "Invalid username"

# Set username taken error message as a variable
duplicate_username = "Username taken"

# Set invalid password message as a variable
invalid_password = "Invalid password"

# Set sign up successful message as a variable
successful_signup = "Sign up successful!"

# Set incorrect username or password message as a variable
incorrect_login = "Incorrect username or password"

# Set login successful message as a variable
login_successful = "Login successful!"

while True:      # start while loop for user to enter new username & password credentials, check validity and if they pass all checks, prompt them to sign into the website. 

    new_username = input('Please enter a new username: ')    # get user to enter new username
    new_password = input('Please enter a new password: ')    # get user to enter new password
    taken_names = ['admin', 'admin123', 'root']              # list of taken usernames


    if new_username in taken_names:                 # username test if already taken
        print(duplicate_username)                   # user gets error message variable that will print username already taken.
        continue                                    # loops user back to input - please enter a username

    if new_username[0].islower() == False:          # test for first character lower case
       print(invalid_username)                      # user gets error mesaage variable invalid username because first letter of username is not a lowercase letter.
       continue                                     # loops user back to iput - please enter a username  
    
    test_username_match = re.fullmatch('[a-z0-9A-Z_]+',new_username)     # test if username only contains letters, numbers or underscore
    if test_username_match == None:
        print(invalid_username)
        

    SpecialChara = ['!', '?', '@', '#', '$', '^', '&', '*', '_', '-']    # define list for password required special characters
    
    # Begin password testing
        
    if len(new_password) <= 8:                                       # test for at least 8 charaters
        print(invalid_password)
        continue
    if not any(char.isdigit() for char in new_password):             # test for at least one digit
        print(invalid_password)
        continue
    if not any(char.isupper() for char in new_password):             # test for at least one uppercase letter
        print(invalid_password)
        continue
    if not any(char.islower() for char in new_password):             # test for at least one lowercase letter
        print(invalid_password)
        continue
    if not any(char in SpecialChara for char in new_password):       # test for at least one special charater
        print(invalid_password)
        continue
    if new_password.count(' ') != 0:                                 # test for blank spaces
        print(invalid_password)

    else:
        print(successful_signup)                                     # informing user of successful signup
                                   
    print("Please enter your username and password: ")               # prompting user to login to website with the newly created valid credentials 
    
    sys_username = input('Enter username: ')                         # setting variable to hold username
    sys_password = input('Enter password: ')                         # setting variable to hold password 

    if sys_username == new_username and sys_password == new_password:  # comparing newly created username & password to what they entered when signing into the website
        print(login_successful)                                        # if newly created matches what they enter on login, print login successful message. 
                                                                       #If not, prompt them to enter username and password again.
        break                                                          # End program
        

    
  
       



'''
These Git Commands are your best friends

git add . (what do I want to include in my next commit)
git commit -m"This is what I am doing" (captures your current changes before pushing)
git push (upload local repo to a remote repo)
git pull (fetches content from remote repo and updates your local repo to match)

'''







