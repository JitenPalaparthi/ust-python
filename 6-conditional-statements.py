# if-else elif in python

num = 100

if num%2==1:
    print(num,"is a odd number")
else:
    print(num,"is an even number")

# what does if want? if is followed by an expression which ultimately yeilds true or false

# num,div = 100 , 2 

# if  num%2==0 and div %2==0:
#     print("yes it is true")
# else:
#     print("yes it is False")


age,gender = 18,'m'

print(age>=18 and (gender=='F' or gender=='f'))

if age>=18 and (gender=='F' or gender=='f'):
    print("she is eligible for marriage becase the age is",age)
elif age>=21 and (gender=='M' or gender=='m'):
    print("He is eligible for marriage, bcz age is",age)
else:
    print("not eligible for marriage")

# using not

ok = True

if not ok:
    print("False")
else:
    print("True")

a,b = 10,10

if not (a==b):
    print("a and b are different",a,b)
else:
    print("a and b are same",a,b)



a,b = 10,20

if a is b:
    print("True")
else:
    print("False")

a = None 

if a == None:
    print("Yes, a is None")