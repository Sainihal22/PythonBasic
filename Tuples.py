# Tuple
# A tuple is a collections of items just like list : Difference is tuple cannot be changed after creation

# Eg : 

# 1. Date of Birth : (22,12,2000)
# 2. GPS coordinates : (12.97812,14,67891)
# 3. Student Record : ("Nihal", 22, "CSE")

# student = ("Nihal", 22, "CSE")
# dob = (22, 12, 2000)
# numbers = (1,2,3,4)
# empty = ()
# single1 = (45,)
# single = ("45",)
# single3 = ["s",]
# print(type(single))
# print(type(single1))
# print(type(single3))

# what makes a variable a tuple ?
# Ans : Comma is what it makes a tuple, not the brackets

# dob = 22, 12, 2000
# print(type(dob))
# print(dob)
'''
Feature          List                 Tuple
─────────────────────────────────────────────────
Created with     [ ]                  ( )
Mutable          Yes                  No
Can change       Yes                  No
Methods          Many                 Only 2
Speed            Slower               Faster
Memory           More                 Less
Use when         Data changes         Data fixed
'''

# Tuple, they tell to make some changes
# tuple --> List --> do some changes --> make it back to tuple
# list()

# fruits = ["apple", "banana"]
# fruits[0] = "grapes"
# print(fruits)

# fruits = ("apple", "banana")
# print(fruits[0])
# fruits[0] = "grapes" TypeError: 'tuple' object does not support item assignment
# print(fruits)
# fruits.append("grapes") AttributeError: 'tuple' object has no attribute 'append'

# Once created → fixed forever
# Cannot add, remove, or change items

# This is NOT a bug — this is the FEATURE
# Use tuple when data should never change

# Methods

# 1. count() : Count Occurrences
# numbers = (1,2,2,3,2,4,2)
# print(numbers.count(2))

# 2. Index() : Find Position
# student = ("Alice", 22, "CSE", "Delhi")
# print(student.index("CSE"))

# Tuple Packing and Unpacking

# Packing : Multiple values into one tuple

# student = "Bob", 22, "CSE"
# print(student)
# print(type(student))

# Unpacking : Split tuples into variables

# student = "Bob", 22, "CSE"
# name, age, dept = student
# print(student)
# print(name)
# print(age)
# print(dept)

# No. of variables MUST match number of items

# student = "Bob", 22, "CSE"
# name, dept = student
# print(student)
# print(name)
# print(dept)

# numbers = (1,2,3,4,5,6)

# first, *middle, last = numbers
# print(first)
# print(middle)
# print(last)

# numbers = (1,2,3,4,5,6)
# first, *rest = numbers
# print(first)
# print(rest)

# numbers = (1,2,3,4,5,6)
# *first, rest = numbers
# print(first)
# print(rest)

# Swapping using Tuple

# a = 10
# b = 5

# a, b = b, a
# print(a)
# print(b)

# Tuple as Dictionary Key

# Tuple can be used as dictionary keys -- lists cannot
# locations = {}
# locations[(12.97, 36.45)] = "Bengaluru"
# print(locations)

# locations[[12.93, 16.25]] = "Bengaluru"
# print(locations)

# Dictionary keys must be hashable
# Hashable means → value cannot change
# Tuple is immutable → hashable → can be key
# List is mutable   → not hashable → cannot be key


# Use LIST when:
# →  Data needs to change
# →  Adding or removing items
# →  Order changes

# Use TUPLE when:
# →  Data is fixed
# →  Returning multiple values from function
# →  Using as dictionary key
# →  Want to protect data from change
# →  Slightly faster and less memory

# Use tuple — fixed data
# months   = ("Jan","Feb","Mar","Apr","May","Jun",
#             "Jul","Aug","Sep","Oct","Nov","Dec")

# days     = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")

# # Use list — changing data
# cart     = ["Milk", "Eggs"]
# cart.append("Bread")

# students = ["Alice", "Bob"]
# students.remove("Bob")

# Common built in functions with tuple

# numbers = (5,2,8,1,9,3)
# print(len(numbers))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# print(sorted(numbers))
# print(numbers.sort())  AttributeError: 'tuple' object has no attribute 'sort'

# student = ("Alice", 22, "CSE")

# output : 

# ("Soundarya", 22, "ECE")

# student_tuple = ("Alice", 22, "CSE")
# print(student_tuple)
# student_list = list(student_tuple)
# student_list[0] = "Soundarya"
# student_list[1] = 22
# student_list[2] = "ECE"
# print(student_list)
# print(tuple(student_list))

# t = (1,2,3,[5,6,7], 8,9)
# t[3].append(3)
# print(t) # (1, 2, 3, [5, 6, 7, 3], 8, 9)

# Write a code to create a tuple of 5 fruits. Print each fruit with its index using a loop

# t1 = (1,2,3)
# t2 = (4,5,6)

# result = t1 + t2

# print(result)

# t = (1,2,3)

# t += (4,)

# print(t)

# Nested Tuples

# students = ("Alice", 22, ("CSE", "A"), ("Maths", "Python", "DBMS"))

# print(students[2][1])

# Nested Tuples Loop

# subjects = (("Maths", 95), ("Science", 85), ("Python", 95))

# for subject, marks in subjects:
#     print(f"{subject} : {marks}")

# Named Tuple

# A named tuple lets you access items by name instead of index.

# student = ("Bob", 25, "ECE")

# print(student[0])

# from collections import namedtuple

# Students = namedtuple("Student", ["name", "age", "dept"])

# s1 = Students("Bob", 25, "ECE")

# print(s1.name, s1.age, s1.dept)