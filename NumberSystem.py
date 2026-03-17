# 1. Binary : Base 2 and Digits used here are 0, 1
# 2. Octal : Base 8 and Digits used here are 0-7
# 3. Decimal : Base 10 and Digits used here are 0-9
# 4. Hexadecimal : Base 16 and Digits used here are 0-9, A to F

# Binary Conversion

# decimal to binary
# n = 10
# result = 0
# place = 1

# while n>0:
#     rem = n % 2
#     result = result + (rem * place)
#     place = place * 10
#     n = n//2

# 
a = 5
b = 3
print(a & b)
print(a | b)

#Decimal to Binary
# result=0
# place=1
# rem=0
# n=int(input("Enter an Number:"))

# while n>0:
#     rem=n%2
#     result=result+rem*place
#     place=place*10
#     n=n//2
    
# print(result)


#binary to Decimal
# place=1
# result=0
# rem=0
# n = int(input("Enter an Number:"))

# while n>0:
#     rem=n%10
#     result = result + rem * place
#     place = place * 2
#     n= n//10

# print(result)

# Decimal to octal
# result=0
# place=1
# rem=0
# n=int(input("Enter an Number:"))

# while n>0:
#     rem=n%8
#     result=result+rem*place
#     place=place*10
#     n=n//8
    
# print(result)


# binary to Octal
# place=1
# result=0
# rem=0
# n = int(input("Enter an Number:"))

# while n>0:
#     rem=n%10
#     result = result + rem * place
#     place = place * 8
#     n= n//10

# print(result)