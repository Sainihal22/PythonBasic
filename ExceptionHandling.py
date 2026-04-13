# Exception Handling

# An Exception is an error that happens while program is running

# print(10/0)
# print(int("abc"))
# print(x)

# Without handling

# Program crashes
# All code after error --> never runs
# User sees ugly error message

# With handling

# Program handles eror gracefully
# Shows friendly message
# Continues running

# Exception              When it happens
# ──────────────────────────────────────────────────────
# ZeroDivisionError      divide by zero
# ValueError             wrong value type  int("abc")
# TypeError              wrong type        "a" + 1
# NameError              variable not defined
# IndexError             list index out of range
# KeyError               dict key not found
# FileNotFoundError      file does not exist
# AttributeError         method does not exist on object
# ImportError            module not found

# Basic structure

# try:
#     # code
# except:
#     # runs if error occurs

# try:
#     result = 10/0
#     print(result)
# except:
#     print("Something went wrong")