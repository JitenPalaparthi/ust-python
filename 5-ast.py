import ast 

source= "x = (2 + 3) * 4"

# docstring if the string is in multiple lines, then give it with in """ some string """
source = """
age,gender = 18,'m'

print(age>=18 and (gender=='F' or gender=='f'))

if age>=18 and (gender=='F' or gender=='f'):
    print("she is eligible for marriage becase the age is",age)
elif age>=21 and (gender=='M' or gender=='m'):
    print("He is eligible for marriage, bcz age is",age)
else:
    print("not eligible for marriage")
"""

tree = ast.parse(source)

print(ast.dump(tree,indent=4))