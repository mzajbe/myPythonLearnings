# Python - Join Sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}


set3 = set1.union(set2)
print(set3)

# You can use the | operator instead of the union() method, and you will get the same result.

# set4 = set1 | set2
# print(set4)


# Join multiple sets with the union() method:
mySet = set1.union(set2, set3, set4)
print(mySet)


# The union() method allows you to join a set with other data types, like lists or tuples.
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)



set1.update(set2)
print(set1)
# Note: Both union() and update() will exclude any duplicate items.