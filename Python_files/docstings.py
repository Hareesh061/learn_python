# doc stings in python
# docstrings are used to document python modules, functions, classes, and methods.
# they are used to provide information about the purpose and usage of the code.
# docstrings are typically written in triple quotes """ """ and are placed at the top of a module
# or function definition.
# docstrings can be accessed using the __doc__ attribute of a module or function.


def square(n):
    '''takes a number, do the square operation, prints result'''
    print(n**2)

square(5)

print(square.__doc__)
