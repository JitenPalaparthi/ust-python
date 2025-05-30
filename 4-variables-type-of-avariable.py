# How to know the type of a variable

x = 10 
y= 10.4 
s ="Hello World"
c = 'A'
d= True 
e =None

print(type(x))
print(type(y))
print(type(s))
print(type(c))
print(type(d))
print(type(e))

print(isinstance(x,int))

# f = x + s # what kind of error this is 
# print("f=",f)

# create a tuple 

t1 = (100,"Hello World",True)
# typle is immutable, so neither increase its size nor change value with index
# t1[0]=200
# t1[1]="Hello UST Global Folks"
# t1[2]=False
#t1[3]=12321

print("tuple t1:",t1[0],t1[1],t1[2])

t2 = 100, "Hello World",True

print("tuple t2:",t2[0],t2[1],t2[2])

t3,t4, t5 = t1 #(100, "Hello Wrold",True) # _ blank identifier
print("t3:",t3)
t3 = 200
print("t3:",t3,"t4:",t4,"t5:",t5)
#print(t1[0])

t1 = ()
t2 = (10,)

v1,v2 = t2 

print(type(v1),type(v2))


print(t1,t2)