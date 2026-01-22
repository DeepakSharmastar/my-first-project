# list and tuple 
# List in python 
# a built in data type that stores set of values
# it can store elements of different types (integer,float,string,etc) 

# marks = [87,64,32,23] #marks[0], marks[1]..
# student = ["karan", 85, "delhi"] #student[0], student[1]...
# student[0] = "arjun" #allowed in python
# len(student) #return length

# marks = [83,32,44,30,40]
# print(marks)
# print(type(marks)) # check type of marks
# print(marks[0])
# print(marks[1])
# print(len(marks)) #check for length

# string = immutable - we can not change
# list = mutuable - we can change list

# student = ["deepak", 85, 29, "delhi"]
# print(student)
# print(student[1])
# student[0] = "pankaj"
# print(student)
# print(student[4])

# --- list slicing ----
# similar to string slicing

# list_name[starting_idx : ending_idx] #ending idx is not included
# marks = [87,64,33,95,76]
# marks[1:4] is [64,33,95]
# marks[ :4] is same as marks[0:4]
# marks[1: ] is same as marks[1 :len(marks)]
# marks[-3:-1] is[33,95]

# marks = [87,64,33,95,76]
# print(marks[1:4])
# print(marks[:4])
# print(marks[1:])
# print(marks[-3:-1])

# ---- list methods -----
# list = [2,1,3]
# list.append(4) #adds one element at the end [2,1,3,4]
# list.sort() #sort in ascending order [1,2,3]
# list.sort(reverse = True) #sort inn descending order [3,2,1]
# list.reverse() # reverses list [3,1,2]
# list.insert(idx,el) # insert elements at index
# list.remove(1) # removes first occurrence of elements [2,3]
# list.pop(idx) #removes elemet at idx 

# list = [2,3,1,3]
# list.append(4)
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.reverse()
# print(list)
# list.insert(2,4)
# print(list)
# list.remove(1)
# print(list)
# list.pop(1)
# print(list)

# ------ Tuples in python -------

# a built in data type that lets us create immutable sequence of values
# tup = (87,64,33,95,76) #tup[0],tup[1]
# tup[0] = 43 # not allowed in python

# tup1 =()
# tup2 = (1)
# tup3 = (1,2,3,4)

# tup = (2,1,3,1)
# print(type(tup))
# print(tup[0])
# print(tup[0:1])

# ----- Tuple Methods -----
# tup.index(el) # returns index of first occurrence tup.index(1) is 1
# tup.count(el) #counts total occurrences tup.count(1) is 2

# print(tup.index(1))
# print(tup.count(1))

# Practice 
# WAP to ask the user to enter names of their 3 favorite movies & store them in a list 
movie = []
# mov1 = input("enter your first name: ")
# mov2 = input("enter your second name: ")
# mov3 = input("enter your third name: ")
# movie.append(mov1)
# movie.append(mov2)
# movie.append(mov3)
# movie.append(input("enter your 1 movie"))
# movie.append(input("enter your 2 movie"))
# movie.append(input("enter your 3 movie"))
# print(movie)

# WAP to check if a list contains a palindrome of elements.(Hint:use copy() method)

# palin = [1,2,3,2,1]
# list2 = [1,2,3]
# copy_list = palin.copy()
# copy_list.reverse()
# copy_list2 = list2.copy()
# copy_list2.reverse()



# if(copy_list == palin):
#     print("this is palindrome")
# else:
#     print("This Is not Palindrome")

# if(copy_list2 == list2):
#     print("This IS palindrome")
# else:
#     print("This Is Not Palindrome")

# WAP to count the number of students with the "A" grade in the following tuple 
grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))


# store the above values in a list & sort from "A" to "D" 

# grade = ["C","D","A","A","B","B","A"]
# grade.sort()
# print(grade)


