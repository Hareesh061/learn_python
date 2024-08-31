# local and global variable in python       
# local variable is defined inside a function and is not accessible outside the function
# global variable is defined outside a function and is accessible inside the function
# we can modify the global variable inside the function but we need to use the global keyword
# we can't modify the local variable inside the function


x = 3
print(f"global variable is:{x}")

def global_fun():
    x = 8
    print(f"local variable is:{x}")


global_fun()
print(f"global variable is:{x}")


