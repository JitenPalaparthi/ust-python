# 1. Create three variables a,b,c and swap values
a,b,c = 10,20,30 

a,b,c = c,a,b 

print("a:",a,"b:",b,"c:",c)

# 2. create a string and try to add a char to the string 

str1 = "Hello World"
char1='!'

print(str1+char1)

# 3. create two tuples t1 = (1,2,3) t2 =(1.1.,2.2,3.3)


t1 = (10,20,30)
t2 = (10.1,20.2,30.3)

t3 = t1+t2 # add of a tuple is not add of a numbers
print("tuple to tuple addition t3:",t3)


z=zip(t1,t2)# [(10,10.1),(20,20.3),(30,30.3)]

t3= tuple(a+b for a,b in zip(t1,t2))

print("element addition of t3:",t3)

