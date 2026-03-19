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

# 9. count()