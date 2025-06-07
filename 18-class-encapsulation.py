class Rect:

    shape = "rect"

    def __init__(self,l,b): 
        self.l = l
        self.b = b
        self.__a= None # do it by convenction
        self.__p =None # it is by convenction

    def what():
        return Rect.shape

    def __calculate_area(self): # it is private 
        self.__a = self.l *self.b

    def __calculate_perimeter(self): # it is private method
        self.__p = 2 * (self.l +self.b)

    def area(self):
        self.__calculate_area()

    def perimter(self):
        self.__calculate_perimeter()


rect1 = Rect(10.12,12.34)

a1=rect1.area()

print("area of rect:",a1)

p1= rect1.perimter()
print("perimeter of rect:",p1)


print("length:",rect1.l)
print("breadth:",rect1.b)

try:
    print("area:",rect1.__a)
    print("perimeter:",rect1.__p)
    a2= rect1.__calculate_area() # cannot call becase __calculate_area is private
    p2 = rect1.__calculate_perimeter()
    print("area of rect:",a2)
except AttributeError as a:
    print("some thing went wrong",a)

print("hello end of this program")






