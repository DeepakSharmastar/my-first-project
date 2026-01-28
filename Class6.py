# function and recursion 
# a = 5
# b =10
# sum = a+b
# print(sum)

# def calc_sum(a,b):
#     sum = a+b
#     print(sum)
#     return sum
# calc_sum(10,20)

# this is my function defination 
# def calsum(a,b):  # parameters
#     return a+b

# sum = calsum(110,220) # function call ; arguments
# print(sum)

# def print_hello():
#     print("hello")

# print_hello()

# average of three numbers 
# def avg(a,b,c):
#     sum = a+b+c
#     avgs = sum/3
#     print(avgs)
#     return avgs
# avg(30,40,50)


# function type 
# 1 built in function
# 2 userdefine function

# default perameter 
# def cal_prod(a=1,b=2):
#     print(a*b)
#     return a*b
# cal_prod()


# 1. wap to print the length of a list. (list in the perameter)

# def list_pera(list):
#     print(len(list))
#     # return len(list)
# list = [1,2,3,4,5,6,7,8,9]
# list_pera(list)

# 2. wap to print the elements of a list in a single line. (list is the parameter)

# heroes = ["thor","ironman","captain","saktiman"]
# # print(heroes[0], end=" ")
# # print(heroes[1], end=" ")

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(heroes)
# print()

# 3. WAF to find the factorial on n (n is perameter)

# def cal_fact(n):
#     fact =1
#     for i in range(1,n+1):
#      fact *= i
#     print(fact)
# cal_fact(5)

# 4. wap to convert usd to inr

# def converter(usd_val):
#    inr_val = usd_val * 83
#    print(usd_val, "USD = ", inr_val)

# converter(2)

# def oddeven(n):
#    if(n%2==0):
#       print("even")
#    else:
#     print("odd")
   
# oddeven(10)

# Recusrion 
# def show(n):
#    if(n==0):  #base case for stop recursion
#       return
#    print(n)
#    show(n-1)

# show(5)

# def fact(n):
#     if(n==0 or n==1): 
#         return 1
    
#     return fact(n-1)*n
# print(fact(4))

# wap a recursive function to calculate the sum of first n natural numbers

# def first_natural(n):
#     if(n==0):
#         return 0
#    #  print(n)
#     return first_natural(n-1) + n
# sum = first_natural(5)
# print(sum)

# wap a recursive function to print all elements in a lsit
# hint : use list & index as parameters 

def print_list(list , idx=0):
    if(idx == len(list)):
        return 
    print(list[idx])
    print_list(list,idx + 1)

fruits = ["mango", "banana" , "apple"]
print_list(fruits)

    