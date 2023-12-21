import math



''' Compile time errors / static errors'''


''' Exceptions / Runtime errors'''


''' ValueError '''


''' AttributeError '''


''' NameError '''
 

''' TypeError '''


# Lets prevent a user from dividing by zero


# Lets implement a try, except, than test



# userin = input("Enter a number: ")
# num_list = []
# num_list.append(float(userin))
# print(num_list)




'''
Exercise - Handling Invalid User Input
Write a Python program that takes a customeris age as user input and determines whether they're eligible for a senior discount.
Sometimes the age might not be in the correct format. Handle this using try-except, and print a descriptive error message if the age can't be cast to an int.
If the age is greater than or equal to 65, the customer is eligible for the discount. Otherwise, they're not eligible. Print whether the customer is eligible or not.

'''

# customers_age = int(input("Enter age please: "))
# if customers_age >= 65:
#     print("Eligible for discount")
# else:
#     print("Not eligible for discount")



''' Exercise 

You can add a finally block that will be executed regardless if the try block raises an error. 
This is good for cleaning up resources, because it will always be run.

'''

# def append_user_input(lis):
#     try:
#         # Tries to add a float to a list
#         lis.append(float(input("Enter a number: ")))
#     except ValueError:
#         # What to do if the user input can't be cast to a float
#         print("Invalid input")
#         return None
#     finally:
#         # This gets run no matter what, even if
#         # the function returns in the except block
#         print("your list:", lis)

# lis = []
# append_user_input(lis)


''' Exercise - Raising exceptions
Write a program to take the square root of user input.
Use a try-except statement to ensure the user inputs a float.
If the user inputs a negative number, raise a ValueError that will also be caught by the except statement. Make sure to write a descriptive message in the exception you raise.
'''

# Propogating exceptions (functions)
# while True:
#     try:
#         user_input = float(input("Please enter your number: "))
#     if user_input < 0:
#         raise ValueError
#     except ValueError
#         print("You must enter a float and it cannot be negative")
#     else:
#     result = math.sqrt(user_input)
#         print(result)
#     break


# Function that calculates average of two numbers


# def average_two_nums(num1, num2):
#     return (num1 + num2) / 2

# try:
#     print(average_two_nums(5, 3))
# except:
#     print("We can catch the error in the function call")


'''
Exercise
You have been assigned the task of creating a sales tax calculator for an e-commerce company. 
Write a Python function called calculate_final_price that takes the price of a product and the sales tax rate, 
and return the final price including tax.
The price should be a positive number, and the tax rate should be between 0 and 1 (exclusive). 
If either of them are outside of the valid range, raise a custom ValueError with an appropriate error message.
Now, test your implementation by asking the user to input a product price and sales tax rate, 
and call your function. Catch any potential ValueError raised by the function.
'''

def calculate_final_price(price, sales_tax_rate):

    if price <= 1: # Interval Comparison
        raise ValueError("Tax must be between 0 & 1")
    
    total_tax = price * sales_tax_rate
    return print + total_tax



# Interval comparison
# if 100 <= my_value <= 200:
#     pass



