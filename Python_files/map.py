# map, filter, reduce in python


def cube(x):
    return x**3



l = [ 1,2,3,4,5,6]

newlist = map(cube,l)
print(list(newlist))


# is vs '=='
# is checks for the same object in memory
# '==' checks for the value of the object

