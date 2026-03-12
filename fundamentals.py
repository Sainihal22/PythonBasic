# Interpreter: Python
# Compiler : C++, Java, C
# print(10+20)
# print(10 + None)
# print(10 + 30)
# print(10 + "STR")

# Variables
# Its a named container that stores a value in memory.
# Datatypes
# name = "Nihal" # String (str)
# age = 25 # integer (int)
# salary = 65000.45 # float
# is_active = True / False # boolean (bool)
# nonetype = None # Empty or No value

# 1. type : built in function
# number = 45.789
# print(number)
# print(type(number))

# number = "45.789"
# print(number)
# print(type(number))

# number = 45
# print(number)
# print(type(number))

# number = True
# print(number)
# print(type(number))

# Rules : 

# 1. It should not start with a number
# 2. Hyphens are not allowed
# 3. Reserved keywords are not allowed

# name = "Soundarya"

# Type Casting

# X = "10"
# convert string into integer
# Y = int(X)
# Convert string into float
# Z = float(X)
# print(X, type(X))
# print(Y, type(Y))
# print(Z, type(Z))

# Casting Functions
# 1. int() : convers to int
# 2. float() : converts to float
# 3. str() : converts to string
# 4. bool() : converts to bool

# num1 = 56.89
# print(int(num1))

# Input from User
# input()
# name = input("Enter your name : ")
# print(name, type(name))

# name1 = int(input("Enter a number : "))
# print(name1, type(name1))

# num2 = float(input("Enter a float number : "))
# print(num2, type(num2))

# Q. Create variables from Name, Age, City and print each with its respective type
# Q. Create variables for a product, price, and quantity. Print the total price.

# Input : Nihal
# Output : Hello Nihal, Greetings!

# name = input("Enter your name : ")

# # basic level : concating strings
# print("Hello " + name + ", Greetings!")

# # f string method
# print(f"Hello {name}, Greetings!")

# Swapping variables, swap two numbers

# 1. Using Python Power
# 2. Using Normal Way

# a = 5
# b = 7

# Output : 
# a = 7
# b = 5

# 1. Python Power
# a, b = b, a
# print(a)
# print(b)

# 2. Normal Way
# Using one more variable
# temp = a
# a = b
# b = temp
# print(a)
# print(b)

# 3. Without using third variable

# a = a + b
# b = a - b
# a = a - b
# print(a)
# print(b)

# Comparison

# a = 10
# b = "10"

# print(a == b)
# print(type(a) == type(b))

# 1. Take two numbers from the user and print their sum.
# 2. Take two numbers from the user swap it and print their sum using f string.

# Loops

# 1. For loop : we know starting and ending point
# 2. While loop : we dont know ending, but we know the condition


# 3. Do while loop : First checks condition then looping starts : not in python

# For loop

# for i in range(start, end, steps)

# for i in range(0,11, 2):
#     if i % 2 == 0:
#         print(i, "is even")
#     else:
#         print(i, "is odd")

# While loop

# check condition -> True? run the block -> check condition again
#                 -> False -> Exit the loop

# while condition:

# count = 1

# while count <= 5:
#     print(count)
#     count = count + 1

# print("The value of count is : ", count)

# count = 1
# while True:
#     print("Running this application")
#     if count <=5:
#         print(count)
#         count = count + 1
#     else:
#         break

# count = 1
# while count <= 3:
#     print(count)
#     count = count + 1
# else:
#     print("loop finished normally")

# count = 1

# while count <= 5:
#     count = count + 1
#     if count == 3:
#         continue
#     print(count)
    # print(count)
    # count = count + 1

# Operators

# 1. Arithmetic : +, -, *, /, %, **, //
# print(7/2)
# print(7//2)
# 2. Comparison : ==, !=, <, >, <=, >=
# 3. Logic : and, or, not
# for i in range(0,11):
#     if i % 2 != 0:
#         print("Odd")
# 4. Membership : in, not in
# 5. Assigment : =, +=, -=, *=
# count += 1 is similar to count = count + 1
# HW get the difference between +=, and =+, type() and isinstance()
# Bitwise Operators
# 6. Identity : is, is not

