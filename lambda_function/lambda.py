# Lambda Function

# regular function
def quadratic_function(number):
    return number**2

print(f"Resut of quadratic function = {quadratic_function(4)}")

# lambda function
# output = lambda argument: expression
quadratic_function = lambda number:number**2
print(f"Hasil fungsi kuadarat = {quadratic_function(5)}")


exponent = lambda num,pow:num**pow
print(f"Result of exponent = {exponent(5,3)}")

# example of lambda function

# sorting regular list (based on alphabetic order)
data_list = ["wijaya","rey","yuji"]
data_list.sort()
print(f"Sorted list = {data_list}")

# sorting based on length of the name using regular function
def name_length(name):
    return len(name)

data_list.sort(key=name_length)
print(f"Sorted list by length = {data_list}")

# sorting based on length of the name using lambda function
data_list = ["wijaya","rey","yuji"]
data_list.sort(key=lambda name:len(name))
print(f"Sorted list by length = {data_list}")
