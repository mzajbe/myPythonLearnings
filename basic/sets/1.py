

# Set items are unordered, unchangeable, and do not allow duplicate values.

thisSet = {"apple", "banana", "cherry"}
print(thisSet)

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisSet2 = {"apple", "banana", "cherry", True, 1, 2}
print(thisSet2)

# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
thisSet3 = {"apple", "banana", "cherry", False, True, 0}
print(thisSet3)

print("\n\n")

# Get the Length of a Set
thisSet4 = {"apple", "banana", "cherry"}
print(len(thisSet4))

print("\n\n")

# A set can contain different data types:
set1 = {"abc", 34, True, 40, "male"}


myset = {"apple", "banana", "cherry"}
myString = "Hello"
myInt = 20
mybool = True
print(type(myset))
print(type(myString))
print(type(myInt))
print(type(mybool))

# <class 'set'>
# <class 'str'>
# <class 'int'>
# <class 'bool'>


print("\n\n")


