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