''' Tuples & Sets '''

'''
Fun Facts about Tuples
    -ordered and unchangeable (example, storing a username and password, storing an RGB value that must not change)
    -can't add or remove items
    -round brackets
    -faster than lists
    -used to store constants
    -used heterogeneous data structures (integers, floats, strings, etc) for example someone's age, gender and last name, (15, 'M', 'JONES')
    -heterogenous data structures save memory. why? lists need to over-allocate to account for new elements
    -readability
    -lets the programmer or other programmer know, this data collection should not be altered
'''

my_number_tuple = (1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 8, 8, 8, 9, 10, 10, 10, 10)

# Use the count Tuple method to count how many instances we have for 2, 3, 8, 9, 10

# print(my_number_tuple)

# print(my_number_tuple)

# print(my_number_tuple)

# print(my_number_tuple)

# print(my_number_tuple)


my_letter_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')

# Use the index tuple method to return the position of letters b, d, f, h, and i

# print(my_letter_tuple)

# print(my_letter_tuple)

# print(my_letter_tuple)

# print(my_letter_tuple)

# print(my_letter_tuple)




my_data = ('dsec', 'sdsw', 'sdwx', 'bxwx', 'lwkw')

# # Access dsec via indexing

# print(my_data)

# # Access sdwx via indexing

# print(my_data)

# # Access lwkw via indexing

# print(my_data)


# Add these two tuples in a new tuple called nature

animals = ('giraffe', 'gazelle', 'bird', 'dog', 'cat')

trees = ('maple', 'redwood', 'sycamore')




# Add these two tuples in a new tuple called food

fruits = ('mango', 'orange', 'apple')

vegetables = ('zucchini', 'onion', 'garlic')



# Tuple unpacking - unpacking values into variables

# Lets unpack my_tuple into variables and print out the second and last variables

my_tuple = (1, 2, 3)

# Let do some looping! 

weekdays = [("Monday", 1), ("Tuesday", 2), ("Wednesday", 3), ("Thursday", 4), ("Friday", 5), ("Saturday", 6), ("Sunday", 7)]



'''
You have a tuple of numbers:
numbers = (1,2,3,4,5,6,7,8,9,10,11,12)
You have a tuple of months:
months = ("January","February","March","April","May","June", "July","August","September","October","November","December")
Use these tuples to make a list of tuples where each tuple contains a number and the month it corresponds to, like this: [("January",1),...,("December",12)]
Now print each month and its number using tuple unpacking in a for loop. The first line of output should look like this:
January is month 1 of the year.

'''

numbers = (1,2,3,4,5,6,7,8,9,10,11,12)
months = ("January","February","March","April","May","June", "July","August","September","October","November","December")


# Using the index of one of our tuples to iterate, lets do a for loop


# The code within our for loop to execute will create our tuple and append to our list


# We can than unpack this tuple in another for loop to create the required output


