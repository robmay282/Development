print("Importing my modules")

# def full_name(first, last):
#     fullname = first + ' ' + last
#     ''' This will creat3e a full name from a first and last name'''
#     myname = first + ' ' + last
#     print(fullname)

# # full_name('jean', 'juste')

# def even_num(num):
#     ''' Lets return True if Even, otherwise False'''
#     if num % 2 == 0:
#         print("True")
#     else:
#         print("False")

# even_num(5)

# def full_name(first, last):
#     fullname = first + ' ' + last
#     ''' This will creat3e a full name from a first and last name'''
#     myname = first + ' ' + last
#     print(fullname)

# # full_name('jean', 'juste')

# def even_num(num):
#     ''' Lets return True if Even, otherwise False'''
#     if num % 2 == 0:
#         print("True")
#     else:
#         print("False")

def vowel(word):
    ''' Is it a vowel or not?'''
    vowels = 'aeiou'
    for w in word:
        if w in vowels:
            print(f'{w} is a vowel')
        else:
            print(f'{w} is a consanant')

vowel('hello')


