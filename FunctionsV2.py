# Functions

# A Function is a reusable block of code that performs a specific task.

# Defining
# Calling

# def function_name(parameters):
#     # body
#     return value

# Example

# def greet(name):
#     return f"Hello {name}"

# result = greet("Nihal")
# print(greet("Nihal"))
# print(f"Result : {result}")

# def : keyword to define a function
# greet : function name
# name : parameter (placeholder for input)
# return : Sends value back to caller
# greet("Nihal") : Calling the function
#                  "Nihal" is the argument
# result : Stores the returned value

# Function without return

# def greet(name):
#     print(f"Hello {name}")

# result = greet("Nihal")
# print(result)

# No return Statement : Function returns None, does not return anything
# result = None

# Return Multiple Values

# def min_max(numbers):
#     return max(numbers), min(numbers)

# high, low = min_max([5,2,8,1,9])
# print(high, low)

# return min, max --> returns a Tuple
# low, high --> Tuple unpacking 

# Default Arguments

# Give a parameter a default value --> Used when caller does not pass it

def greet(name, message = "Hello"):
    return f"{message} {name}"

print(greet("Nihal")) # uses default
print(greet("Nihal", "OK")) # overrides default
print(greet(message="Good", name="Boy"))  # keyword args