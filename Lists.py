# Lists
# Its a collection of items stored in a single variable
# Eg : Shopping lists, shopping carts, to-do list, etc

# shopping = ["Milk", "Bread", "Egg"]
# marks = [85, 90, 65, 70]
# empty = []
# mixed = ["Milk", 90, 65.7, True, None]

# Properties

# 1. Its ordered : Items stays in order
# 2. Its mutable : It can be changed after creation
# 3. It allows duplicates : Same value can be repeated
# 4. Any Data type together : int, str, bool, float

# Compare with strings

# 1. String : Sequence of characters : Immutable
# 2. List : Sequence of anything : Mutable

# Indexing
# fruits = ["apple", "mango", "banana", "grapes"]
# print(fruits[2])
# print(fruits[5]) IndexError: list index out of range

# Slicing
# fruits = ["apple", "mango", "banana", "grapes"]
# print(fruits[5:10])
# print(fruits[:3])
# print(fruits[2:])
# print(fruits[::-1])
# print(fruits[::2])

# Mutable
# fruits = ["Apple", "Mango", "Banana", "Grapes"]
# fruits[5] = "Orange" IndexError: list assignment index out of range
# print(fruits)

# List Methods

# 1. append() : Add to End
# fruits = ["apple", "mango"]
# fruits.append("grapes")
# print(fruits)
# Time : O(1) : Always Fast

# 2. insert() : Add at a position
# fruits = ["apple", "mango", "grapes"]
# fruits.insert(1, "banana")
# print(fruits)
# fruits.insert(-1, "banana")
# print(fruits)
# fruits.insert(-6, "banana")
# print(fruits)

# 3. remove() : removes by value
# fruits = ["Apple", "Mango", "Banana", "Grapes"]
# fruits.remove("Mango")
# print(fruits)
# fruits.remove("Pineapple") ValueError
# print(fruits)

# 4. pop() : remove by index
# fruits = ["Apple", "Mango", "Banana", "Grapes"]
# fruits.pop() # it removes last item by default
# print(fruits)
# fruits.pop(5) IndexError
# print(fruits)

# 5. sort() : sort the elements in asc/dec order (Sort in place)
# numbers = [5, 2, 8, 1, 9, 3]
# numbers.sort() # asc
# print(numbers)
# fruits = ["apple", "mango", "grapes", "pineapple", "kiwi", "Litchi", "chickoo"]
# print(fruits.sort())
# print(fruits)

# numbers.sort(reverse=True) # desc
# print(numbers)

# 6. sorted() : Returns a new sorted list
# numbers = [5, 2, 8, 1, 9, 3]
# result = sorted(numbers) # asc
# print(result)
# result = sorted(numbers, reverse=True)
# print(result) # desc
# print(numbers)

# 7. reverse() : Reverse in place
# fruits = ["Apple", "Mango", "Banana", "Grapes"]
# fruits.reverse()
# print(fruits)

# 8. index() : Finds the Position
# fruits = ["Apple", "Mango", "Banana", "Grapes"]
# print(fruits.index("Litchi"))

# 9. count() : Counts the occurrences
# numbers = [5, 2, 8, 1, 9, 3, 5, 2, 10, 3]
# print(numbers.count(5))

# 10. extend() : Adds multiple items
# fruits = ['apple', "mango"]
# veggies = ["carrot", "potato"]

# # fruits.extend(veggies)
# veggies.extend(fruits)
# print(fruits)
# print(veggies)

# Difference : 

# append(x) : it add x as a single item
# extend([x]) : it adds each items of list seperately

# a = [1,2,3]
# b = [1,2,3]

# a.append([4,5])
# print(a)
# print(a[3])

# b.extend([4,5])
# print(b)

# 11. copy() : Copy a list
# original = [1, 2, 3]
# original_copy = original.copy()

# original_copy.append(4)
# print(original)
# print(original_copy)

# original_copy = original
# original_copy.append(4)
# print(original)
# print(original_copy)

# 12. clear() : Empty the list
# fruits = ["apple", "mango", "banana"]
# fruits.clear()
# print(fruits)

# 13. len() : returns the length of list
# fruits = ["apple", "mango", "banana"]

# print(len(fruits))

# Method           What it does                Time
# ───────────────────────────────────────────────────
# append(x)        Add x to end               O(1)
# insert(i, x)     Add x at index i           O(n)
# remove(x)        Remove first x             O(n)
# pop()            Remove and return last      O(1)
# pop(i)           Remove at index i          O(n)
# sort()           Sort in place              O(n log n)
# sorted()         Return new sorted list     O(n log n)
# reverse()        Reverse in place           O(n)
# index(x)         Find index of x            O(n)
# count(x)         Count x occurrences        O(n)
# extend(list)     Add all items of list      O(n)
# copy()           Shallow copy               O(n)
# clear()          Remove all items           O(n)
# len()            Total items                O(1)

# O(1) : Fastest
# O(n) : Medium
# O(n log n) : Slowest