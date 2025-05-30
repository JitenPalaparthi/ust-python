# variable is a name refers to the memory location
# every value in python is an object

# numbers --> whole numbers, decimal numbers 

# string --> collection of characters

# boolen -> true or flase 

# character --> single unicode character

import sys

x = 100
print("Size of x",sys.getsizeof(x),"Value of--> ",x)


y = 200.34
print("Size of y",sys.getsizeof(y),"Value of--> ",y)


str1="Hello World"
print("Size of str1",sys.getsizeof(str1),"Value of--> ",str1)


ok1 = True 
print("Size of ok1",sys.getsizeof(ok1),"Value of--> ",ok1)

char1 = 'A'
print("Size of char1",sys.getsizeof(char1),"Value of--> ",char1)

char2 = '✅'
print("Size of char2",sys.getsizeof(char2),"Value of--> ",char2)

N = None # No value 
print("Size of N",sys.getsizeof(N),"Value of--> ",N)
 
count = 100 # This count is a global variable 

def increment(): # declaring and implementing a func
    #count=1 ## creating a new variable 
    global count # global keyword tells python use the global varaible called count
    count +=1 # performing an arithmetic operation

increment() ## calling the function
print("Count=",count) # print the value count after the function call 


# a process contains some memory
# Code Segment
# Data Segment --> static variables , uninit global variables , constants are stored.
# Stack Memory --> 2mb
# Heap Memory --> as much as you want, provided by sufficient memory available 


# every object in python contains
# type information
# reference count
# memory management overhead
# actual value