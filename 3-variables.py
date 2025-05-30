# variables

# traditional swap
a,b = 10,20 
t = a
a = b 
b = t
d = a
print("a=",a,"b=",b)
print("address of a:",id(a),"address of b:",id(b),"address of d:",id(d))

# easy swap in python
a,b = 10, 20 
print("a=",a,"b=",b)
a,b = b,a 
print("a=",a,"b=",b)
print("address of a:",id(a),"address of b:",id(b))

# arithmetic operations

a = 10 
b = 13.5


c = a+b 
print("c=",c)

c = a-b * 10 / 2 

print("c=",c)

c = (a+b)**2*(a/2) # ** exponentation
# 23.5**2*5
# 552.25 * 5
# 2761.25
print("c=",c)
# precedence
# (), ** , +x,-x,~x, * , / ,//,% ,+,-, <<,>>,&,
print("div=",13/2,"floor div",13//2,"mod=",13%2)

ok1 = True 
ok2 = False 

ok3 = ok1 or ok2 and 100>99 ## This is a logical and comparision expression
# True and True
# True
print(ok3)

