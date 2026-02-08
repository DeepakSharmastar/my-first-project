# inheritence 
# polymorophism

# del keyword (used to delete object properties of object itself. )

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("deepak")
# print(s1.name)
# del(s1)
# print(s1.name)


# private (like) attribute & method

# class Account:

#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass   # double __ use for private keyword

#     def reset_pass(self):
#         print(acc1.__acc_pass)



# acc1 = Account("12345", "password")

# print(acc1.acc_no)
# print(acc1.reset_pass())
# print(acc1.__acc_pass)


# class Person:

#     __name = "anonymous"  # this is private variable access only internal function

#     def __hello(self):
#         print("hello person")

#     def welcome(self):
#         self.__hello()



# p1 = Person()

# print(p1.welcome())


# inheritance 

# class Car:
#     color = "black"

#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod

#     def stop():
#         print("car stoped....")

# class ToyotaCar(Car):

#     def __init__(self , name):
#         self.name = name
        

# Car1 = ToyotaCar("fortuner")
# Car2 = ToyotaCar("prius")

# # print(Car1.name)
# # print(Car1.start())
# print(Car1.color)

# Inheritance 
# types
# single inheritance
# multi-level inheritance 
# multiple inheritance

# 2 multi level inheritance 

# class Car:

#     @staticmethod
#     def start():
#         print("car started ...")

#     @staticmethod

#     def stop():
#         print("car stoped...")
        
# class ToyotaCar(Car):

#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):

#     def __init__(self, type):
#         self.type = type
    
# car1 = Fortuner("diesel")
# car1.start()

# print(car1.type)

# class A:
#     varA ="Welcome to class A"

# class B:
#     varB = "Welcome to Class B"

# class C(A,B):
#     varC = "welcome to class C"

# C1 = C()
# print(C1.varC)
# print(C1.varB)
# print(C1.varA)

# Super Method =  super() method is used to access methods of the parent class 

# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stoped...")

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()

# car1 = ToyotaCar("prius","electric")
# print(car1.type)

# Class Method

# syntax 

# class Student:
#     @classmethod  # decorator

#     def college(cls):
#         pass

# class person:
#     name = "anonymous"

#     # instnce method 

#     # def changeName(self, name):
#     #     self.__class__.name = "rahul"

#     # class method 

#     @classmethod

#     def changeName(cls, name):
#         cls.name = name



# p1 = person()
# p1.changeName("rahul kumar")
# print(p1.name)
# print(person.name)

# Property 
# we use @property decorator on any method in the class to use the method as a property 

# class Student:


#     def __init__(self, phy, chem , math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         # self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

#     # def calcPercentage(self):
#     #      self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

#     #  use @property method for check percentage
#     @property

#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"
    



# stu1 = Student(89,98,78)
# print(stu1.percentage)   

# stu1.phy = 60
# # print(stu1.phy)
# # stu1.calcPercentage()
# print(stu1.percentage)


# Polymorphism : operator overloading
# when the same operator is allowed to have different meaning according to the context 

# operator & dunder function 

# a + b #addition  a.__add__(b)
# a - b #subtraction a.__sub__(b)
# a * b #multiplication a.__mul____(b)
# a / b #division a.__truediv____(b)
# a % b #module a.__mod____(b)

# print([1,2,3] + [4,5,6])  # merge
# print(1+2)  #3
# print("deepak" + "sharma") # concatenate

# comples number - 

# ex 1i + 3j
        
# class Complex:

#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def ShowNumber(self):
#         print(self.real, "i +", self.img, "j")

#     def __add__(self,num2):  # _ _ add_ _ this is dunder function
#         newreal = self.real + num2.real
#         newimg = self.img +  num2.img

#         return Complex(newreal, newimg)
    
#     def __sub__(self,num2):  # _ _ sub_ _ this is dunder function
#         newreal = self.real - num2.real
#         newimg = self.img -  num2.img

#         return Complex(newreal, newimg)


# num1 = Complex(1,3)
# num1.ShowNumber()

# num2 = Complex(2,4)
# num2.ShowNumber()

# num3 = num1.add(num2)

# num3.ShowNumber()

# num3 = num1 + num2
# num3.ShowNumber()

# num4 = num1 - num2
# num4.ShowNumber()

# lets practice 
#  qs.  define a Circle class to create a circle with radious r using the constructor.
# define a Area() method of the class which calculates the area of the circle.
# define a perimeter() method of the class which allows to you calculate the perimeter of tha circle
# 

# class Circle:

#   def __init__(self,radius):
#     self.radius = radius



#   def Area(self):

#     return (22/7)* self.radius ** 2


#   def Perimeter(self):
#     return 2 * (22/7)* self.radius

# c1 = Circle(21)

# print(c1.Area())
# print(c1.Perimeter())


# q.2 define a Employee class with with attribute role, department & salary . this class show also
# showDetails() method 

# create an engineer class  that inherits properties from employee & has additional attributes : name & age

# class Employee:

#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role = ", self.role)
#         print("dept = ", self.dept)
#         print("salary = ", self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "75,000")


# # E1 = Employee("Accountant", "Finance", "60,000" )

# # E1.showDetails()

# engg1 = Engineer("rahul", 40)

# engg1.showDetails()

# q3  Create a class called order which stores item & price.
# user dunder function __gt__() to convey that 
# order1> order2 if price of order1> price of order2

class Order:

    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price


    
odr1 = Order("chips",20)
odr2 = Order("kurkure" , 25)

print(odr1 < odr2) # true




  

  

