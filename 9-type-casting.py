# type casting and type conversion

x = 123  # int
y = 54.34 # float

z = x + y  # implicit type casting

print(z)

x = "123" # str
y = 87.34 # float

z = int(x)+y 

print(z)

s = 123 # int

print(type(str(s)))

pi=3.14 # float

intpi = int(pi) # converting it to int, so it losses the decimal value

print(intpi)

print(bool(1))
print(bool("True"))
print(bool("Yes"))

print(bool(0))
print(bool(False))
print(bool(""))


# print(isinstance(intpi,str))

a,b = "123.123k",98.23

if isinstance(a,(int,float)) and isinstance(b,(int,float)):
    print(a+b)
else:
    try:
        print(float(a)+float(b))
    except ValueError:
        print("invalid input") # why invalid input, bcz it tried to convert but failed
        print("cannot perform arithmetic operation on non")
