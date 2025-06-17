class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display_person_info(self):
        print(f"Person name: {self.name} \n Age: {self.age}")

class Student(Person):

    def __init__(self, student_id,grade):
        self.student_id=student_id
        self.grade=grade
    
    def display_student_info(self):
        print(f"Student ID:  {self.student_id} \n Grade: {self.grade}")

class Teacher(Person):

    def __init__(self, teacher_id, subject):
        self.teacher_id=teacher_id
        self.subject=subject

    def display_teacher_info(self):
        print(f"Teacher: {self.teacher_id} /n Subject: {self.subject}")

class TeachingAssistant(Student):

    def __init__(self, name, age):
        super().__init__(name, age)

p1=Person("Sam","30")
s1=Student("101","A")
p1.display_person_info()
s1.display_student_info()