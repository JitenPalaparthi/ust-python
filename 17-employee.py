class Employee:

   # """This is a class that represents employee"""
    company = "UST Global" # it is a class level variable

    # constructor --> 

    def __init__(self,name,position,salary):
        # initialize employee variables , instance attributes
        self.name = name 
        self.position= position
        self.salary=salary 
        self.years_of_service=0 # default value
    
    def give_raise(self, amount):
        self.salary += amount # self.salary = self.salary+amount
        return f"{self.name}'s new salary is ${self.salary}"
        #return "employee's new salary is $1000"


emp1 = Employee("Jiten","Developer",37000) # emp1 is an object of type Employee
emp2 = Employee
print("name",emp1.name,"salary:",emp1.salary,"company:",emp1.company,"position:",emp1.position,"service",emp1.years_of_service)

emp1.give_raise(1200)
print("name",emp1.name,"salary:",emp1.salary,"company:",emp1.company,"position:",emp1.position,"service",emp1.years_of_service)

print("name",emp2.name,"salary:",emp2.salary,"company:",emp2.company,"position:",emp2.position,"service",emp2.years_of_service)
print("company:",emp2.company)

# create a class called animal and give few attributes to animal,may be a dog
# name,breed , age as the instance attribures
# type is dog which is a class level varible
# create a method called speak (just write it is barking)
