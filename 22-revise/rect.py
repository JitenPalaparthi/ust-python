class Rect:

    # classlevel attribute
    shape="Rectangle"

    # constructor
    def __init__(self,l,w):
        self.length  =l  # object level attributes
        self.width = w # object level attributes
    
    # alternate constrtuctor
    @classmethod
    def from_defaults(cls):
        return cls(1.0,1.0)
    
    # method
    def area(self):
        return self.length * self.width

    # method
    def perimeter(self):
        return 2 *(self.length+self.width)
    

r1 = Rect(100.12,123.2)

a1,p1=r1.area(),r1.perimeter()

print("Area of rect r1:",a1,"\nperimeter of rect r1:",p1)

r2= Rect.from_defaults()

a2,p2 = r2.area(),r2.perimeter()

print("Area of rect r2:",a2,"\nperimeter of rect r2:",p2)


