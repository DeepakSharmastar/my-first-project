# total rent 
# spend of unit
# charge per unit
# numbers of persion
# foot order spend

# outpu
# total reant

rent = int(input("Enter Your rent : "))
unit = int(input("enter your bijali unit"))
charge = int(input("Charge per unit"))
food = int(input("Total spend for food"))
person = int(input("enter number of person"))

total_bill = unit * charge

total = (rent+ total_bill + food)/person
print(total)