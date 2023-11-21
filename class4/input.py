# input

# first_name = input('Good afternoon, what is your name?  ')
# prompts for name
# prompt for age
# casting the input an integer - converting
# age = int(input('How old are you'))
# print(type(first_name))
# print(type(age))
# output users first name
# print(first_name)
# response
# print('Hello, ',first_name)
# print('Hello, ' + first_name)


# use strip string method to sanitize user input
# no_spaces = first_name.strip()
# print(no_spaces)

# Example - write some code that will take a string from the user and print if it is a number or not.
# Examples: apple
# False

# 4
# true

fruit = input('what is your favorite fruit? ')
print(fruit)
print(fruit is int)
result = fruit.isnumeric()
print(result)
