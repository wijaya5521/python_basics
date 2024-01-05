## read external file

from os import replace


# print("="*3,"Membaca file txt ","="*3)
# file = open("15. file handling/read external file/data.txt",mode="r",encoding="utf-8")

# print(f"status read :  {file.readable()}") # check is file readable?
# print(f"status read :  {file.writable()}") # check is file writable?

# read file data.txt
# print(file.read())

# read file row by row
# print(file.readline(),end="") 
# print(file.readline(),end="") 
# print(file.readline(),end="") 

# read file all rows as list
# print(file.readlines())

# close file
# print(f"is file closed : {file.closed}")
# file.close() # close file
# print(f"is file closed : {file.closed}")

## other way to open file use with()
print("="*3,"Membaca file txt ","="*3)
with open("15. file handling/read external file/data.txt",mode="r",encoding="utf-8") as file:
    content = file.readline()
    print(content.split(","))
print(f"is file closed : {file.closed}")

