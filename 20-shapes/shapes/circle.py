import math

class Circle:

    #PI = 3.14 # by convenction it is a class level variable and think it as a constant

    def __init__(self,r):
        self.r=r

    def area(self):
        return math.pi*self.r * self.r
    
    def perimeter(self):
        return 2 * math.pi * self.r