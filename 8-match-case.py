# match case is there in python from version 3.10

day = 4
# num=100
# if type(num) is bool:
#              print(num,"is bool")
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("no day")


point = (-10,12)
match point:
    case (0,0):
        print("The origin")
    case (0,y):
        print("Y-Axis is",y)
    case (x,0):
        print("X-Axis is",x)
    case (x,y):
        print("X-Axis is",x,"y-Axis",y)
    case _:
        print("invalid point")

num = True
match num:
    case int():
        if type(num) is bool:
             print(num,"is bool")
        else:
            print(num,"is int")
    case float():
         print(num,"is float")
    case str():
         print(num,"is string")
    case bool():
         print(num,"is bool")
    case _:
        print("not int,float,string or bool")