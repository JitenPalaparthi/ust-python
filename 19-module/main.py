# main.py

# from mymodule import Circle

# circle1 = Circle(12.3)

# area = circle1.area()
# perimter= circle1.perimeter()

# print("area of circle1:",area)
# print("perimeter of circle1",perimter)

import mymodule

circle1= mymodule.Circle(12.23)
area = circle1.area()
perimeter= circle1.perimeter()

formatter = f"area of circle1:{area:.2f}"
print(formatter)
print(f"area of circle1:{area:.2f}")
print("perimeter of circle1",f"{perimeter:.2f}")

triangle1= mymodule.Triangle(12.2,32.3)

area = triangle1.area()

print("area of triangle1:",area)





