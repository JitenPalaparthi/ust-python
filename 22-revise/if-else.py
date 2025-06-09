try:
    age = int(input("enter age: "))

    if age>=18:
        print("eligible for vote")
    else:
        print("not eligible for vote")
except ValueError :
    print("enter valid value. Re-run the application with valid value")
