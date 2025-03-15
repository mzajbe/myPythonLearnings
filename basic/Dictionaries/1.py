# Creating a Dictionary
# empty dictionary 
my_dict = {}

student = {
    "name": "Zajbe",
    "age":24,
    "courses": ["Math", "CompSci"]
}

# Accessing Values 
print(student["name"])

# If the key doesn't exist, it raises a KeyError. To avoid this, use the .get() method:
print(student.get("address"))  # Output: None (no error)
print(student.get("address", "Not Found"))  # Output: Not Found (default value)


# Adding or Updating Items
student["phone"] = "555-5555"
student["email"] = "zajbe@gmail.com"

print(student)

# Removing Items 
del student["age"]
print(student)

email = student.pop("email")
print(email)

# Iterating Through a Dictionary

# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(key, value)


# Dictionary Methods
# .keys(): Returns a list of all keys.
print(student.keys())  # Output: dict_keys(['name', 'courses', 'email'])


# .values(): Returns a list of all values.
print(student.values())  # Output: dict_values(['Alice', ['Math', 'Science'], 'alice@example.com'])
# .items(): Returns a list of key-value pairs as tuples.

print(student.items())  # Output: dict_items([('name', 'Alice'), ('courses', ['Math', 'Science']), ('email', 'alice@example.com')])


# .update(): Merges another dictionary into the current one.
student.update({"age": 22, "phone": "123-456-7890"})


# Nested Dictionaries
students = {
    "Alice": {"age": 21, "courses": ["Math", "Science"]},
    "Bob": {"age": 22, "courses": ["History", "English"]}
}

print(students["Alice"]["courses"])  # Output: ['Math', 'Science']