# prime number or not 
num = input("enter a number ")
try:
    num = int(num)
    if num<=1:
        print(num,"is not a prime number")
    else:
        count=0
        for i in range(1,num+1):
            if num%i==0:
                count+=1
        if count==2:
            print(num,"is prime number")
        else:
            print(num,"is not a prime number")
except ValueError:
    print("invalid number")

# if isinstance(num,int):
#     print(num)
# else:
#     print("invalid number")