class Person:
    
    def __init__(self,name,age):
        self.name=name
        self.age = age 
    
    def display_personal_info(self):
        print(f"Name;{self.name} Age:{self.age}")


class Worker:

    def __init__(self,job_title,salary):
        self.job_title=job_title
        self.salary=salary
    
    def display_work_info(self):
        print(f"Job Title:{self.job_title} Salary:{self.salary}")


class Employee(Person,Worker):

    def __init__(self,name,age,job_title,salary):
        Person.__init__(self,name,age)
        Worker.__init__(self,job_title,salary)

    def display_full_info(self):
        self.display_personal_info()
        self.display_work_info()
    
    def welcome(self):
        print("Welcome to the office")

emp = Employee("Jiten",40,"Architect",1233.23)
emp.display_full_info()

#emp.welcome()