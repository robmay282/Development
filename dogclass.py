# class Dog:
#     #document const - our constructor
#     def _init_(self, name, birth_year, breed):
#         self.name = name
#         self.birth_year = birth_year
#         self.breed = breed
        
#     # string representation, this is what happens
#     def _str_(self):
#         return f'Name: {self.name}\nBirth year: {self.birth_year}\nBreed: {self.breed}'
    
#     # this function will calculate the dog's human age
#     def human_age(self):
#         today = datetime.now()
#         year = today.year
#         return year - self.birth_year


#     # This is using the reurn value from human_age(), we can make the function call, in another function
#     def show_results_from_another_function(self):
#         return 100 * self.human_age()

#     def dog_years(self):
#         dogyears = 7 * self.human_age()
#         return f'{self.name} is {dogyears} years old'

    
# dog4 = Dog()
# dog1 = Dog('fluffy', 2020, 'chihuhua')
# dog2 = Dog('chino', 2015, 'japanese chin')
# dog3 = Dog('fido', 2018, 'doberman')

# print(dog1)
# # print(dog1.human_age())
# print(dog2.human_age())

# # print(dog1)
# # print(dog2)
# # print(dog3)

# # Human age
# print(dog1.human_age())

# # testing call from another function

# print(dog1.show_results_from_another_function())
# print(dog2.show_results_from_another_function())
# print(dog3.show_results_from_another_function())


# # dog years for dog
# print(dog1.dog_years())

# # today = datetime.datetime.now()
# # year = today.year
# # month = today.month
# # day = today.day
# # print(year)
# # print(month)
# # print(day)

