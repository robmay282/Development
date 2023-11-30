from statistics import mode

''' Fun facts about dictionaries 

    -collection of keys and values
    -used to store associated information
    -keys are the words, values are the definitions

'''

# # How do we create a dictionary?

# user_data = {"user_id":"400",
#             "name":"Fritz"}

# print(user_data)

# print(type(user_data))

# # Bracket notation

# print(user_data["name"])
# print(user_data["user_id"])

# Add new key value
# user_data["address"] = 'elm street'
# print(user_data)

# # lets look at all the methods available to us
# print(dir(user_data._contains_("user_id"))

# # lets try one
# print(user_data["name"])

# Dict constructor
# new_dictionary = dict()
# print(new_dictionary)
# print(type(new_dictionary))
# Dictionary methods
# Lets use the keys methods to get the keys from this dictionary
# dog = {"breed": "japanese chin", "genter": "female",
#        "age": 7}


# Lets use the values methods to get the values from this dictionary
# print(f'The keys for our dog dictionary: {dog.keys()}')

# with an f string


# Lets use clear method to remove all elements
# dog = {"breed": "japanese chin", "genter": "female",
#        "age": 7}

# dog.clear()
# print(dog)

# Lets use get method to get a key value


# lets look at one of the parameters to show an error if the key doesnt exist


# Lets create a copy


# Lets remove a specified key with pop
# dog = {"breed": "japanese chin",
#        "genter": "female",
#        "age": 7}
# new_dog = dog.copy()
# print(new_dog)

# Lets remove a last inserted key-value pair with popitem

# dog = {"breed": "japanese chin",
#        "genter": "female",
#        "age": 7}
# new_dog = dog.popitem()
# print(new_dog)

# Get a list with each key-value pair with items
# dog = {"breed": "japanese chin",
#        "genter": "female",
#        "age": 7}
# key_value_pairs_in_a_dictionary = dog.items()
# print(key_value_pairs_in_a_dictionary)

# we can loop through

# dog = {"breed": "japanese chin",
#        "genter": "female",
#        "age": 7}

# for key, value in dog.items():
#     print(key, value)

# Update dictionary

# dog = {"breed": "japanese chin",
#        "genter": "female",
#        "age": 7}

# dog.update({"temperament":"happy"})  # add our new key valute pair
# print(dog)

# dog.update({"breed":"chihauhua"})
# print(dog)

# Update can also update current key value pairs, as well as adding

# Dictionaries vs Lists
# list1 = ['a', 'b', 'c', 'd', 'e']
# dict1 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 5: 'e'}

# print(list1[3])  
# print(dict1[3])  

# list1[3] = 'z'
# dict1[3] = 'z'

# print(list1[3])  
# print(dict1[3])  

'''
Write some code that takes two lists and converts them into one dictionary.
In:
list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]
Out:
{'one': 4, 'two': 10, 'three': 30}

'''

# list1 = ['one', 'two', 'three']
# list2 = [4, 10, 30]

# Using zip and dict methods
# Zip creates a zip object
# driver = ('sam', 'majestic', 'reynelle')
# car = ('yamaha', 'lexus', 'infiniti')

# combine_in_tuple = zip(driver, car)
# print(tuple(combine_in_tuple))

# Dict creates a dictionary

# my_keys = ['one', 'two', 'three']
# my_values = [4, 10, 30]

# my_dictionary = dict(zip(my_keys, my_values)) # this is creating our dictionary from 2 lists
# print(my_dictionary)

# Using dictionary comprehension

# my_keys = ['one', 'two', 'three']
# my_values = [4, 10, 30]

# my_dictionary = {keys : values for (keys, values) in zip (my_keys, my_values)}
# print(my_dictionary)

# zip function can be very useful

# my_keys = ['one', 'two', 'three']
# my_values = [1,2,3]



'''
Exercise

Write a dictionary that contains five words and their definitions. Then have your code print the word and their definition one at a time.
Hint: Use the items() method

'''
# dog = {"breed": "japanese chin",
#        "genter": "femaale",
#         "age": 7}
# for key, value in dog.items():
#     print(key, value)

# dog = {"breed": "japanese chin",
#        "genter": "female",
#        "age": 7}

# for key, value in dog.items():
#     print(key, value)


# As datasets, we can use bracket notation

# choices = {"flavors":['strawberry', 'vanilla', 'orange'],
#            "sizes":['large', 'medium', 'small']}

# print(choices["flavors"][0])  # strawberry

            
# print(choices["sizes"][1]) # mediums
'''
Exercise
Create a dictionary for an automobile including make, model, year, number of doors, and number of cylinders.

'''
# car = {"honda": "accord",
#        "year": "2000",
#        number of doors, and number of cylinders}


'''
In statistics, the mode is the value that appears most frequently in a dataset.
For example, in this list: [1,2,4,1,3,4,1,1] the mode is 1
Write some code that uses a dictionary to calculate the mode of a list.

'''
my_list = [1,2,4,1,3,4,1,1]

output = {}

# for m in my_list:      # for loop
#     if m in output:
#         output[m] += 1 # incrementing the count
#     else:
#         output[m] = 1 # add it initially

# print(output)

# for m in my_list:
#     output[m] = my_list.count(m) # can increment and update
# print(output)

# Statistics module
# find_my_mode = [1,2,4,1,3,4,1,1,2]
# result = mode(find_my_mode)
# print(result)


'''
Suppose you have a list of employee records that contain the following information for each employee: name, job title, salary. The records are stored as a list of dictionaries.
Use this list to create a dictionary where the keys are the job titles and the values are the average salaries for each job title.
Example:



records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000}]
Output: {'manager': 50000, 'developer': 62500}
'''


records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000}
           ]

output = {}

# Iterate through records and create 2 new lists to seperate devs and managers
mgr_list = [i for i in records if (i['title'] == 'manager')]
dev_list = [i for i in records if (i['title'] == 'developer')]

# loop for the average salaries

mgr_average_salary = sum(s['salary'] for s in mgr_list) / len(mgr_list)
# print(mgr_average_salary)

dev_average_salary = sum(s['salary'] for s in dev_list) / len(dev_list)
# print(dev_average_salary)

output.update({"manager": mgr_average_salary})
# print(output)
output.update({"developer": dev_average_salary})
print(output)

 



