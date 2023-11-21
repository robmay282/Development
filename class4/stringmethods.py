# string methods

# capitalize()
# animal = 'dog'
# print(animal.capitalize())

# count()
# vehicle = 'toyota'
# print(vehicle.count('t'))

# casefold()
# name = 'Robin Maynard'
# print(name.casefold())

# center()
# name = 'Robin'
# print(name.center(20))

# count()
# fruit = 'banana'
# print(fruit.count('a'))

# expandtabs()
# name = 'R\to\tb\ti\tn'
# print(name.expandtabs(8))

# find()
# name = 'Welcome to my world.'
# print(name.find('w'))

# index()
# name = 'Welcome friends'
# print(name.index('f'))

# isalnum
# result = 'robin2m'
# print(result.isalnum())

# isalpha
# result = 'robin2m'
# print(result.isalpha())

# isdecimal
# result = '.87463'
# print(result.isdecimal())

# isdigit
# result = 'robin'
# print(result.isdigit())

# islower
# result = 'robin'
# print(result.islower())

# isupper
# result = 'Tobin'
# print(result.isupper())

# isnumeric
# result = '2335444'
# print(result.isnumeric())

# isspace
# result = ' '
# print(result.isspace())

# istitle
# result = 'The Catcher And The Rye'
# print(result.istitle())

# join()
# This is our list of students
our_class = ['Sam', 'Judith', 'Robin']

# Join our list with our separator
# result = ' '.join(our_class)
# we started with a list and ended up with a str
# print(result)
# print(type(result))
# print(type(our_class))

# partition()
# my string
# my_day = 'I had a pretty good day today'

# create my tuple with 3 parts
# result = my_day.partition('pretty')
# print(result)

# lower()
# my string
# name = 'ROBIN MAYNARD'
# result = name.lower
# print(name.lower())

# replace()
# my string
# word = 'bananas'
# result = word.replace('a','A')
# print(result)

# split
# word = 'bananas'
# result = word.split('a')
# print(result)

# splitlines()
# class_list = 'robin\njudith\njean'
# result = class_list.splitlines()
# print(result)

# startswith
# fruit = 'banana'
# result = fruit.startswith('b')
# print(result)

# strip()
# name = '  Robin Maynard'
# result = name.strip()
# print(result)


# x = 'hello'
# print(x)

# str2 = 'HELLO'.lower()
# print(str2)

# print(x == str2)  # they are equal to each other
# print(x is str2)  # they are not the same object

# print(id(x))
# print(id(str2))


# Write some code that will take a string from the user and print if it is a number or not.

# examples
# apple
# False
# 4 
# True

# write some code that will print a box around a string
user_input =('What is your word?')

# Top and Bottom of box
top_or_bottom = (len(user_input) * '*')

# Output
print(top_or_bottom)
print('*' + user_input + '*')
print(top_or_bottom)

