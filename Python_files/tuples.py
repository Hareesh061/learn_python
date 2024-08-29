# typles in python- we cant change the values of tuples

tup = (1,2,3,4,"hai")
print(type(tup),tup)

# methods in tuples- if you want to make changes like adding,sort,reverse in tuples you must convert tuple into list first.


tup = (2,4,5,2,3)

temp = list(tup)
print(temp)
temp.sort()

tup = tuple(temp)
print(tup)


tup=(3,4,3)
temp = tup.count(4)
print(temp)