# if as expression using ternary operator kind of 

num = 24 
result= None

if num%2==0:
    result="even"
else:
    result="odd"

print(result)
num = 37

# same as above but writing ternary operator code 

result= "even" if num%2==0 else "odd" # ternary operator 

print(result)

marks = 85 

grade = "A" if marks>=95 else "B" if marks>=85 else "C"

print(grade)

marks= 67
# same as above but writing normal code
if marks>=95:
    grade = "A"
else:
    if marks>=85:
        grade="B"
    else:
        grade="C"

print(grade)
