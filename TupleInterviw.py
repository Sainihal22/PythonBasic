# 1.

# t1 = (1,2,3)
# t2 = (4,5,6)

# result = t1 + t2
# print(result)

# 2.

# t = (1,2,3)

# t += (4,)

# t = t + (4,)

# print(t)

# 3. 

# fruits = "apple", "mango", "banana", "grapes"
# print(fruits)

# 0 apple
# 1 mango
# 2 banana
# 3 grapes

# Tuple Comparison

# Tuples are compared item by item from left to right.

# t1 = (1,2,3)
# t2 = (1,2,3)
# t3 = (1,2,4)
# t4 = (1,3,0)

# print(t1 == t2)
# print(t1 == t3)
# print(t1 < t3)
# print(t1 < t4)
# t1 = None
# t2 = ""
# t1 = tuple()
# t2 = ()
# t3 = dict()
# t3 = {}
# t4 = list()
# t4 = []
# t5 = set()
# t1 = (1,2)
# t2 = (1,2,3)

# print(t1 < t2)

# print(t1 == t2)
# print(t1 < t2)

# HW : Sorting list of Tuples
# user_input = [("Alice", 23), ("Bob", 25), ("Charlie", 20)]
# Problem 2 — Find Duplicates in List
# numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]

# user_dict = {}

# for n in numbers:
#     if n in user_dict:
#         user_dict[n] += 1
#     else:
#         user_dict[n] = 1

# result = []

# for key, value in user_dict.items():
#     if value > 1:
#         result.append(key)

# print(result)

# word1 = "School master"
# word2 = "The classroom"

# # 1. Clean the first word manually
# clean_w1 = ""
# for char in word1:
#     if char != " ":
#         # Manually lowercasing (or use .lower() if permitted)
#         clean_w1 += char.lower()

# # 2. Clean the second word manually
# clean_w2 = ""
# for char in word2:
#     if char != " ":
#         clean_w2 += char.lower()

# # 3. Check length immediately
# if len(clean_w1) != len(clean_w2):
#     result = False
# else:
#     # 4. Tally letters for word 1
#     tally1 = {}
#     for char in clean_w1:
#         if char in tally1:
#             tally1[char] += 1
#         else:
#             tally1[char] = 1

#     # 5. Tally letters for word 2
#     tally2 = {}
#     for char in clean_w2:
#         if char in tally2:
#             tally2[char] += 1
#         else:
#             tally2[char] = 1

#     # 6. Compare the two dictionaries
#     is_match = True
    
#     # Check if they have the same number of unique letters
#     if len(tally1) != len(tally2):
#         is_match = False
#     else:
#         # Check if each letter count matches
#         for letter in tally1:
#             if letter not in tally2 or tally1[letter] != tally2[letter]:
#                 is_match = False
#                 break
    
#     result = is_match

# print(f"Are they anagrams? {result}")

