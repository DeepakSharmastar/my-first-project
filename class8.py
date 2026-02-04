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

# class Student():

#     def __init__(self, name ,marks):
#         self.marks = marks
#         self.name = name
#     @staticmethod  # static method use for use function without self arguments (decorator)
#     def hello():  # with out self argument this function return error
#         print("hello")

#     def avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg score is : " , sum/3)
        

# s1 = Student("deepak",[20,30,40])
# s1.avg()

# # we want change name in future 
# s1.name = "sharma"
# s1.avg()
# s1.hello()

# s2 = Student(98)
# s3= Student(40)


# important concept 
# abstraction  (hiding implementation details of  a class)
# encapsulation  (wraping data)
# inheritence 
# polymorophism
# 1. 
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started...")
# car1 = Car()
# car1.start()

# create account class with 2 attributes - balance & account no
# create method for debit , credit & printing the balance 

class Accouunt:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self, amout):
        self.balance -= amout
        print("Rs" , amout, "was debited")
        print("total balance = " , self.get_balance())

    # credit method 
    def credit(self,amount):
        self.balance += amount
        print("Rs" , amount, "was credit")
        print("total balance = " , self.get_balance())
    # final balance
    def get_balance(self):
        return self.balance


acc1 = Accouunt(10000, 123456)
acc1.debit(1000)
acc1.credit(5000)

# print(acc1.balance)
# print(acc1.account_no)


