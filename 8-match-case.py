# match case is there in python from version 3.10

day = 4

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

