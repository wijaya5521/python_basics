# global & local scope
global_name= 'Wijaya' # this is global variable

# access global variable
def show_name():
    print(f"Your name is : {global_name}")

show_name()

# acces global variable using loop    
for i in range(1,5):
    print(f"loop {i} : {global_name}")
    
def local_name():
    name_local = "riyan" # this is local variable
    
# print(name_local) # you can not access local variable

def change_name(name):
    global global_name
    global_name= name
    print(f"Your current name is : {global_name}")
    
print(f"Your old name is : {global_name}")
change_name("Riyan")
     
