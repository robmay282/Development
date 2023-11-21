'''
Ranges
    - Must be integers, whole numbers
    - Used to iterate
    - Does not store all the numbers, but knows what they should be
    - Simple to write and create
    -saves memory
'''

# Using the range function, lets count to 20


# using the range function, lets count from 10 to 80


# using the range function, lets count from 0 to 10 by increments of 2


# Lets examine the output! Try to visualize the output


# Write a range that is every five years from 1960 to 2000. Use it with a variable and without
# for y in range(1960, 2000, 5):
#     print(i, end=' ')
# # Write a range that counts down from 30 to 0

'''
Exercise:
Rewrite the for loop we made last class that goes through a list and prints each item in the 
list, along with its index. (Hint: you can use a range, and you won't need a separate counter 
variable.)

Example:
planets = ["mercury", "venus", "earth", "mars"]
0: mercury, 1: venus, 2: earth, 3: mars
'''
# with range
# counter = 0 # elimiating the range will allow you to remove the counter.

# planets = ["mercruy", "venus", "earth", "mars"]

# for p in range(len(planets)):
#     print(f'{p}:{planets[p]}')


'''
Exercise:
You have a list of employees, and a list of job titles. Assume the lists are the same length and in the same order.
Use one for loop to go through both lists and print the job title of each employee.
For example, if these are your lists:
employees = ['Bob', 'Cynthia', 'Abdul']
job_titles = ['accountant', 'engineer', 'recruiter']
This should be your output:
Bob's job title is accountant.
Cynthia's job title is engineer.
Abdul's job title is recruiter.

'''
employees = ['Bob', 'Cynthia', 'Abdul']
job_titles = ['accountant', 'engineer', 'recruiter']

my_stop_parameter = len(employee)

for i in range(len(employees)):
    employee = employees[i]
    job_titles = job_titles[i]

    print(f" {employees}: {job_titles}")


'''
Write some code that creates a range based on what the user enters. 
Challenge: you can make a range with 1, 2, or 3 numbers. How would you allow the user to pick any of these options?

'''
