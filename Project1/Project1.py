# Project 1 - Robin Maynard

### Website Sign-Up ###
# In this project, you will write a program that prompts a user to sign up for a website. 
# The user must come up with a username and password, 
# then log in using the username and password.
# There are requirements for both the username and password. 
# If either one doesn't meet the requirements, print an appropriate error message and ask
# the username for a new username and password.
# If they are both valid, store them as variables. Then ask the user to log in 
# using the username and password they chose.

### NEW USERNAME CODE SECTION ###

# Step 1 - Get new username input from the user.
new_username = input("Please follow the new username requirements when creating your account. \n"
                     "The new username must: \n"
                     "-Start with a lowercase letter. \n" 
                     "-Only contain letters, numbers and underscores. \n" 
                     "Enter a new username: \n "
                     )
print(new_username)

# Set error messages
# Set invalid username error message as a variable
# invalid_username = "Invalid username"

# Set username taken error message as a variable
# duplicate_username = "Username taken"

# Testing - confirm with boolean statement if new username follows requirements.

# TEST 1 - Does username start with a lowercase letter? - check completed successfully
test_result1 = new_username
if test_result1.islower() == True:
    print("test 1 pass")
else: 
    print("test 1 fail")

# TEST 2 - Does username only contain letters, numbers and underscores

allowed_characters_username = set('0123456789abcdefghijklmnopqrstuvwxyz_')
test_result2 = new_username
if set(test_result2).issubset(allowed_characters_username):
     print("test 2 pass")
else: 
     print("test 2 fail")

# TEST 3 - Is username already taken?
# already_taken = set('need to get from jean')
# test_result3 = new_username
# if set(test_result3).issubset(already_taken):
#      print("test 3 pass")
# else: 
#      print("test 3 fail")

# TEST 4 - Check if username passes all tests.
test_final_username = (test_result1 and test_result2)
print("Is new username valid?",test_final_username)


### NEW PASSWORD CODE SECTION ###

# Get new password input from the user.
# new_password = input("Please create a new password. \r
#                  The password must:\r
#                  -Contain at least 8 characters.\r
#                  -Contain at least one uppercase letter.\r
#                  -Contain at least one lowercase letter.\r
#                  -Contain at least one digit.\r
#                  -Contain at least one of these characters: !, ?, @, #, $, ^, &, *, _, -, \r
#                  -Doesn't contain any spaces.
#                  ")


# Set invalid password error message as a variable
# invalid_new_password = "Invalid password"

# If invalid password, loop back up to Get password step.
# If password is valid, print Sign up successful
# print("Sign up successful!")

# LOGGING IN STEPS - Prompt user to enter the newly created username & password to log into the system.
# Enter username
# user_name = input("Enter username. ")
# Enter password
# password = input("Enter password")

# Check if username and password are correct.
# if new_username == user_name and new_password == password
# print(Login successful!)
#      else
#      print("Incorrect username and password.") # loop back to login step.
      

