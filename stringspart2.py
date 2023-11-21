# Strings are Immutable

# first_name = 'JEAN'

# # apply method

# first_name = first_name.lower()
# print(first_name.lower())

# Excerise - Immutability
# my_string = 'hello'
# my_string.upper()
# print(my_string)

# my_string = my_string.upper()
# print(my_string)


# INDEXING
# animal = 'kangaroo'
# print(animal[4])
# last_letter = animal[len(animal) - 1] # remember me, last letter 
# print(last_letter)


# Indexing in Reverse

# greeting = "Hello World"
# print(greeting[-1]) # letter d
# print(greeting[-2]) # letter l
# print(greeting[-3]) # letter r
# print(greeting[-4]) # letter o
# print(greeting[-5]) # letter w

# SLICING [start:stop:step]
# my_fav_food = 'cheeseburger'
# # first six letters
# first_six_letters = my_fav_food[0:6:2]

# print(first_six_letters)

# Slicing in Reverse
# my_fav_music = 'classical'
# backwards = 
# my_fav_music[::-1]
#print(backwards)

# print(my_fav_music[1::-1])
# print(my_fav_music[2::-1])
# print(my_fav_music[3::-1])
# print(my_fav_music[4::-1])
# print(my_fav_music[5::-1])

# write some code to print the second half of a string. (if the string is odd length, you can choose whether to print the shorter or longer "half")

# my string
# dog_name = 'willow'
# find the middle of my string

# find the end of my string
# backwards = dog_name[3:6:1]
# output
# print(backwards)


# get my string from user
# second_half = input("What is your word? ")

# find the middle of my string
# start_val = int((len(second_half) / 2))
# print(start_val)
# find the end of my string
# stop_val = len(second_half)
#print(stop_val)
# output to user
# print(second_half[start_val:stop_val])

# Short function to find second half of a word
# def
#     second_half(word):

# Assignment 2 - Robin Maynard - 10.20.23 
# This code will prompt to enter an email address. The code will take the email address and run it through a number of code validations to check if it is in the proper format. 

# Step 1 - Get input from the user. This will prompt the user to enter their email address.
email_address = input("Enter your email addresss.  ") 
# result = email_address
print(email_address) # Test result - When run, I was prompted to enter my email address and then the email address was printed successfully.

# Step 2 - Sanitize with .strip(). This step checks for blank spaces at the beginning and end of the input. If blanks are found, .strip will remove them.
strip_email = email_address.strip()
print(strip_email) # Run result was successful. I entered an email with spaces before and after the text and when printed, the spaces were removed. I then ran the code again, but this time entered my email as rmay@gmail.ccom and the result was False as it should be.

# Step 3 - Test 1 - '.' at the thrid-to-last index. Before top level domain (examples: com, org, edu)
test_1 = (email_address[-4] == '.')
print(test_1) # Run result was successful. I entered email address rmay@gmail.com and the printed result was True. This tells us that the 4th to last character is equal to '.'.

# Step 4 - Test 2 - One '@' symbol at the fifth to last index or earlier
test_2 = ('@' in email_address[0:-5])
print("Test 2: Check for one'@' symbol before your '.' and top level domain:", test_2)  # Test was True when I entered rmay@gmail.com

# Step 5 - Test 3 - At least 1 character before the '@' symbol because an email address can't begin with '@'.
stop_value = email_address.index('@') #index position of my @ symbol
test_3 = (len(email_address[0:stop_value]) >=1)
print("test 3: at least 1 character before the @ symbol", test_3)

# Step 6 - Test 4 - No spaces within the string itself
test_4 = email_address.count(' ') == 0
print("test 4: Check for white space within the email address:", test_4)

# Step 7 - Test 5 - Final Test - Confirm with boolean statements that all test either passed or failed
final_result = (test_1 and test_2 and test_3 and test_4)
print("Does your email address pass all testing:",final_result)



