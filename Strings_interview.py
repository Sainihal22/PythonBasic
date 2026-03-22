# Output Based Questions

# 1.

# text = "   Hello World   "

# print(text.strip())
# print(len(text))
# print(len(text.strip()))

# 2.

# sentence = "I love Python and Python is very easy"
# print(sentence.count("Python"))
# print(sentence.find("Python"))
# print(sentence.find("Python", 10))
# print(sentence.find("Java")) # gives -1
# print(sentence.index("Java")) # it throws error

# 3. 

# text = "Hello World"
# print(text.replace("l", "L"))
# print(text.replace("l", "L", 1))
# print(text.replace("l", "L", 2))
# print(text.replace("l", "L", 5))

# 4. 

# text = "hello world"
# print(text.capitalize())
# print(text.upper())
# print(text.title())

# 5. 

# fruits = "apple,mango,banana"
# parts = fruits.split(",")
# print(parts)
# print(len(parts))
# print(parts[2])
# print(parts[5])
# print(parts[-1])
# print(",".join(parts[::-1]))

# 6.

# name = "   Alice   "
# print(name.strip() == "Alice")
# print(name == "Alice")
# print(name.strip().startswith("A"))
# print(name.startswith("A"))

# 7. 

# text = "abcdefg"
# print(text[2:])
# print(text[:3])
# print(text[1:5:2])
# print(text[-3:])
# print(text[:-3])

# 8.

# a = "hello"
# b = "hello"
# c = "HELLO"

# print(a == b)
# print(a == c)
# print(a == c.lower())
# print(a is b)

# 9.

# name = "Alice"
# name[0] = "B"
# print(name)

# 10.

# sentence = "I love Python and Python is very easy"
# result = sentence.find("Java")

# if result == -1:
#     print("Valid")
# else:
#     print("Invalid")

# 11.

# word = "playing"

# if word.endswith("ing" or "ed"):
#     print("Valid")

# if word.endswith(("ing", "ed")):
#     print("Valid")

# 12. 

# age = "25"
# next_year = age + 1
# print(next_year)

# 13. 

# age = "25"
# next_year = int(age) + 1
# print(next_year)

# 14.

# for i in range(len("Hello") + 1):
#     print("Hello"[i])

# 15. 

# text = "Hello"
# for i in range(len(text)):
#     print(text[i])

# 16.

# words = ["apple", "mango banana"]
# result = " ".join(words)
# print(result)
# print(result.split() == words)

# 17.

# Take sentence from user as an input and count vowels, consonants, and spaces

# sentence = input("Enter a sentence:")
# Vowels = "aeiou"
# v_count = 0
# s_count = 0
# c_count = 0
# n_count = 0

# for ch in sentence:
#     if ch in Vowels or ch in Vowels.upper():
#         v_count+=1
#     elif ch == " ":
#         s_count+=1
#     elif ch.isalpha():
#         c_count+=1
#     # else:
#     elif ch.isdigit():
#         n_count+=1

# print(f'The count of vowels is {v_count}')
# print(f"The count of consonants is {c_count}")
# print(f"The count of spaces is {s_count}")
# print(f"The count of numbers is {n_count}")

# 18. 

# Print each word and its length.
# Input  :  I love Python
# I      : 1
# love   : 4
# Python : 6

# sentence = input("ENter the sentence:")

# words = sentence.split()

# for ch in range(len(words)):
#     print(f"{words[ch]} : {len(words[ch])}")

# for i in words:
#     print(f"{i} : {len(i)}")

# 19. 

# Print only words longer than 3 characters.
# Input  :  I love Python and Java

# love
# Python
# Java

# sentence = input("enter the word:")
# words = sentence.split()

# for ch in words:
#     if len(ch) > 3:
#         print(ch)

# 20. 

# Replace all vowels with `*`.
# ```
# Input  :  Hello World
# Output :  H*ll* W*rld

# s = input("enter the sentence:")

# vowels = "aeiou"
# result = ""
# for ch in sentence:
#     if ch in vowels or ch in vowels.upper():
#         result = result + '*'
#     else:
#         result = result +ch
        
# for v in vowels:
#     s= s.replace(v, "x")
# print(s)