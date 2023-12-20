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