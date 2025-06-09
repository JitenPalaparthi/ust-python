for i in range(1,10):
    print(i)

fruits = ["Mango","Banana","Orange","Jackfruit","Water Milan"]

for fruit in fruits:
    print(fruit)

# 1 1 2 3 5 8 13 21 34 55

i = 1
a,b = 0,1
while True:
    if i>20:
        break
    print(a)
    a,b = b , a+b
    i+=1

print("duplicate numbers")
list = [1,2,3,4,5,6,3,4,5,6,3,3,3,7,9,11,12,6,6,6,6,6,6,6,6]

counts = {} # dictionary , they key and the value


for num in list:
    if num in counts: # if it is a key in the dictionary
        counts[num]+=1
    else:
        counts[num]=1
       
for num in counts:
    if counts[num]>1:
        print(num, "is duplicate for times",counts[num])


list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
list3 = list2 # memory copy
print("list1->",id(list1),"\nlist2->",id(list2),"\nlist3->",id(list3))
if list1 == list2: # it equals the values
    print("list1 and list2 are equal")
else:
    print("list1 and list2 are different")

if list1 is list2:
    print("list1 and list2 are same")
else:
    print("list1 and list2 are different")

if list2 is list3:
       print("list3 and list2 are same")
else:
    print("list3 and list2 are different")



