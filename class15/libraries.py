import math # importing math library
import statistics # importing statistics
import pandas as pd # importing pandas to work with our dataframe
from datetime import date 
import requests
'''
Example
Import the math library.
Take the radius of a circle as user input.
Then, compute the area of the circle using the math library.
'''
# # Area of a circle = pi * radius * radius
# radius = int(input("what is the radius"))

# try:
#   area_of_a_circle = math.pi * radius * radius
#   print(f'area_of_a_circle {area_of_a_circle : .2f})
# except ValueError:
#       print("Invalid input\, numbers only")

'''
Exercise
Lets make some magic happen with the statistics library.
'''


# Middle value in odd numbered list
# odd_list = [1, 2, 3, 4, 5, 2, 9, 1, 3, 4, 6, 7, 8]

# median_of_an_odd_list = statistics.median(odd_list)

# print(median_of_an_odd_list)



# Average of two middle values
# even_list = [1, 2, 3, 4, 5, 2, 9, 1, 3, 4, 6, 7]
# average_of_an_even_list = statistics.median(even_list)
# print(average_of_an_even_list)

'''
Exercise
Lets make some magic happen with the pandas library.
'''

# # Dictionary with my users
# users = {
#   "acct_num": ['abb', 'cde', 'ggh', 'sdf'],
#   "name": ['jim', 'sarah', 'tanya', 'bob']
# }{

# # Load into a dataframe
# df = pd.DataFrame(users)
# # print(df)

# # # generate a csv
# # df.to_csv('test.csv',index=False)

'''
Exercise
Lets make some magic happen with the date time library.
'''
# today = date.today()
# print(today)
# print(f'Today is  {today}')

# print(f'The day is {today.day}')
# print(f'The month is {today.month}')
# print(f'The year is {today.year}')


'''
https://jsonplaceholder.typicode.com/
This website provides free api testing. Lets leverage python's request module to see if we can do a get request against this data
'''
my_response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(my_response.text)