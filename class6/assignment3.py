# Assignment 3 - Robin Maynard
# This code will prompt the user to enter a username and password. The code will run the user's input through tests to check if the username and password are correct and then notifiy the user of the outcome.

# Step 1 - Set variable for system username
var_username = ('rmaynard')

# Step 2 - Set variable for system password
var_password = ('123abc')

# Step 3 - Log into system. Prompt user to enter their username.
user_username = input("Enter username. ")
# print(user_username) 

# Step 4 - Log into system. Prompt user to enter their password.
user_password = input("Enter password. ")
# print(user_password)

# Step 5 - Test 1. Check if username & password entered is equal to the sytem stored var_username & var_password. Then, notify the user if they entered the correct or incorrect username and password.
if(var_username) == user_username and var_password == user_password:
    print("Login is Successful")
else:
    print("Incorrect username and password")



