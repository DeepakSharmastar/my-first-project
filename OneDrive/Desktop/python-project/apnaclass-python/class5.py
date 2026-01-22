# Loops 
# 1. while loop 
# count =1
# while count <= 5 :
#    print ("Hello")
#    count += 1

# i =1 
# while i <=100 :
#     print(i)
#     i += 1
# print("loop ended")

# print number from 1 to 100 

# num = 1
# while num <= 100 :
#    print(num)
#    num += 1

#2 print number from 100 to 1
# num = 100
# while num >=1 :
#     print(num)
#     num -= 1

#3. print the multiplication table of a number n

# n = int(input("Enter Number : "))
# i = 1
# while i <= 10 :
#     mul = n * i
#     print(mul)
#     i += 1

#.4 print the elements of the following list using loop
# [1,4,9,16,25,36,49,64,81,100]


# num = [1,4,9,16,25,36,49,64,81,100]
# i = 0

# while i < len(num) :
#     print(num[i])
#     i += 1

# 4. search for a number x in this tuple using loop 
#    (1,4,9,16,25,36,49,64,81,100)

# tup = (1,4,9,16,25,36,49,64,81,100)
# idx = int(input("Enter Your Number : "))
# i = 0

# while i < len(tup) :
#     if (tup[i] == idx):
#      print("FOUND AT Index", i)
#     i += 1

# break and continue 

# i = 0

# while i < 5 :
#     print(i)
#     if (i == 3) :
#      break
#     i +=1

# print("end the loop")

# i = 0
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue #skip
#     print(i)
#     i += 1

# Loops for 

# list = [1,2,3,4,5]
# veg = ["potato", "brinjal", "ladyfinger"]

# for val in list:
#     print(val)

# for val in veg:
#     print(val)

# tup = (1,2,3,4,5,6,7,8,9,0)

# for val in tup :
#     print(val)

# str = "deepaksharma"

# for char in str:
#     print(char)


# str = "deepaksharma"

# for char in str:
#     if (char == 'a'):
#         print("a found")
#         break
#     print(char)

# else:
#     print("end")

# using for 
# 1. print the elements of the following list using a loop
# list = [1,4,9,16,25,36,49,64,81,100]

# for val in list:
#     print(val)

# 2. search for a numbr x in tuple using loop  // linear search

# tup = (1,4,9,16,25,36,49,64,81,100)

# x = int(input("Enter Your Number : "))
# idx = 0

# for val in tup:
#     if(val == x):
#         print("Found x value", tup[idx])
#     idx += 1

# Range 

# seq = range(5)
# for i  in seq :
#  print(i)

# for i  in range(5) :
#  print(i)


# for i  in range(1,5) :
#  print(i)

# for i  in range(1,5,2) :  # range(start, stop , step)
#  print(i)

# for i in range(2,100,2):
#     print(i)

# 1. print number from 1 to 100 using for and range()

# for i in range(1,101):
#     print(i)
# 2. print number from 100 to 1 

# for i in range(100,1,-1):
#     print(i)

# 3. print multiplication table of a number n 

# n = int(input("Enter Your Number"))

# for i in range (1, 11):
#     print(i*n)

# pass statements 

# for i in range(5):
#     pass #without pass statment show err
# print("Some Useful work")

# if i > 4:
#     pass #without pass statment show err
# print("Some Useful work")

#1. wap to find the sum of first natural number . usinng while

# n = int(input("Enter your number : "))
# sum = 0

# for i in range(1,n+1):
#   sum += i

# print(sum)

# n = int(input("Enter your number : "))
# sum = 0
# i = 1
# while i<= n:
#   sum += i
#   i+= 1
# print(sum)


# 2.wap to find the factorial of first n numbers using for 
n = int(input("Enter Your Number : "))
fact = 1

for i in range(1,n+1):
    fact *= i
print(fact)