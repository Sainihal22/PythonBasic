# 1. Reverse a Number
# Input : 1234
# Output : 4321

# num = 1234
# rev = 0

# while num > 0:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10       # floor division

# print(rev)

# 2. Sum of digits
# Input : 1234
# Output : 10

# n = 14589
# sum = 0

# while n > 0:
#     rem = n % 10
#     sum = sum + rem
#     n = n // 10

# print(sum)

# 3. Pallindrome Number
# Input : 121
# Output : Its a pallindrome number , input number and its reversed number are same (121 == 121 -> True)

# N = 10
# M = N
# rev = 0
# while M > 0:
#     rem = M % 10
#     rev = rev * 10 + rem
#     M = M //10

# if N == rev:
#     print("It is a Pallindrome Number")
# else:
#     print("Not a Pallindrome Number")

# 4. Numbers divisible by 3 & 5

#print even number 1 to 50 using loops

# for i in range (0,51):
#   if i%2 == 0:
#       print(i)

# x=10
# y=50
# z=30

# largest = x
# if y >largest:
#     largest=y
# if z >largest:
#     largest=z


# print(largest)

# for i in range(0,51):
#     if i%3==0 and i%2==0:
#         print(i)

#fibonacci series
# a=0
# b=1
# for i in range (10):
#     temp=a+b
#     print(a)
#     a=b
#     b=temp

#factorial
# fac=1
# n=int(input("enter a number to perform factorial:"))
# for i in range(1,n+1):
#     fac=i*fac
# print(fac)

#counting the number of digits in a number input 12345 output 5
n=int(input("enter a number:"))
count = 0
while n>0:
    n = n//10
    count+=1


print(count)
#check for a prime number
#prime numbers: divisble by 1 and itself


#prime number

# P = True
# n=int(input("give an number:"))
# for i in range(2,int(((n**0.5)+1))):
#     if n%i==0:
#         P = False
#         break
# if P==True:
#     print(f"{n} is Prime")
# else:
#     print(f"{n} is notPrime")

#armstrong

# M=int(input("Enter an number:"))
# N=M
# S=M
# count=0
# dig=0
# while N>0:
#     N=N//10
#     count=count+1
# print(f"{count} is count")
# print(f"{N} is N")
# print(f"{M} is M")
# while M>0:
#     rem=M%10
#     print(rem)
#     dig = (rem**count) + dig
#     M = M//10
# print(f"{dig} is dig")
# print(f"{M} is M")
# if S==dig:
#     print(f"{S} is a Armstrong Number")
# else:
#     print(f"{S} is not an Armstrong Number")

