# sets in python 
# set is an unordered collection of unique elements
# set is mutable
# set is iterable


set = {2,3,2,8}
print(set)


#empty set


s = set()
print(type(s))


# set methods in pythons
#issuperset()
#issubset()
# add() - adds an element to the set
# discard() - removes an element from the set if it is a member
# remove() - removes an element from the set if it is a member
# pop() - removes and returns an arbitrary set element
# clear() - removes all elements from the set
# union() - returns a set with elements from the first set, that are not in the second
# intersection() - returns a set with elements common to the set and the other set
# difference() - returns a set with elements in the set and not in the other set
# symmetric_difference() - returns a set with elements in either the set or the other set, but
# not both



set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.pop())
set1.clear()
print(set1)



