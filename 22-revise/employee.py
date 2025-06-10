class Employee:
    # Class Level variable/attributes
    # Object attributes
    # Class Methods

    Company="UST Global" # Class level attribute

    # constructor is used to construct or create an object

    def __init__(self,name,email,mobile):
        self.name=name
        self.email=email
        self.mobile=mobile
    
    def greet():
        print("Hello there!")
    
    def say_hi(self):
        print("Hello there!")
    
    def print_details(self):
        print("Company:",Employee.Company)
        print("Name:",self.name,"\nEmail:",self.email,"\nMobile:",self.mobile)
    
    # alternative constructor
    @classmethod
    def create_employee(cls,name,email,mobile:str=None):
        return cls(name,email,mobile)

Employee.greet()
emp1 = Employee("Jiten","JitenP@Outlook.Com","9618558500")# the constructor

emp1.say_hi()
emp1.print_details()
print()
emp2= Employee.create_employee("Jiten","Jiten.Palaparthi@Gmail.com")
emp2.print_details()
