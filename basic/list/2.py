lst=[1,2,3,4] # Initialize a list with values 1, 2, 3, and 4.
lst.append(5) # Append the value 5 to the end of the list.
print(lst) # Print the updated list.
lst.extend([6,7,8]) # Extend the list by appending the elements of the list [6, 7, 8].
print(lst) # Print the extended list.
lst.pop() # Remove and return the last element of the list (8 in this case).
lst.pop() # Remove and return the last element of the list (7 in this case).
print(lst) # Print the list after popping the last two elements.


print("\n\n")


print(sum(lst))
lst.pop()
print(lst)
lst.pop(3)
print(lst)

print("\n\n")


lst2=[1,1,3,4,4,6,7,8,9,10]
print(lst2.count(1)) # Counts the number of occurrences of 1 in lst2 and prints the result.
print(lst.index(1)) # Finds the index of the first occurrence of 1 in lst and prints the result. Note: this uses the 'lst' variable from the previous example, NOT 'lst2'.
print(lst2*2) # Creates a new list by repeating the elements of lst twice and prints the result.