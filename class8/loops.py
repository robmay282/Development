'''
Loops
1. While loops - Run as long as a given condition is true
2. Example - Create a while loop that prints every integer from 1 to 10
3. Create a while loop that will keep asking a user for their user id, until they type 'stop'.
4. Improved login system - Rewrite the username and login program. If the user enters the
incorrect username or login, they will keep receiving a prompt.
5. For Loops - Iterate through strings, lists, tuples, dictionaries, sets....
'for item in collection'
6. Write a loop that loops through a string, counts all the letters, and then print how long the
string is.
7. Take a string from the user, verify that it's a number. Write a loop that adds all the digits
together, then print the total.
8. Adding conditionals to loops - Write some code that will loop through a string and print
whether each letter is a vowel or a consonant.
9. You’re working on a data analysis project for a company that looks at written text. You’re only interested in letters from A-Z because you’re analyzing language. However, the data you’re given has some values that shouldn’t be there.
Write a Python program that takes a string as input from the user, removes anything from the string that isn’t a letter, and prints the new string.
You can loop through the string in a for loop, use the .isalpha() string method, and remember that strings are immutable, so you will have to build a new string from scratch using string concatenation.

'''

'''
1. While loops - Run as long as a given condition is true
2. Example - Create a while loop that prints every integer from 1 to 10
'''

# i = 0 # initilaization

# while i <= 10: #condition
#     print(i)
#     i += 1 # increment by 1

# print("I am out of the loop") # we are out of the loop

'''
3. Create a while loop that will keep asking a user for their user id, until they type 'stop'.
'''

#Prompt the user
# user_id = input("User Id:")  # if I type stop

# while user_id != "stop": # While the user id is anything but "stop"
#     user_id = input("User Id") # if I enter stop here
#     print("This ios where we are")

# print("Have a nice day") # this is outside of our while loop


'''
4. Improved login system - Rewrite the username and login program. If the user enters the
incorrect username or login, they will keep receiving a prompt.
'''
# #  system id and password

# sys_id = 'admin'
# sys_password = 'password'
# user_id = input("user id:")
# user_password = input("password:")

# while sys_id != user_id and sys_password != user_password:
#     print("incorrect user id or password")
#     # reprompt user for credentials, # will run back to line 60 if incorrect
#     user_id = "user id"
#     user_password = input("password")

# print("login successful, have a great day!")




'''
5. For Loops - Iterate through strings, lists, tuples, dictionaries, sets....
'for item in collection'
'''



'''
Lets loop through the string "Hello World"

'''
# my_string = 'Hello World'
# for item in my_string:  # for item in collection
#     print(item, end=" ")


'''
Lets loop through a list of colors

my_colors = ['red', 'green', 'orange', 'yellow']
# '''
# my_colors = ['red', 'green', 'orange', 'yellow']
# for m in my_colors:
#     print(m)


'''Lets loop through a tuple
my_fav_food = ('pizza', 'subs', 'chicken')
'''
# my_fav_food = ('pizza', 'subs', 'chicken')
# for food in my_fav_food:
#     print(food)

# Ranges range(start, stop, step)

# for i in range(16):
#     print(i)

# for i in range(5, 26):  # use i if stepping through numbers. i is the default. can use word or any valid variable.
#     print(i)

'''
6. Write a for loop that loops through a string, counts all the characters (spaces included), and then prints how long
the string is.
'''
# current_feeling = 'onward and upward'
# i = 0 # our counter
# for c in current_feeling:
#     i += 1 # each time through our string we will increment 1
#     print(i) # our output

'''
7. Take a string from the user, verify that it's a number. Write a loop that adds all the digits
together, then print the total.
# '''
# test_string = '14253'

# total = 0  # our running total

# for t in test_string: # we have to test to make sure this is a number
#     if t.isalnum(): # our test
#         t = int(t) # cast to our integer
#         total += t # add to total
#     print(total) # our output


'''
8. Adding conditionals to loops - Write some code that will loop through a string and print
whether each letter is a vowel or a consonant.
'''
''' old solution '''

# my_string = 'hello'
# i = 0
# for i in my_string:
# solution = my_string.count('a') + my_string.count('i') +
# my_string.count('o') + my_string.count('u')

# # list for reference
# my_vowel_list = ['a','e','i','o','u'] # our list collection
# my_vowel_tuple = ('a','e','i','o','u') # our tuple list collection
# my_vowel_string = (aeiou) # our string

# my_string = 'saturday'

# for letter in my_string:
#     if letter in my_vowel_string:
    #     print(letter, "is a vowel")
    # else:
    #     print(letter, "is a consonant")


'''
9. You’re working on a data analysis project for a company that looks at written text. You’re only interested in letters from A-Z because you’re analyzing language. However, the data you’re given has some values that shouldn’t be there.
Write a Python program that takes a string as input from the user, removes anything from the string that isn’t a letter, and prints the new string.
You can loop through the string in a for loop, use the .isalpha() string method, and remember that strings are immutable, so you will have to build a new string from scratch using string concatenation.
'''

test_string = '1234ABCDE%^&*$#'

new_string = '' # this will be our new string

for t in test_string:
    if t.isalpha(): # checks for anything that isn't a letter
        new_string += t # append to our new string, anything that evaluates to true
print(new_string)


