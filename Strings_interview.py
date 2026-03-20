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

name = "Alice"
name[0] = "B"
print(name)

