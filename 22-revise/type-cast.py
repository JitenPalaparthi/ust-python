def sum_of(a,b):
    return a+b

x = 100 # x is a variable that is stored in stack , ref that is in the heap(100)
print("1.id x:" ,id(x))
z = x  
x = x+z
print("2.id z:",id(z))
print("3.id x:" ,id(x))

y = float(x)

r1= sum_of(x,y)

# 
x = 100.1233 # (100.1233)
print("4.id x:",id(x))


y = int(x)
print(y)

r2= sum_of(x,y)

try:
    s ="123.123q"
    f1 = float(s)
    print(f1)
except ValueError as e:
    print(e)

list=[123,123.23,32,True,"Hello"]

sum = float(0)

for item in list:
    if isinstance(item,(int,float)): # checking whether intem is int,float
        sum+=item


print("sum=",sum)

for item in list:
    match type(item): # this is going to match the type of a vaiable
        case "int":
            sum+=item
        case "float":
            sum+=item
        case _: #default , black identifier _ is considered as a default case in python
            pass


