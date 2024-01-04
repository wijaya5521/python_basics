# mathematics modules

def add(*args):
    result = 0
    for data in args:
        result += data
    return result

def multiply(*args):
    result = 1
    for data in args:
        result *= data
    return result

def exponent(number,n):
    exponentOf = lambda number,n:number**n
    return exponentOf(number,n)