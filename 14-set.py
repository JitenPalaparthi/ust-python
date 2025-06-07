# a set is unorderd ,mutalbe collection of unique elements

list1 = [1,2,3,4,5,5,4,3,2,1]
set1 =  {1,2,3,4,5,5,4,3,2,1}

print(set1)
print(list1)

set2 = set([1,2,3,4,5,5,4,3,2,1]) # create a set using a constructor
print(set2)

set2.add(7)
try:
    set2.remove(20)
    print(set2)
except KeyError:
 print("Key not found")



def divide(a,b):
   if b==0:
      raise ValueError("divide by zero error")
   else:
        return a/b
   
try:
    divide(200,0)
except ValueError as e:
   print("wrong value-->:",e)


# Errors in Python

# ValueError --> Wrong type of value
# TypeError  --> Wrong type
# KeyError --> Missing key in a dict
# IndexError --> Index out of range in a list or set
# RuntimeError --> Generic error in the logic
# FileNotFoundError --> When is not found and performing operatoins on a file which does not exist
# AssertionError --> Manual checks with assert
# AttributeError --> An object does not contain the attribute