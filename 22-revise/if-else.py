try:
    age = int(input("enter age: "))

    if age>=18:
        print("eligible for vote")
    else:
        print("not eligible for vote")
except ValueError :
    print("enter valid value. Re-run the application with valid value")

a,b=(10,20.1)

print("c=" , {a+b})
print ("c=", int(a+b)) # when you cast float to int, you lose data..
# 100 -->

print(bin(100))

# 64 bit floating point number
# 1  --> Sign bit 
# 11 --> Exponent bits 
# 52 --> Mantissa or a fractional part
