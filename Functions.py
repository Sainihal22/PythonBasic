# Functions

# It is a reusable block of code that does a specific task

# Basic Syntax

# def function_name(parameters):
    # Code
    # print()
    # return

# 1. Paramatised Functions with no return

# def calculate_area(l,b):
#     print(l * b)

# print(calculate_area(5,6))
# calculate_area(15,6)
# calculate_area(25,6)
# calculate_area(7,6)

# def calculate_area(l,b):
#     print(l * b)

# result = calculate_area(5,6)
# print(result)

# 2. Paramatised with return
# def calculate_area(l,b):
#     area = l * b
#     print(area)
#     return area
#     # print(l - b)

# result = calculate_area(5,6)
# print(result)

# 3. No Parameters with no return

# def calculate_area():
#     pass

# def calculate_area():
#     l = 5
#     b = 6
#     area = l * b
#     print(area)

# calculate_area()

# 4. No parameters with return

# def calculate_area():
#     l = 5
#     b = 6
#     area = l * b
#     return area

# result = calculate_area()
# print(result)
# print(calculate_area)

# def min_max(numbers):
#     print(numbers)
#     minimum_number = min(numbers)
#     maximum_number = max(numbers)
#     return minimum_number, maximum_number
#     # print(minimum_number)
#     # print(maximum_number)

# list_of_numbers = [5,2,8,1,9]
# min_number, max_number = min_max(list_of_numbers)
# print(min_number, max_number)

# def min_max(numbers):
#     print(numbers)
#     minimum_number = min(numbers)
#     maximum_number = max(numbers)
#     return [minimum_number, maximum_number]
#     # print(minimum_number)
#     # print(maximum_number)

# list_of_numbers = [5,2,8,1,9]
# min_number= min_max(list_of_numbers)
# print(min_number)

# Default Arguments / Parameters
# Give a parameters a default value - it will be used when caller does not pass it

# def greet(name, message = "Hello"):
#     print(f"{message} {name}")

# greet("Bob", "Good Morning")
# greet("Alice")

# *args
# Used when we don't know how many arguments will be passed

# *args --> collects all positional arguments
#       --> Stored as tuple inside function
#       --> name args is convention, * is important

# Can pass any number of arguments

# def total(*args):
#     print(args)
#     print(type(args))
#     result = 0
#     for i in args:
#         result = result + i
#     return result

# print(total(1,2,3,4,5))

# **kwargs
# It used when we dont know the names of keys will be passed as an argument

# **kwargs --> collects all keywrod arguments
#          --> stored as DICT inside function
#          --> name kwargs is convention, ** is important

# def student_info(**kwargs):
#     print(kwargs)
#     # print(**kwargs)
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(key, value)

# student_info(name="Alice", age=23, branch="CSE")

# *args and **kwargs together

# def display(*args, **kwargs):
#     print("Args : ", args)
#     print("Kwargs : ", kwargs)

# display(1,2,3, name="Alice", age=22)

# def function(normal, *args, **kwargs) : Always in this order

# Lambda Functions
# A one-line anonymous function - no def, no name

# Syntax

# lambda parameters : expression

# Normal function
# def square(n):
#     return n * n

# square = lambda n : n * n
# print(square(5))

# add = lambda a,b : a + b
# greet = lambda name : f"Hello {name}"
# is_even = lambda n : n%2 == 0

# print(add(3,4))
# print(greet("Alice"))
# print(is_even(10))

# map() : Apply function to each item

# numbers = [1,2,3,4,5]
# squares = []
# for i in numbers:
#     squares.append(i * i)
# print(squares)

# squares = list(map(lambda n : n*n, numbers))
# print(squares)

# filter() : Filter items by condition

# numbers = [1,2,3,4,5,6,7,8]

# evens = list(filter(lambda n : n%2 == 0, numbers))
# print(evens)

# SCOPE : LEGB Rule