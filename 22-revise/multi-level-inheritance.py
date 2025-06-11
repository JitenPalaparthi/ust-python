

"""
Multi-Level Inheritance
Animal
  |
Mammal
  |
 Dog
  |
 Pug
"""

class Animal:

    def __init__(self,name):
        self.name=name
    
    def speak(self):
        print(f"{self.name} is an animal")


class Mammal(Animal):

    def __init__(self,name,is_warm_blooded=True):
        super().__init__(name)
        self.is_warm_blooded=is_warm_blooded
    
    def speak(self):
        super().speak()
        print(f"{self.name} is an animal. Warm Blooded:{self.is_warm_blooded}")

class Dog(Mammal):

    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    
    def speak(self):
        super().speak()
        print(f"{self.name} is dog of breed {self.breed}")


class Pug(Dog):

    def __init__(self,name):
        super().__init__(name,breed="Pug")
        
    def speak(self):
        super().speak()
        print(f"{self.name} is a cute Pug")
    
puggy = Pug("Puggy")
puggy.speak()
