# no array in python there is a list 

# ordered
# mutable 
# duplicate values in the list 

mylist= [10,20,30,40,50,50,40,30,20,10]
print(mylist[5])

sum=0

for v in mylist:
    sum+=v

print("sum=",sum)

mylist.append(100) # appends to the list

print(mylist)
mylist.remove(50) # removes the fist occurance in the lsit 
print(mylist)
print(len(mylist)) # prints the len of the list
mylist.sort() # sorts the list 
print(mylist)
mylist.insert(5,200) # inserts at a index
print(mylist)

matrix2d = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2d[0][2]=300


for row in matrix2d:
    for item in row:
        print(item," ",end="")

list3d=[
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
]

print()
for list in list3d:
    for row in list:
        for item in row:
            print(item," ",end="")
