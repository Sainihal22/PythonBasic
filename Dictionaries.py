# Dictionaries

# It stores data in key value pairs
# E.g : Phone book

# Key properties

# 1. Key Value Pairs : Every item will have a key and a value
# 2. Keys are unique : No duplicate keys
# 3. Mutable : Can add, remove, change
# 4. Ordered : while inserting an element order is being maintained (3.7+)
# 5. Keys are hashable : Keys must be immutable

# Valid and Invalid Keys

# d = {
#     "name" : "Soundarya",
#     1 : "one",
#     3.14 : "pi",
#     True : "yes",
#     "BMS" : 1,
#     (1,2) : "Tuple"
# }
# print(d)

# Invalid
# d = {
#     {"A": 1, "B" : 2} : "Dict",
#     {1,2} : "Sets",
#     [1,2] : "List"
# }
# print(d)

# Creating a dictionary

# Method 1 : Curly braces

# student = {
#     "name" : "Alice",
#     "age" : 22,
#     "branch" : "CSE"
# }
# print(student)

# Method 2 : dict() constructor

# student = dict(name = "Soundarya", age = 22, branch = "ECE")
# print(student)

# Method 3 : Empty then Add

# student = {}
# student["name"] = "Soundarya"
# student["age"] = 23
# student["branch"] = "ECE"
# print(student)

# Method 4 : From two lists using zip()

# keys = ["name", "age", "branch"]
# values = ["Soundarya", 22, "ECE"]

# student = dict(zip(keys, values))
# print(student)

# Accessing

# student = {
#     "name" : "Alice",
#     "age" : 22,
#     "branch" : "CSE"
# }
# print(student["name"])
# print(student.get("name"))

# print(student["section"])
# print(student.get("section", "No Key present"))

# Adding new key value pairs
# student = {"name" : "Soundarya", "age" : 22}
# print(student)
# student["branch"] = "ECE"
# print(student)

# Updating
# student = {"name" : "Soundarya", "age" : 22}
# print(student)
# student["age"] = 23
# print(student)

# Get all keys
# student = {"name" : "Soundarya", "age" : 22}
# print(student.keys())
# keys = list(student.keys())
# print(keys)

# update() : Merge or update
student = {"name" : "Soundarya", "age" : 22}
place = {"city" : "Bengaluru", "branch": "ECE"}
student.update(place)
print(student)