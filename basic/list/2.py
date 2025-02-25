lst=[1,2,3,4] # Initialize a list with values 1, 2, 3, and 4.
lst.append(5) # Append the value 5 to the end of the list.
print(lst) # Print the updated list.
lst.extend([6,7,8]) # Extend the list by appending the elements of the list [6, 7, 8].
print(lst) # Print the extended list.
lst.pop() # Remove and return the last element of the list (8 in this case).
lst.pop() # Remove and return the last element of the list (7 in this case).
print(lst) # Print the list after popping the last two elements.