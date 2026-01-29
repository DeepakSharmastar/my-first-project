# file i/o in python 
# ram = volatile memory 

# open file 

# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()


# read method 

# f = open("demo.txt","r")
# # data = f.read(5) # read entire file
# data = f.readline() # read file line by line
# print(data)
# data1 = f.readline() # read file line by line
# print(data1)
# # print(type(data))
# f.close()


# writing to a file 

# # f = open("demo.txt","w")  # w for write file
# f = open("demo.txt","a") # append for new data in old data
# f.write(" \ni want learn that yestrday")
# # print(data)

# f.close()

# create new file 
# f = open("sample.txt","w")
# f.write("This sample file create by code")
# f.close()

# f = open("sample.txt", "r+") # r+ mode use for overide and replace first word
# f.write("abc")
# print(f.read())
# f.close()

# f = open("sample.txt", "w+") # w+ mode use for read and overide and no truncat
# # f.write("abc")
# print(f.read())
# f.write("abc")
# f.close()


# f = open("sample.txt", "a+") # a+ mode use for read and add (append) no truncat
# # f.write("abc")
# print(f.read())
# f.write("abc")
# f.close()


# with syntax 
# with open("demo.txt","r") as f:  
#     data = f.read()
#     print(data)

# with open("demo.txt", "w") as f:
#    data= f.write("this is new data")
#    print(data)

# deleting a file 
# using the os module 
# module (like a code library) is a file written by another programmer that generally has a functions we can use 
# import os
# os.remove("filename")

# import os   # pip install tensorflow for instal 

# os.remove("sample.txt")

# question 

# create a new file "practice.txt" using python. add the following data in it 
# Hi everyone
# we are learning file i/o 
# using java.
# i like programming in java


# f = open("practice.txt", "w")
# f.write("Hi everyone\nwe are learning file i/o\nusing java.\ni like programming in java")


# f.close()

# # java replace in python in above text

import os
# with open("practice.txt","r") as f:
#     data = f.read()
# newdata =  data.replace("java","python")
# print(newdata)

# with open("practice.txt","w") as f:
#     f.write(newdata)

# 3 . search if the word "learning" exists in the file or not
# word  = "learning"
# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find(word)!= -1):
#         print("found")
#     else:
#         print("Not Found")

# convert in function 

def check_for_ford():
    word  = "learning"
    with open("practice.txt","r") as f:
      data = f.read()
      if(data.find(word)!= -1):
        print("found")
      else:
        print("Not Found")


check_for_ford()