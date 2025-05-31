
greet = "Hello UST Global Folks!" # greet is string which is nothing but collection of chars

revstr=""

for c in greet:
   # print(c, "-->")
   revstr=c+revstr # this concatination

print(revstr)

# i from 0 to 100
for i in range(100):
   i = i+1
   if i % 2 ==0:
      print(i," ",end="")

print()

print("using continue")


for i in range(100):
   i=i+1
   if i % 2 == 0:
      continue
   else:
      print(i, " ",end="")

print("\nusing break statement")

for i in range(1000):
   if i==100:
      break # break breaks the whole loop
   else:
       if i % 2 == 0:
        continue
       else:
         print(i, " ",end="")

