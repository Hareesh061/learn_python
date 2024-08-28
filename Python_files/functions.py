#functions in pythons - 1. build in function 2. user defined function

def addNumber(a,b):
    sum= a+b
    print(sum)

def bigNum(a,b):
    if(a>b):
        print("a is greater")
    else:
        print("b is bigger")
    

a = int(input("enter number a: "))
b = int(input("enter number b: "))

addNumber(a,b)
bigNum(a,b)

# function arguments and return statement- 1. default arguments 2. keyword arguments 3. required arguments



