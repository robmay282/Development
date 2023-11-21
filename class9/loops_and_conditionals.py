'''
Loops & Conditionals

1. What is the difference between a for and while loop?
2. Break keyword - Breaks out of the loop
3. Write some code that takes in numbers from a user one at a time. This should keep going until
the user enters 0. Then print the sum of all the numbers.nIf the user inputs something that isn’t a
number, an error message should appear and the program should stop. (Hint: use break)
4. Continue - skips over the iteration
5. Exercise: Sum of Even Digits
Take a string as user input, and verify that it’s a number.
Loop through each digit of the number, and only add it to the sum if it’s even.
Print the sum of all the even digits at the end.
Make sure to use the continue keyword.
6. Break vs Continue
7. Pass
8. While-Else and For-Else
9. Write some code that takes in strings from a user one at a time.
After each string is taken in evaluate if the string is empty, a number, a set of letters, or contains symbols.
    If the string is empty, stop the loop.
    If the string is a number, convert it to a float and add it to a total.
    If the string is a set of letters, concatenate to the other letter strings passed in.
    If it contains a symbol, or is none of the above, do nothing and repeat the loop.
Make sure to use break and/or continue.


'''

'''
1. What is the difference between a for and while loop?
'''
# when we are iterating through a collection. 
# while loop we will keep going while a condition is True
# for loop
# colors = ['red', 'green', 'blue']
# for C in colors:
#     print(C)

# while loop
# goal = 5
# num = 0
# while num <= goal:
#     print("not there yet", num)
#     num += 1

'''
Create a while loop that will prompt the user for the starting point and the ending point and
will count down from the user specified starting point to the user specified ending point, by 2.
'''

# var_starting_point = input('enter your starting point? ')
# var_ending_point = input('enter your ending point? ')

# while var_starting_point >= var_ending_point:
#     var_starting_point -=2
#     print(var_starting_point)


'''
Let's write a for loop that loops through our first name, output with one space between each letter
in the output
'''

# first_name = 'robin'
# for f in first_name:
#     print(f, end='*')

'''
2. Break keyword - Breaks out of the loop
'''
# userid = ""

# while userid !="stop":
#     userid = input("Enter something or hit stop")
#     print(userid)

# # while true

# while True:
#     print("Hello World")
#     print("Hello World")
#     print("Hello World")

# while userid !="stop":
#     userid = input("Enter something or hit stop")
#     print(userid)

# with break
# userid = ""
# while True:
#     userid = input("Enter something or hit stop")
#     if userid == 'stop':
#         break
#     print(userid)

# userid = ""

# while userid != "stop":
#      userid = input("Enter something or hit stop")
#      # variable userid == pizza123
#      for l in userid:
#         if l.isalpha():  # if the letters in trhat string pass this test
#             print(l,end="")
#         else:
#             break # this lets us break out of the inner loop
#      print()



'''
Write a while loop that takes input from the user that will decrement by 3 and will break out
of the loop when  the number is even lets use a print statement to help show us where we break
the loop
'''

# num = int(input("pick a number: "))

# while num != num % 2:
#     num -= 3
#     print(num)
#     if num % 2:
#         num -= 3
#         print("Your number is", num, "which is even")
#         break

'''
3. Write some code that takes in numbers from a user one at a time. This should keep going until
the
user enters 0. Then print the sum of all the numbers. If the user inputs something that isn’t a
number, an error message should appear and the program should stop. (Hint: use break)

Example (error):
5
7
c
Error: Not a number


Example (no error):
5
12
0
Sum: 17

Hint: "While True" is a looping construct in the Python programming language that allows a block of code
to be repeated indefinitely. It is often used in conjunction with a break statement, which allows
the loop to be exited under certain conditions.
'''


'''
4. Continue - skips over the iteration
'''

'''
Use the continue keyword to loop through a string and only print the vowels.
'''


'''
Loop through the string 'The year really flew by' and only print the consonants
'''

'''
5. Exercise: Sum of Even Digits
Take a string as user input, and verify that it’s a number.
Loop through each digit of the number, and only add it to the sum if it’s even.
Print the sum of all the even digits at the end.
Make sure to use the continue keyword.

'''
total = 0 

user_input = input("Enter your number: ")

for n in user_input:
    # convert to an integer
    #     n = int(n)
    if (n% 2) == 1: # test here for odd or even
        continue
    else:
        total +=n
print(total)


'''
6. Break vs Continue
'''




'''
7. Pass
'''


'''
8. While-Else and For-Else
'''


'''
9. Write some code that takes in strings from a user one at a time.
After each string is taken in evaluate if the string is empty, a number, a set of letters, or contains symbols.
    If the string is empty, stop the loop.
    If the string is a number, convert it to a float and add it to a total.
    If the string is a set of letters, concatenate to the other letter strings passed in.
    If it contains a symbol, or is none of the above, do nothing and repeat the loop.
Make sure to use break and/or continue.
'''



'''
REQUIREMENTS
    If the string is empty, stop the loop.
    If the string is a number, convert it to a float and add it to a total.
    If the string is a set of letters, concatenate to the other letter strings passed in.
    If it contains a symbol, or is none of the above, do nothing and repeat the loop.
'''

'''
"While True" is a looping construct in the Python programming language that allows a block of code to be repeated indefinitely.
'''

