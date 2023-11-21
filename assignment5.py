
# Assignment 5 
# Robin Maynard
# I did not fully complete this assignment. I was able to sum the columns,
# but not calculate the averages.


# You are given a 2D list representing a table of data with rows and columns.
# Write a Python program to calculate the sum and average of each column in the table.
# For example, if this is your list:
# data = [[45,56,89],[67,34,78],[23,67,34]]
# This would be your output:
# Column 1: Sum = 135, Average = 45.0
# Column 2: Sum = 157, Average = 52.33
# Column 3: Sum = 201, Average = 67.0
# Hint: Make a list to store the sums, and a list to store the averages.

# START OF ROBIN'S CODE:

# Here I am setting the variable for the provided 2D list.
lis = [
    [45,56,89],
    [67,34,78],
    [23,67,34]
    ]

final = []   # this will be the final list to hold the swapped column rows
 
for i in range(len(lis[0])):  # swapping columns to rows
    temp = []                 # this temp list will hold each column number and then will append to the final list
    for item in lis:
        temp.append(item[i])  # for loop add each swapped column row to final list
    final.append(temp)        

# COLUMN 1 CODE

column_1 = sum(final[0])    # I'm adding the column numbers 45 + 67 + 23
sum_1 = int(column_1)       # making sum an integer
average_1 = sum_1/3         # assign var to calculate the column average by dividing the sum by 3
print(f"Column 1: Sum = {column_1}, Average = {average_1}")   # printing Column 1

# COLUMN 2 CODE

column_2 = sum(final[1])    # I'm adding the column numbers 56 + 34 + 67
sum_2 = int(column_2)       # making sum an integer
average_2 = sum_2/3         # assign var to calculate the column average by dividing the sum by 3
average_2decimals = round(average_2, 2)   # rounding the average - limit answer to two decial places
print(f"Column 2: Sum =, {column_2}, Average = {average_2decimals}")  # printing column 2

# COLUMN 3 CODE

column_3 = sum(final[2])  # I'm adding the column numbers 89 + 78 + 34
sum_3 = int(column_3)     # making sum an integer
average_3 = sum_3/3       # assign var to calculate the column average by dividing the sum by 3
print(f"Column 3: Sum =, {column_3}, Average = {average_3}")  # printing column 3

# print("Thank you so much Jean for taking the time last minute to help me. You always give your class time and support!") 
# print("Robin is a slacker and didn't make enough time to complete this! :-)")


