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
# a = 5
# b = 3
# print(a & b)
# print(a | b)

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

# Converting decimal to binary, octal, hexadecimal
# num = 32
# print(bin(num))
# print(oct(num))
# print(hex(num))

#Print an Even/Odd number
n=int(input("Enter an number:"))

if n&1 == 0:
    print(f"{n} is Even ")
else:
    print(f"{n} is odd ")

#print the power of 2

n=int(input("Enter an number:"))
if n & n-1 == 0:
    print(f"{n} is a power of 2")
else:
    print(f"{n} is not a power of 2")

#Swap

a=int(input("Enter a number a:"))
b=int(input("Enter a number b:"))

a=a^b
b=a^b
a=a^b
    
print(a, b)
    
    
#counting the number of 1s
n=int(input("Enter an number:"))
count =0
while n>0:
    n = n&n-1
    count +=1

    
print(count)    

#count the number of 0s

n=int(input("Enter an number:"))
m=n
count =0
countingdigits=0
result=0
place =1
while n>0:
    countingdigits += 1
    n =n //2
    
print(countingdigits)

while m>0:
    m=m&m-1
    count+=1
print(count)
print(f"{countingdigits-count} is the number of 0's")


#using built in function
n=int(input("Enter an number:"))
m=n
count =0
countingbits=n.bit_length()

print(countingdigits)

while m>0:
    m=m&m-1
    count+=1
print(count)
print(f"{countingdigits-count} is the number of 0's")


#
a=int(input("Enter an number:"))
b=int(input("Enter an number:"))
print(a&b)
print(a|b)
print(a^b)
print(a<<b)
print(a>>b)