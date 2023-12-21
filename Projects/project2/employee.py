import datetime # import datetime module to calculate years worked

# Project 2 - Robin Maynard - 12/22/23

'''Project 2 - First Draft (Employee Class)
Due December 22, 2023 11:59 PM
Instructions
Following the steps outlined in class and in the slides, you should have a functioning Employee Class

Define your class and include your constructor with any necessary attributes.
Create your string method to display your employee data 
Define a method for a total_expense() function 
Accessor and mutator methods (get and set) for all attributes. 
Test organize and document your class'''

# Define Employee Class including constructor and attributes.

class Employee:
 # document constructor
    def __init__(self, name, job_title, department, salary, hire_year):
         self.name = name
         self.job_title = job_title
         self.department = department
         self.salary = salary
         self.hire_year = hire_year
        
# Create string method to display your employee data

    def __str__(self):
         return f'Name: {self.name}\nJob Title: {self.job_title}\nDepartment: {self.department}\nSalary: {self.salary}\nHire Year: {self.hire_year}'
    
# Define a method for a years_worked() function

    def years_worked(self):
         today = datetime.datetime.now()    # I'm using the datetime module to get the current year so that we can subtract the hire year to get the years worked
         year = today.year
         return int(year) - int(self.hire_year)
    

# Define a method for a total_expense() function

    def total_expense(self):
        totalexpense = int(self.salary) * self.years_worked()   # I'm using the output from years_worked() function to calculate total expense.
        return f'Employee Name: {self.name}\nEmployee Total Expense: ${totalexpense}'
    
    def total_employee_record(self):
        totalemployeerecord = f''


    # # Accessor Methods - returns an attribute to the user
    def get_name(self):
         return self.name
    
    def get_job_title(self):
         return self.job_title
    
    def get_department(self):
         return self.department
    
    def get_salary(self):
         return self.salary
    
    def get_hire_year(self):
         return self.hire_year
    
     # # Mutator Methods - lets the user change the attribute
    def set_name(self, new_name):
       self.name = new_name

    def set_job_title(self, new_job_title):
       self.job_title = new_job_title

    def set_department(self, new_department):
       self.department = new_department

    def set_salary(self, new_salary):
       self.salary = new_salary

    def set_hire_year(self, new_hire_year):
       self.hire_year = new_hire_year

# testing print statements for employees
        
employee_a = Employee('Fred Smith', 'Developer', 'Information Technology', '58000', '1999')
employee_b = Employee('Rob Roberts', 'Representative', 'Customer Service', '53000', '2015')
employee_c = Employee('Bob Burns', 'Analyst', 'Operations', '55000', '2020')

# Printing each employee's data

print(employee_a)
print(employee_a.total_expense())
print(employee_b)
print(employee_b.total_expense())
print(employee_c)
print(employee_c.total_expense())






# Accessor and mutator methods (get and set) for all attributes.




# Test organize and document your class



# git add . (what do I want to include in my next commit)
# git commit -m"This is what I am doing" (captures your current changes before pushing)
# git push (upload local repo to a remote repo)
# git pull (fetches content from remote repo and updates your local repo to match)