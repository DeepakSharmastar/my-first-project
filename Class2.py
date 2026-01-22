# Strings 
# string is a data type that stores a sequence of charector.
# basic operation 

# 1. concatenation
# "hello" + "world"  --> "helloworld"

# str1 = "This is a string \nwe are creating it in python"
# str2 = 'apnacollege'
# str3 = """ this is a string"""

# escape sequence charector \n , \t
# print(str1 + str2)

# 2. length of str 
# len(str)
# print(len(str2))

# indexing 
# A p n a _ C o l l e g e
# 0 1 2 3 4 5 6 7 8 9 10 11
# str = "Apna_College"
# str[0] is 'A',str[1] is 'p' ...
# str[0] = 'B' #not allowed 

# str = "apna college"
# ch =str[0]
# print(ch)

# Slicing 
# Accessing part of a string 
# str[starting_idx : ending_idx] # ending index is not included
# str ="ApnaCollege"
# str[1:4] is "pna"
# str[ :4] is same as str[0:4]
# str[1: ] is same as str str[1:len(str)]

# str = "apna college"
# print(str[1:4])
# print(str[1:5])
# print(str[0:5])
# print(str[0:12])
# print(str[0:len(str)])
# print(str[0:])
# print(str[: 6])
# print(str[4: 6])

# negative slicing 
# 0   1  2  3  4
# A   p  p  l  e
# -5 -4 -3 -2 -1

# str = "apple"
# str[-3 : -1] is "pl"
# str = "apple"
# print(str[-4:-1])

# string functions 
# str "i am a coder" 
# str.endswith("en") # return true if string ends with substr
# str.capitalize() # capitalize 1st char
# str.replace(old, new) # replace all occurrence of old with new
# str.find(word) # return 1st index of 1st occurrence
# str.count("am") # count the occurrence of substr in string 

# 1. str.endswith("er")
# str = "i am studying python from apnacollege"
# print(str.endswith("ege")) # return true

# print(str.capitalize())
# str = "i am studying python from apnacollege"

# print(str.replace("o" ,"a"))
# print(str.replace("python" ,"javascript"))
# print(str.find("o")) # find index of O
# print(str.count("a")) # count letter and word

# practice question 
# WAP to input user's first name & print its length
# str = str(input("Enter First Name: "))
# str = len(str)
# print(str)

# wap to find the occurrencee of '$' in string

# str = "hi, $i am the $ symbol $99.99"
# print(str.count("$"))

# Conditional Statements 
# if-elif-else(SYNTAX)

# if(condition):
#     Statments1
# elif(condition):
#     Statments2
# else:
#     StatmentsN     
# age = 21
# if(age >=18):
#     print("You Are Eligiable for vote apply")

# light = "red"

# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("look")
# else:
#     print("light is broken")


# num = 1
# if(num > 2):
#     print("greater than 2")
# elif(num > 3):
#     print("greater than 3")
# else:
#     print("not valid")

# age = 17
# if(age >=18):
#     print("can vote") # indentation {} use space
# else:
#     print("can not vote")

# ex- conditional statments 
# grade students based onn marks 
# marks >=90,grade = "A"
# 90 > marks >= 80, grade = "B"
# 80 > marks >= 70, grade = "C"
# 70 > marks , grade = "D"

# marks = int(input("Enter Youur Marks: "))

# if(marks >= 90):
#     print("Grade: A")
# elif(marks >= 80 and marks < 90):
#     print("Grade: B")
# elif(marks >= 70 and marks < 80):
#     print("Grade: C")
# elif(marks > 60 and marks < 70 ):
#     print("Grade: D")
# else:
#     print("Fail")

# nesting condition means condition under condition

# age = 17
# if(age>= 18):
#     if(age >= 80):
#         print("can not drive")
#     else:
#         print("can drive")
# else:
#     print("Can not Drive")

# WAP to check if a number enter by the user is odd or even

# num = int(input("Enter Your Number: "))

# if(num % 2 == 0):
#     print("Number is Even")
# else:
#     print("Number is Odd")

# WAp to find the greatest of 3 numbers enter by user
# a = int(input("Enter Your Number A: "))
# b = int(input("Enter Your Number B: "))
# c = int(input("Enter Your Number C: "))

# if(a > b):
#     print("A is greater than B")
# elif(b > c):
#     print("B is greater than C")
# else:
#     print("C is greater than Both A and B")

# WAP to check if a number is a multiple of 7 or not

x = int(input("enter number"))

if(x % 7 == 0):
    print("Multiple of 7")
else:
    print("Not A multiple")




    



