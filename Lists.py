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

# List Comprehension 

# normal way

# numbers = []
# for i in range(1,6):
#     numbers.append(i)
# print(numbers)

# comprehension way

# numbers = [i for i in range(1,6)]
# print(numbers)

# Squares of a number

# squares = [i*i for i in range(1,6)]
# print(squares)

# only even numbers
# even = []
# for i in range(1,10):
#     if i%2==0:
#         even.append(i)
# print(even)

# even = [i for i in range(1,10) if i%2==0]

# names = ["alice", "bob", "charlie"]
# upper = [i.upper() for i in names]
# print(upper)

# Filter long names whose length is greater than 3
# names = ["alice", "bob", "charlie", "eve", "david"]
# long_names = [i for i in names if len(i)>3]
# print(long_names)

# Nested Lists
# A list inside a list

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# # print(matrix)
# print(matrix[0][0])

# Looping

# for row in matrix:
#     for item in row:
#         print(item, end= " ")
#     print()

## 11. List vs Other Data Structures
'''

Structure    Ordered    Mutable    Duplicates    Use When
──────────────────────────────────────────────────────────────
List         Yes        Yes        Yes           General collection
Tuple        Yes        No         Yes           Fixed data
Set          No         Yes        No            Unique items
Dictionary   Yes*       Yes        No keys       Key-value pairs
String       Yes        No         Yes           Text only


Choose list when:

Need to add or remove items
Order matters
Duplicates are allowed
Need index based access

'''

# Q1. 

# fruits = ["apple", "mango", "banana", "grapes"]
# print(fruits[-2])
# print(fruits[1:3])
# print(len(fruits))

# Q2. 

# numbers = [5,2,8,1,9,3]
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

# Q3.

# fruits = ["apple", "mango", "banana"]

# fruits.append("grapes")
# fruits.insert(1, "pineapple")
# fruits.remove("mango")

# Q4.

# a = [1,2,3]
# b = a

# a.append(4)
# print(a)
# print(b)

# Q5.

# numbers = [1, 2, 2, 3, 3, 3, 4]

# print(numbers.count(7))
# print(numbers.index(3))

# Q6.

# numbers = [i*2 for i in range(1,6)]
# print(numbers)
# [2, 4, 6, 8, 10]

# numbers = [i for i in range(1,11) if i%2 == 0]
# print(numbers)

# Q7.

# a = [1, 2, 3]
# a.append([4,5])
# print(a)
# print(len(a))

# b = [1, 2, 3]
# b.extend([4,5])
# print(b)
# print(len(b))

# Q8 Write the code : 
# 1. Take 5 numbers from user one by one
# 2. Store those 5 numbers in a list
# 3. Print the list, sum and largest number

# brute-force approach 

# numbers = []
# for i in range(1,6):
#     n = int(input(f"Enter the number {i} : "))
#     numbers.append(n)

# print(numbers)
# total = 0

# for i in numbers:
#     total = total + i

# print(total)

# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# print(largest)

# a = [1,2,3]
# b = [4,5,6]

# print(a + b)
# print(a * 3)

# numbers = [1,2,3,4,5]

# for i in range(len(numbers) + 1):
#     print(numbers[i])

# a = [1,2,3]
# b = a
# b.append(4)
# print(a)

# numbers = [3,1,4,1,5]
# result = sorted(numbers)
# print(result)
# numbers.sort()
# print(numbers == result)

# fruits = ["apple", "mango", "banana"]
# fruits.remove("grapes")
# print(fruits)

# numbers = [1,2,3,4,5]
# for n in numbers:
#     if n%2 == 0:
#         numbers.remove(n)
# print(numbers)

# Reverse a list taking values from user, without using reverse() and [::-1]

# x = int(input("enter the length of list:"))
# numbers = []


# for i in range(1, x+1):
#     n = int(input(f"Enter the number {i}: "))
#     numbers.append(n)
# print(numbers)

# L = 0
# R = len(numbers) - 1 

# while L < R:
#     temp = numbers[L]
#     numbers[L] = numbers[R]
#     numbers[R] = temp
#     L = L + 1
#     R = R - 1

# print(numbers)

# Second Largest

# numbers = [3,1,4,1,5]

# largest = numbers[0]
# second_largest = None

# for i in numbers:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif second_largest is None or i > second_largest:
#         if i != largest:
#             second_largest = i

# print(largest)
# print(second_largest)

user_input = [1,2,2,3,4,3,3,4]
empty={}

for i in user_input:
    if i in empty:
        empty[i]+=1
    else:
        empty[i]=1
       
# print(empty)

# duplicates = []

# for i in empty:
#     # print(i, empty[i])
#     if empty[i] > 1:
#         duplicates.append(i)

# print(duplicates)

# Move All Zeros to End
# numbers = [0, 1, 0, 3, 0, 5]
# [1, 3, 5, 0, 0, 0]

# result = []

# for i in numbers:
#     if i != 0:
#         result.append(i)


# for i in numbers:
#     if i == 0:
#         result.append(i)

# print(result)

# non_zeros = []
# zero_count = 0

# for i in numbers:
#     if i != 0:
#         non_zeros.append(i)
#     else:
#         zero_count += 1

# for i in range(zero_count):
#     non_zeros.append(0)

# print(non_zeros)

# j = 0

# for i in range(len(numbers)):
#     if numbers[i] != 0:
#         temp = numbers[i]
#         numbers[i] = numbers[j]
#         numbers[j] = temp
#         j += 1

# print(numbers)

# list3=[]
# for i in list1:
#     if i in list2:
#         list3.append(i)
        
# print(list3)

# Merge Two Lists and Remove Duplicates

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# #  [1, 2, 3, 4, 5, 6]

# list1.extend(list2)
# print(list1)

# backup=[]
# output=[]

# for i in list1:
#     if i not in backup:
#         backup.append(i)
#         output.append(i)
        
# print(output)

# Move All Zeros to End
# numbers = [0, 1, 0, 3, 0, 5]
# # [1, 3, 5, 0, 0, 0]

# for i in numbers:
#     if i == 0:
#         numbers.append(i)
#         numbers.remove(i)
        
# print(numbers)