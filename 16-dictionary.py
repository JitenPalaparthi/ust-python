# unordered, mutable , and index collection of key-value pairs 

print(hash("Jiten"))
print(hash("Anil"))
print(hash("Rekha"))

# sha --> Secured Hashing Algorithms
# dictionaries are called as hashmaps

person = {
    "name":"jiten",
    "age":40,
    "city":"Trivandrum"
}

try:
    print(person["salary"])
except KeyError as k:
    print("the key-->",k,"does not exist")


if "salary" in person:
    print(person["salary"])
else:
    print("the key-->does not exist")


print(person["name"])

# loop for dictionary gives key and value
for key,value in person.items():
    print(key,"-->",value)

# what can be a key --> which ever the type can use immutable, hashable function can be a key

# buckets --> keys and values (two parallexl arrays, each bucket contains 8 elements)
# 2 --> 2 to the power of 
# load factor --> 66% , when the number entries/buckets > 66% the buckerts are doubled
# but it rebalances all the elements across the newly created buckets 

# hash -> generally, takes the key and applies the hash function and gives a number which is nothing but the bucket number

# some algorthims , split the key(hash) -> segment and offset 

# overflow bucckets -> Linked list is used 
# collisions 

# Ubuntu Image -- docker 
# Few layers (Image Layers )

# Postgres Ubuntu -> Layer-1, Layer-2, Layer-3
# MySql Ubuntu 
# Kafka Ubuntu 
