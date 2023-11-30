import re 

# Do I need any modules? If so, as a best practice, import them at the top of the file

'''
Project Description: Website Sign-Up
In this project, you will write a program that prompts a user to sign up for a website. The user must come up with a username and password, then log in using the username and password.
There are requirements for both the username and password. If either one doesn’t meet the requirements, print an appropriate error message and ask the username for a new username and password.
If they are both valid, store them as variables. Then ask the user to log in using the username and password they chose.
'''

# Problem: How should I start? 
# Solution: Your program should start with a print statement clearly explaining to the user both the username and password requirements. 
# Test, push code, test push code, test push code :)

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


# Define error messages

# Set invalid username error message as a variable
# invalid_username = "Invalid username"

# Set username taken error message as a variable
# duplicate_username = "Username taken"


# Problem: The user must be continuously prompted for input.
# Solution(s): What tools do we have in place to facilitate this? If-then-else statements in conjunction with a while loop. 
# Test, push code, test push code, test push code :)



while True:

    username = input('Please enter a username: ')   # get username
    password = input('Please enter a password: ')   # get password 
    taken_names = ['admin', 'admin123', 'root']     # taken name list
    # print(username)
    # print(password)
    # break
    if username in taken_names:                     # username test if already taken
        print("Username taken")
        continue

    if username[0].islower() == False:              # test for first character lower case
       print("Invalid username")
       continue
    
    test_username_match = re.fullmatch('[a-z0-9A-Z_]+',username)
  
    if test_username_match:
        print("Invalid username")
        continue

    
    # print("I am here")







    # if len(user_string) == 0: # if the string is empty, stop the loop
    #     print("Invalid username")
    #     break # we are done
#     elif user_string[0].islower():  # does username start with lowercase letter?
#         new_string += user_string
#         print("username starts with lowercase letter.")
#         print(new_string)
#         continue
#     elif not user_string.isalnum():
#         print("Looks like a special character, lets continue")
#         continue
#     elif user_string[0].islower():  # does username start with lowercase letter?
#         new_string = re.search('[_]', user_string)
#         print("username contains _.")
#         print(new_string)
#         continue
# elif not user_string.isalnum() == ['admin', 'admin123', 'root']:
#         print("Looks like a special character, lets continue")
#         continue
# print("Have a nice day")

# make it if they 
# code from class today




# Problem: How are we managing error messages?
# Solution(s): We can serve error messages from strings in variables. We can serve error messages from a collection instrument such as a list or a tuple. Bad practice would be hardcoding error messages in our code. Though it works, it would be come difficult to handle and manage should a program be scaled up in the future or new error messages are added in the future with features. Handle this before you begin your while loop
# Test, push code, test push code, test push code :)



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







