'''
import mathematics folder from science folder
import science.mathematics

or you can use
from science import mathematics
'''

''' or import specific function '''
from science.mathematics import add,substract,multiply,exponent,factorial

print(add(1,2,3,4))
print(substract(1,2,6,7))
print(multiply(1,2,6,7))
print(exponent(11,2))
print(factorial(7))