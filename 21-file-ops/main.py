# Mode Description
# 'r'  Read (default mode)
# 'w'  Write (overwrites file)
# 'a'  Append (adds to file)
# 'x'  Create (fails if file exists)
# 'b'  Binary mode (e.g., 'rb', 'wb')
# 't'  Text mode (default)
# 'r+'  Read and Write mode
# 'a+'  Append and Read mode
# 'w+'  Write and Read mode

# file = open("data.txt",'a')

# try:
#     file.write("Hello UST Global!\n")
# except FileNotFoundError:
#     print("file not found")

# file.close() # if you dont close , you are not clearin resources

with open("data.txt",'a') as file:
    file.write("Hello UST Global!\n")


with open("data.txt",'r') as file: # using with notation , no need to close the file, which is automaticaly done by the system
    content= file.read()
    print(content)