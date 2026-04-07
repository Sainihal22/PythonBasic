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