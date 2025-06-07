# import shapes
# import shapes.circle
# import shapes.triangle

# circle1= shapes.circle.Circle(12.12)
# triangle1= shapes.triangle.Triangle(123.123,232.23)

# area1,perimeter1= circle1.area(),circle1.perimeter()
# area2= triangle1.area()
# print(f"area of circle:{area1:.2f}\nperimter of circle:{perimeter1:.2f}")
# print(f"area of triangle:{area2:.2f}")

from shapes import Circle
from shapes import Triangle

circle1= Circle(12.12)
triangle1= Triangle(123.123,232.23)

area1,perimeter1= circle1.area(),circle1.perimeter()
area2= triangle1.area()
print(f"area of circle:{area1:.2f}\nperimter of circle:{perimeter1:.2f}")
print(f"area of triangle:{area2:.2f}")
