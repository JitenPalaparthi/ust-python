set1 = {10,20,30,40,50}
#set1[0]=100 # cannot access the set thru an index

# 1. set is not ordered 
# 2. 

set1.remove(40)
set1.add(60)
print(set1)

if 20 in set1:
    print("20 is exist")
else: 
    print("20 does not exist")

for value in set1:
    print(value)


set1 = {10,20,30,40,50}
set2 = {40,50,60,70,80}

print(set1.union(set2))
print(set1.intersection(set2))

set3 = {"apple","banana","mango"}
set4 = {"peach","dragonfruit","watermilon"}
print(set3.union(set4))
print(set3.intersection(set4))

print(set3 | set4) # union

print(set3 & set4) # intersection

print(set3.symmetric_difference(set4))
print(set3 ^ set4) # symmetric_difference
# symmetric_difference --> it removes the common elements(intersection) and gives result
A = { 1,2,3,4}
B = { 3,4,5,6}

print(A ^ B)

normalset1 = set([1,2,3])
frozenset1 = frozenset([1,2,3])
normalset1.add(100)
#normalset1[0]=100
print(normalset1)
frozenset1.add(100)




