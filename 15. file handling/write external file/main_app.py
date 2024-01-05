## write external file

# 1. write mode

# print("="*3,"Membaca file txt ","="*3)
# with open("15. file handling/write external file/data.txt",mode="w",encoding="utf-8") as file:
#     file.write("Andi")
# with open("15. file handling/write external file/data.txt",mode="w",encoding="utf-8") as file:
#     file.write("Budi")
# with open("15. file handling/write external file/data.txt",mode="w",encoding="utf-8") as file:
#     file.write("Candra")

'''
when mode write file is overwrite
'''

# 2. append mode
# print("="*3,"Membaca file txt ","="*3)
# with open("15. file handling/write external file/data.txt",mode="w",encoding="utf-8") as file:
#     file.write("Andi,")
# with open("15. file handling/write external file/data.txt",mode="a",encoding="utf-8") as file:
#     file.write("Budi,")
# with open("15. file handling/write external file/data.txt",mode="a",encoding="utf-8") as file:
#     file.write("Candra,")
# with open("15. file handling/write external file/data.txt",mode="r",encoding="utf-8") as file:
#     content = file.read()
#     print(content)


# 3. r+ mode
print("="*3,"Membaca file txt ","="*3)
with open("15. file handling/write external file/data.txt",mode="w",encoding="utf-8") as file:
    file.write("Andi,")
with open("15. file handling/write external file/data.txt",mode="a",encoding="utf-8") as file:
    file.write("Budi,")
with open("15. file handling/write external file/data.txt",mode="a",encoding="utf-8") as file:
    file.write("Candra,")
with open("15. file handling/write external file/data.txt",mode="r",encoding="utf-8") as file:
    content = file.read()
    print(content)
