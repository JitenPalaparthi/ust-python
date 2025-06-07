
with open("materials/1-what_is_python.md","r") as file:
   lines = file.readlines()
   for line in lines:
      print(line,end="")