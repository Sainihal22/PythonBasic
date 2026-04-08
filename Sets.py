# Sets

# A collection of unique unordered items

# Real life eg : 

# 1. Bag of marbles : No two marbles of same colour exists
# 2. Roll Call : Each student appears once
# 3. Lottery Numbers : No repeated number

# fruits = {"apple", "mango", "banana"}
# print(fruits)

# fruits = {"apple", "mango", "banana", "apple", "mango"}
# print(fruits)

# Properties

# 1. Unordered
# 2. Unique
# 3. Mutable
# 4. No indexing

# Initializing Empty set

# empty = {}
# print(type(empty))  # dict

# empty_set = set()
# print(type(empty_set))  # set

# Set Methods

# 1. add()
# Add a single item

# fruits = {"apple", "banana"}
# fruits.add("mango")
# print(fruits)

# 2. update() : Add Multiple Items
# fruits = {"apple", "mango"}
# fruits.update(["banana", "grapes", "orange"])
# print(fruits)

# 3. remove() : Removes Item (Error if not found)

# fruits = {"apple", "mango", "banana"}
# # fruits.remove("mango")
# print(fruits)

# fruits.remove("grapes")
# print(fruits)

# 4. discard() : Removes Item (Does not return Error if not found)

# fruits = {"apple", "mango", "banana"}
# # fruits.discard("mango")
# # print(fruits)

# fruits.discard("grapes")
# print(fruits)

# 5. pop() : Removes random item

# fruits = {"apple", "mango", "banana"}
# removed = fruits.pop()
# print(removed)
# print(fruits)

# 6. clear() : Remove all items

# fruits = {"apple", "mango", "banana"}
# fruits.clear()
# print(fruits)

# 7. copy() : copy a set

# original = {1,2,3}
# copy = original.copy()

# copy.add(4)

# print(original)
# print(copy)

# len() : Count Items
# original = {1,2,3}
# print(len(original))

# Membership Check

# fruits = {"apple", "mango", "banana"}

# print("apple" in fruits)
# print("grapes" in fruits)
# Time : O(1)   ← very fast

# List : O(n)   ← searches one by one
# Set  : O(1)   ← direct lookup using hash

# Set Operations

# 1. Union

# a = {1,2,3,4}
# b = {3,4,5,6}

# print(a | b)
# print(a.union(b))

# 2. Intersection

# a = {1,2,3,4}
# b = {3,4,5,6}

# print(a & b)
# print(a.intersection(b))

# 3. Difference

# a = {1,2,3,4}
# b = {3,4,5,6}

# print(a - b)
# print(a.difference(b))
# print()
# print(b - a)
# print(b.difference(a))

# 4. Symmetric Difference : Items in either but not both

# a = {1,2,3,4}
# b = {3,4,5,6}

# print(a ^ b)
# print(a.symmetric_difference(b))

# Subset and Superset

# a = {1,2}
# b = {1,2,3,4}

# print(a.issubset(b))
# print(b.issubset(a))
# print(a <= b)
# print(b <= a)

# print(a.issuperset(b))
# print(b.issuperset(a))
# print(a >= b)
# print(b >= a)


# isdisjoint() : No common items

# a = {1,2,3}
# b = {4,5,6}
# c = {3,4,5}

# print(a.isdisjoint(b))
# print(a.isdisjoint(c))

# Set Comprehension

# squares_set = {i * i for i in range(1,6)}
# print(squares_set)

# Frozen Set

# It is a set that cannot be changed after creation

# fruits = {"apple", "banana"}
# fruits.add("grapes")
# print(fruits)

# fruits_frozen = frozenset({"apple", "banana"})
# fruits_frozen.add("grapes")
# print(fruits_frozen) AttributeError: 'frozenset' object has no attribute 'add'

# frozenset can be used as a dictionary

# s = {1,2,3}
# d = {s : "value"}

# print(d)

# fs = frozenset({1,2,3})
# d = {fs : "Value"}
# print(d)

# No write operations, only read operations

# Union, intersection, and difference

# When to Use frozenset
# Use frozenset when:
# →  Set should never change
# →  Need to use set as dict key
# →  Want to protect set from modification

# Set vs Tuple vs List

# Feature          List        Tuple       Set
# ──────────────────────────────────────────────────
# Created with     [ ]         ( )         { }
# Ordered          Yes         Yes         No
# Mutable          Yes         No          Yes
# Duplicates       Yes         Yes         No
# Indexing         Yes         Yes         No
# Lookup speed     O(n)        O(n)        O(1)
# Use when         General     Fixed       Unique items
#                  collection  data        fast lookup

# Choose Based on Need

# Need duplicates?
#     Yes → List or Tuple
#     No  → Set

# Need to change?
#     Yes → List or Set
#     No  → Tuple or frozenset

# Need indexing?
#     Yes → List or Tuple
#     No  → Set is fine

# Need fast lookup?
#     Yes → Set  O(1)
#     No  → List or Tuple  O(n)

# 1.

# numbers = {1,2,3,2,3,3,4,4,4,4,5,6}
# print(numbers)
# print(len(numbers))

# 2.

# a = {}
# b = set()
# print(type(a), type(b))

# 3.

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print(a | b)
# # {1,2,3,4,5,6}
# print(a & b)
# # {3,4}
# print(a - b)
# # {1, 2}
# print(a ^ b)
# # {1,2,5,6}

# 4. 

# fruits = {"apple", "mango", "banana"}

# fruits.add("grapes")
# fruits.add("apple")
# fruits.discard("mango")
# fruits.discard("orange")

# print(fruits)
# print(len(fruits))

# {'apple', 'grapes', 'banana'}
# 3

# 5. 

# a = {1, 2, 3}
# b = {1, 2, 3, 4, 5}

# print(a.issubset(b)) # True
# print(b.issuperset(a)) # True
# print(a.isdisjoint(b)) # False

# 6.

# numbers = {1, 2, 3, 4, 5}

# squares = {n * n for n in numbers}
# print(squares)

# {1,4,9,16,25}

# evens = {n for n in numbers if n % 2 == 0}
# print(evens)
# {2,4}

# 7.

# a = {1, 2, 3}
# b = {4, 5, 6}

# print(a.isdisjoint(b))  # True
# a.update(b) 
# print(a) # {1,2,3,4,5,6}
# print(a.isdisjoint(b)) # False

# 8. 

# Write the code.
# Given two lists find common items using sets.

# pythonlist1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# Output: {3, 4, 5}

# pythonlistset= set(pythonlist1)
# print(pythonlistset)

# listset= set(list2)
# print(listset)

# x = pythonlistset & listset
# print(x)

# Write the code.
# Remove duplicates from a list using set.
# Keep original order.
# pythonnumbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Output: [3, 1, 4, 5, 9, 2, 6]

# backup=set()
# output= []

# for i in pythonnumbers:
#     if i not in output:
#         backup.add(i)
#         output.append(i)
        
# print(output)

# pythonlist1 = ["Alice", "Bob", "Charlie", "David"]
# list2 = ["Bob", "David", "Eve"]

# Output: {'Alice', 'Charlie'}


# list1= set(pythonlist1)
# print(list1)


# list2= set(list2)
# print(list2)

# x= list1-list2
# print(x)

# Q: What is a set?
# A: Unordered collection of unique items.
#    No duplicates. No indexing. Fast O(1) lookup.

# Q: How to create empty set?
# A: set() not {}. {} creates empty dict.

# Q: remove() vs discard()?
# A: remove() raises KeyError if not found.
#    discard() does nothing if not found. Safer.

# Q: When to use set over list?
# A: When you need unique items or fast lookup.
#    set lookup O(1) vs list lookup O(n).

# Q: What is frozenset?
# A: Immutable set. Cannot add or remove.
#    Can be used as dictionary key.

# Q: Can set contain list?
# A: No. List is mutable, not hashable.
#    Set can contain tuples and frozensets.

