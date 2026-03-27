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

# Print characters at even and odd index separately.
# ```
# Input  :  Python

# Even : Pto
# Odd  : yhn

# even = ""
# odd = ""
# user_input=input("Enter the sentence:")
# for i in range(len(user_input)):
#     if i%2 == 0:
#         even = even +user_input[i]
#     else:
#         odd = odd + user_input[i]
        
# print(f"Even:{even}")
# print(f"Odd:{odd}")

# Reverse a string without `[::-1]`.

# Input  :  Hellow
# Output :  wolleH

# user_output = ""
# user_input = input("Enter a sentence:")
# for i in user_input:
#     user_output = i + user_output
# print(f"output : {user_output}")

# sentence = "to be or not to be"
# words = sentence.split()
# print(words)
# done = []
# for i in words:
#     if i not in done:
#         count = words.count(i)
#         print(f"Count of {i} is : {count}")
#         done.append(i)

# print(done)


#to be or not to be
# user_input = input("enter a sentence:")

# sentence = user_input.split()

# print(sentence)

# result={}

# for i in sentence:

#     if i in result:
#         result[i]+=1
#     else:
#         result[i] = 1
        
        
# print(result)

# 3.
# sentence = input("Enter Sentence : ")
# words = sentence.split()
# words.sort()
# print(words)

# sentence = "this is a test this is simple this"

# word = ""
# freq = {}

# for ch in sentence:
#     if ch != " ":
#         word += ch
#     else:
#         if word in freq:
#             freq[word] += 1
#         else:
#             freq[word] = 1
#         word = ""

# # last word
# if word:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1

# for key in freq:
#     print(key + ":" + str(freq[key]))

# Split strings into list without any using built in function
# sentence = input("Enter a sentence:")

# final = []
# res = ""

# for ch in sentence:
#     # print(f"ch :{ch}")
#     if ch != " ":
#         res = res + ch
#         # print(f"res: {res}")
#     else:
#         final.append(res)
#         res = ""
        

# final.append(res)

# print(final)


# sentence = "this is a test this is simple this"

# word = ""
# freq = {}

# for ch in sentence:
#     if ch != " ":
#         word += ch
#     else:
#         if word in freq:
#             freq[word] += 1
#         else:
#             freq[word] = 1
#         word = ""

# # last word
# if word:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1

# for key in freq:
#     print(key + ":" + str(freq[key]))


# words = input("Enter a word : ")
# L = 0
# R = len(words) - 1
# while L<R:
#     if words[L] != words[R]:
#         break
#     L = L + 1
#     R = R - 1

# # if words[L] != words[R]:
# #     print("Not a pallindrome")
# # else:
# #     print("Pal")

# if words[L] == words[R]:
#     print("pallindrome")
# else:
#     print("Not a Pal")

# Remove duplicates characters keeping first occurrence

# I/p : programming
# o/p : progamin

# user_input = "programming is a program"

# res = ""
# rpt = ""

# for i in user_input:
#     if i not in rpt:
#         rpt = rpt + i
#         res = res + i

# print(res)

# sentence = input("Enter a sentence:")


# final = []
# res = ""

# for ch in sentence:
#     #print(f"ch :{ch}")
#     if ch != " ":
#         res = res + ch
#         #print(f"res: {res}")
#     else:
#         final.append(res)
#         res = ""
        

# final.append(res)

        
# print(final)
        
# L = 0
# R = len(final)-1
# #print(L,R)
# while L<R:
#     temp = final[L]
#     #print(f"temp is {temp}")
#     final[L]= final[R]
#     final[R]=temp
#     L+=1
#     R-=1
    
# print(final)

# final2=""

# for i in range (len(final)):
#     if i == 0:
#         final2 = final[i]
#     else:
#         final2 += " "+ final[i]
    
# print(final2)