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
    
    def area_of(r):
        return r.l * r.b



rect1 = Rect(10.12,12.34)
rect2 = Rect(100.12,123.34)

a1=Rect.area_of(rect1)
print("area of rect:",a1)

# rect1.area_of


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

### 

def area_of_rect(l,b):
    return l *b

a1 = area_of_rect(12.12,23.45)
print("area of rect a1:",a1)


def sum_of(list):
    sum = 0 # local variable created here
    for l in list:
        sum+=l
    return sum # return 


list = [1,2,3,54,65,76,34]
s = sum_of(list)
print(s)




