# Strings

# 1. They are immutable
# 2. We can using slicing and indexing
# 3. We can traverse using loops

# Name = "nihal"
# Name2 = 'Nihal'
# Name3 = """My Name is Nihal"""
# print(Name1)
# print(Name2)
# print(Name3)
# print(Name1[2])
# print(Name1[0:3:2])

# Name="Nihal"
# print(Name)
# print(type(Name))
# print(Name[0:8])
# print(Name[8])
# print(Name[:5])
# print(Name[5:])
# print(Name[::2])
# print(Name[::-1])
# print(Name[1])
# Name[1]="k"
# print(Name[1])
# for i in range(6):

# Name=Name[0:2]+"k"+Name[3:]
# print(Name)

# String Methods

# 1. Upper Case
# print(Name.upper())

# 2. Lower Case
# print(Name.lower())

# 3 strip()
# Removes spaces from edges

# Word = "   Nihal    is   |     "
# print(Word)
# print(Word.strip())
# 1. Left Strip
# print(Word.lstrip())
# 2. Right Strip
# print(Word.rstrip())

# 4. replace()
# sentence = "I love dogs"
# print(sentence)
# print(sentence.replace("dogs", "cats"))

# 5. split()
# splits strings into a list
# fruits = "apple,banana,mango"
# sentence = "I love dogs"
# print(sentence.split())
# print(fruits.split(","))
# sentence = "My name is Nihal"
# SentenceSplit : Pascal Case
# sentenceSplit : Camel Case
# sentence_split : Snake Case
# sentence-split : Kebab Case
# sentence_split = sentence.split()
# print(sentence_split)
# print(sentence_split[0:2])
# print(sentence_split[-1])

# 6. join()
# Joins list into string. Opposite of split
# fruits = ["apple", "banana", "orange"]
# print(fruits)
# print(type(fruits))
# fruits_str = " @ ".join(fruits)
# print(fruits_str)

# 7. find()  : it returns -1 if the word/substring is not present (safer for production)
# sentence = "I love Devops and its good"
# word = "k"
# print(sentence.find(word))

# 8. index() : it raises error if not found (not safer / u need to handle the error)
# word = "k"
# print(sentence.index(word))

# 9. len()
# word = "banana"
# print(len(word))

# 10. count()
# word = "apple"
# print(word.count("o"))

# 11. startswith() and endswith()
# name = "Will Johnson"
# print(name.startswith("Will"))
# print(name.endswith("son"))
# print(name.endswith(("ing", "ed")))

# 12. isdigit(), isalpha(), isalnum()
# word = "1234"
# print(word.isdigit())
# word = "abc"
# print(word.isalpha())
# word = "abc1234"
# print(word.isalnum())
# word = "12.45"
# print(word.isdigit())

# 13. in, not in
# sentence = "I love Python"
# word = "Java"
# # print(word in sentence)
# print(word not in sentence)

# 14. f-string , .format(), % style
# name = "Nihal"
# age = 26
# print(f"My name is {name} and I am {age} old")
# print("My name is {} and I am {} old".format(name, age))
# print("My name is %s and age is %d" % (name, age))

# 'd' for integers
# 'f' for floating-point numbers
# 'b' for binary numbers
# 'o' for octal numbers
# 'x' for octal hexadecimal numbers
# 's' for string
# 'e' for floating-point in an exponent format

# Loops
# string = "Python"
# length_of_string = len(string)
# count = 0
# for ch in string:
#     # print(ch)
#     count += 1

# print(count)

# for i in range(length_of_string):
#     # print(i)
#     print(string[i])

# string=input("Enter a string:")

# variable=string.split()

# print(variable[2])
# print(len(variable))


# list_variable=["I","had","my","lunch"]
# output = " ".join(list_variable)
# print(output)

# sentence = "to be or not to be not"

# # print(sentence.count("be"))
# print(sentence.find("not"))

# Q6. Write the code.
# Take sentence from user.
#  Print:
# - Total characters
# - Total words
# - Uppercase

# sentence=input("enter a string:")
# print(len(sentence))
# x=sentence.split()
# print(x)
# print(len(x))

# y=sentence.upper()
# print(y)