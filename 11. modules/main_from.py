# input using "from <module> import <function> "

# import one function
# from mathematics import plus

# import several functions 
from mathematics import add,multiply
from mathematics import exponent as exp # import using alias

# import all function
# from mathematics import * 


result_add = add(1,2,3,4,5,6,7,8)
result_multiply = multiply(5,5)
result_exponent = exp(7,2)

print(result_add)
print(result_multiply)
print(result_exponent)