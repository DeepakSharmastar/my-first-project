# OOP In Python 
# class & object 

# create class 

# class Student:
#     name = "deepak"


# # create object(instance) 
# s1 = Student()

# print(s1.namess)

# class Car:
#     color = "blue"
#     brand = "mercedes"
   

# c1 = Car()

# print(c1.color)
# print(c1.brand)

# __init__Function

# constructor 

# class Student:
#     college_name = "abc college"
#     name = "anonymouse" #class attribute
#     # default constructor 
#     def __init__(self):
#         pass

#         print("adding new student in database...")
#     # parameterized constuctor 
#     def __init__(self, fullname, marks):
#         self.name = fullname #obj attribute
#         self.marks = marks
#         print("adding new student in database...")
   
# s1 = Student("karan" ,98)
# print(s1.name, s1.marks)

# s2 = Student("arjun",97)

# print(s2.name,s2.marks, s2.college_name)


# Class & instance Attribute 

# class Student:
#     college_name = "abc college"
#     name = "anonymouse" #class attribute
#     # default constructor 
#     def __init__(self):
#         pass

#         print("adding new student in database...")
#     # parameterized constuctor 
#     def __init__(self, fullname, marks):
#         self.name = fullname #obj attribute
#         self.marks = marks
#         print("adding new student in database...")

        
   


# s2 = Student("arjun",97)

# print(s2.name,s2.marks, s2.college_name)


# method 

# method are function that belonf to objects 

# class Student:

#     def __init__(self, fullname, marks):
#         self.name = fullname #obj attribute
#         self.marks = marks

#     # methods 

#     def welcome(self):
#         print("welcome student", self.name)

#     def get_marks(self):
#         return self.marks
   


# s2 = Student("karan" , 97)

# s2.welcome()
# print(s2.get_marks())

# create a student class that name & marks of 3 subjects as arguments in constructor.
# then create a method to print the avg 

class Student():

    def __init__(self, name ,marks):
        self.marks = marks
        self.name = name

    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is : " , sum/3)
        

s1 = Student("deepak",[20,30,40])
s1.avg()

# we want change name in future 
s1.name = "sharma"
s1.avg()
# s2 = Student(98)
# s3= Student(40)


        

