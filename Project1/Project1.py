import re 

'''
Project Description: Website Sign-Up
In this project, you will write a program that prompts a user to sign up for a website. The user must come up with a username and password, then log in using the username and password.
There are requirements for both the username and password. If either one doesn’t meet the requirements, print an appropriate error message and ask the username for a new username and password.
If they are both valid, store them as variables. Then ask the user to log in using the username and password they chose.
'''

# print("Please follow these requirements when creating your account. \n"
#                      "USERNAME REQUIREMENTS: \n"
#                      "-Must start with a lowercase letter. \n" 
#                      "-Only contain letters, numbers and underscores. \n\n" 
                     
#                      "PASSWORD REQUIREMENTS:\n"
#                      "-Contain at least 8 characters.\n"
#                      "-Contain at least one uppercase letter.\n"
#                     "-Contain at least one lowercase letter.\n"
#                      "-Contain at least one digit.\n"
#                      "-Contain at least one of these characters: !, ?, @, #, $, ^, &, *, _, -, \n"
#                      "-Doesn't contain any spaces")


# Define messages as variables

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


# Problem: The user must be continuously prompted for input.
# Solution(s): What tools do we have in place to facilitate this? If-then-else statements in conjunction with a while loop. 
# Test, push code, test push code, test push code :)



while True:

    new_username = input('Please enter a username: ')    # get username
    new_password = input('Please enter a password: ')    # get password
    taken_names = ['admin', 'admin123', 'root']          # list oftaken name list


    if new_username in taken_names:                 # username test if already taken
        print(duplicate_username)                   # user gets error message variable that will print username already taken.
        continue                                    # loops user back to input - please enter a username

    if new_username[0].islower() == False:          # test for first character lower case
       print(invalid_username)                      # user gets error mesaage variable invalid username because first letter of username is not a lowercase letter.
       continue                                     # loops user back to iput - please enter a username  
    
    test_username_match = re.fullmatch('[a-z0-9A-Z_]+',new_username)     # test if username only contains letters, numbers or underscore
    if test_username_match == None:
        print(invalid_username)
        

    SpecialChara = ['!', '?', '@', '#', '$', '^', '&', '*', '_', '-']    # Begin password testing with function
        
    if len(new_password) <= 8:                                       # test for at least 8 charaters
        print(invalid_password)
          
    if not any(char.isdigit() for char in new_password):             # test for at least one digit
       print(invalid_password)

    if not any(char.isupper() for char in new_password):             # test for at least one uppercase letter
       print(invalid_password)

    if not any(char.islower() for char in new_password):             # test for at least one lowercase letter
       print(invalid_password)

    if not any(char in SpecialChara for char in new_password):       # test for at least one special charater
       print(invalid_password)

    else:
        print(successful_signup)

    
  
       
    

#   Doesn’t contain any spaces
    

# Problem: How are we testing the username requirements?
# Solution(s): It must start with a lowercase letter and only contain letters, numbers, and underscores.
#   -String methods? Regular Expression? Both are acceptable solutions. Regex is more advanced and will save you a few lines of code
# Test, push code, test push code, test push code :)



# Problem: How are we testing password requirements?
# Solution(s): At least 8 characters long
#   Contains at least one uppercase letter
#   Contains at least one lowercase letter
#   Contains at least one digit
#   Contains at least one of these characters: !, ?, @, #, $, ^, &, *, _, -
#   Doesn’t contain any spaces
#   -String methods? Regular Expression? Both are acceptable solutions. Regex is more advanced and will save you a few lines of code
# Test, push code, test push code, test push code :)


# Problem: How are we handling login process after successful sign up?
# Solution: With the assumption that after testing, the username and password fulfill requirements, we can reassign these values to more descriptive variables that are meant for the sign in and do a final test with a simple if else. Ternary operators are off the table as they cannot be used in a conditional expression.
# Test, push code, test push code, test push code :)


'''
These Git Commands are your best friends

git add . (what do I want to include in my next commit)
git commit -m"This is what I am doing" (captures your current changes before pushing)
git push (upload local repo to a remote repo)
git pull (fetches content from remote repo and updates your local repo to match)

'''







