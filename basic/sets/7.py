# Intersection

# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry","x"}
set2 = {"google", "microsoft", "apple","x"}

set3 = set2.intersection(set1)
print(set3)

# You can use the & operator instead of the intersection() method, and you will get the same result.

set3 = set1 & set2
print(set3)

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

set1.intersection_update(set2)

print(set1)


# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

setx = {"apple", "banana", "cherry"}
sety = {"google", "microsoft", "apple"}

setz = setx.difference(sety)

print(setz)

# You can use the - operator instead of the difference() method, and you will get the same result.

set3 = set1 - set2
print(set3)

# Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.



# The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.



set5 = {"apple", "banana", "cherry"}
set6 = {"google", "microsoft", "apple"}

set5.difference_update(set6)

print(set5)


# The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set8 = {"apple", "banana", "cherry"}
set9 = {"google", "microsoft", "apple"}

set10 = set8.symmetric_difference(set9)

print(set10)

# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

set10 = set8 ^ set9
print(set10)