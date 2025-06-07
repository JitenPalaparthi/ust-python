# mymodule.py

class Circle:

    PI = 3.14 # by convenction it is a class level variable and think it as a constant

    def __init__(self,r):
        self.r=r

    def area(self):
        return Circle.PI*self.r * self.r
    
    def perimeter(self):
        return 2 * Circle.PI * self.r


class Triangle:

    def __init__(self,b,h):
        self.b =b 
        self.h=h
    
    def area(self):
        return .5 * self.b * self.h
    



