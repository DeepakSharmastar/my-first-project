# Dictionary & Set 

# Dicti0nary in python 
# Dictionary are used to store data values in key:values pairs 
# they are unordered, mutable(changeable) & don't allow duplicate keys
# "key" : value 
# dict ={
#     "name" : "shradha",
#     "cgpa" : 9.6,
#     "marks" : [98,97,95]
# }

# dict["name"],dict["cgpa"],dict["marks"]

# dict["key"] = "value" # to assign or add new

# info = {
#     "name":"deepak",
#     "subject" : ["python","c","java"],
#     "topics" : ("dict","set"),
#     "age":29,
#     "is_adult" : True,
#     "marks" : 94.4,
   
# }
# null_dict = {

# }
# null_dict["name"] = "pankaj"
# # print(info)
# # print(info["marks"])
# info["name"] ="sharma" # for change key value
# info["surname"] = "gupta"  # for add new values and key
# print(info)
# print(null_dict)

# ----------Nested Dictionary ------------
# student ={
#     "name" : "deepak",
#     "score":{
#         "chem" : 98,
#         "phy" : 97,
#         "math" : 95
#     }
# }

# # student["score"]["math"]
# print(student["score"]["math"])
# print(student["name"])

# ---------Dictionary Methods ----------
# myDict.keys() #return all keys
# myDict.values() #return all values
# myDict.items() #return all (key,val) pairs as tuples
# myDict.get("key") #return the key accordian to value
# myDict.updates(newDict) # insert the specified items to the dictionarys

# student ={
#     "name" : "deepak",
#     "score":{
#         "chem" : 98,
#         "phy" : 97,
#         "math" : 95
#     }
# }
# print(list(student.keys()))  #list use for type cast
# print(list(student.values()))
# print(len(list(student.values())))

# print(student.items())
# print(student["name"]) #if key is not in dict return error
# print(student.get("name")) #if key is not in dict return Nne
# new_dict ={"city":"delhi"} 
# student.update(new_dict)
# print(student)

# --------Set in python ------------
# set is the collection of the unordered items.
# Each elements in the set must be unique & immutable(unchangable)
# we can not store list and dict in set because both are mutuble 

# nums = {1,2,3,4}

# set = {1,2,3,3,3}
# #repeated elements stored only once , so it resolved to [1,2,3]

# null_set= set() #empty set syntax

# collection = {1,2,3,4,"hello","world","world",5}
# print(collection)
# print(type(collection))
# print(len(collection))

# collection ={} # this is dict not set
# # for create empty set  use set()
# collection = set()
# print(collection)
# print(type(collection))

# ------- Set Methods ----------

# set.add(el) #adds an element
# set.remove(el) # removes the elem an
# set.clear() #empties the set
# set.pop() #removes a random values
# both method imp 
# set.union(set2) # combines both set values & returns new
# set.intersection(set2) # combines common values & return new

# imp- sets are mutuable (changeable) but set elements are not mutuable

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.remove(1)
# collection.add("apnaclass")
# collection.add((1,2,3,4))
# # collection.add([1,2,3,4,5,6]) unhashable type - mutable - hashvalue - immutable
# # collection.clear()
# print(collection)
# print(len(collection))

# collection ={"hello", "apnacollege","world","coding"}
# print(collection.pop())
# print(collection.pop())

# union 

# set1 ={1,2,3}
# set2 ={2,3,4}
# print(set1.union(set2)) #{1,2,3,4}

# intersection 
# set1 ={1,2,3}
# set2 ={2,3,4}

# print(set1.intersection(set2)) #{3}

# let's practice 
# Store following word meaning in a python dictionary

# table : "a piece of furniture", "list of facts & figures"
# cat : "a small animal"

# dictionary = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture", "list of facts & figures"]

# }
# print(dictionary)

# you are given a list of subject for student. assume one classroom is required for 1 subject. how many classroom are needed by all students
# "python","java","c++","python","javascript",
# "java","python","java","C++","c"

# # set1 ={"python","java","C++","python","javascript"}
# # set2 = {"java","python","java","C++","c"}
# # print(len(set1.union(set2)))
# subject ={
#     "python","java","C++","python","javascript",
# "java","python","java","C++","c"
# }
# print(subject)

# Wap to ener marks of 3 subject from the users and store them in a dictionary
# . start with an empty dictionary & add one by one. use subject name as key & marks as value
# dictionary = {}
# x = int(input("enter phy "))
# dictionary.update({"phy" : x})
# x = int(input("enter math "))
# dictionary.update({"math" : x})
# x = int(input("enter chem "))
# dictionary.update({"chem" : x})

# # sub1 = {"chem" : 99,"math" : 99, "eng" : 77}
# # dictionary.update(sub1)
# print(dictionary)

# figure out of way to store 9 & 9.0 as separate values in the set 
# (you can take help built in data type)
# values = {9,"9.0",9.10,9.0}
# print(values)

values ={
    ("float" ,9.0),
    ("int",9)
}
print(values)