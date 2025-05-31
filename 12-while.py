# while loop


count=1 
while count<=10:
    if count%2==0:
        print(count," ",end="")
    count+=1
else:
    print("loop exits",count)

print("")

count=1
while True:
    if count==51:
        break
    if count%2==0:
        print(count," ",end="")
    count+=1


print("loops outer and inner, to break using done")
count=0
done=False
for i in range(1,6):
    if done:
        break
    for j in range(1,6):
        if i==3:
            done=True
            break
        print("i",i,"=>","j",j)
        count+=1
print(count)


def outer_loop():
    count=0
    for i in range(1,6):
        for j in range(1,6):
            if i == 3:
                return
            print("i",i,"=>","j",j)
            count+=1
        print(count)

outer_loop()

# print("loops outer and inner, to break using done")
# count=0
# outer:
# for i in range(1,6):
#     for j in range(1,6):
#         if i==3:
#             break outer;
#         print("i",i,"=>","j",j)
#         count+=1

# print(count)