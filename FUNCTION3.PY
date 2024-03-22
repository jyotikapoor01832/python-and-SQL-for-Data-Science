lst = [1,3,4,5,6]
print("List : ",lst)

def poweroftwo(num):      #Square of digits in a list
    return num**2
newlst = list(map(poweroftwo,lst))    #Map function
print("New list :",newlst)


from functools import reduce

def multiply(x,y):       #Product of all numbers in a list
    return x*y
product = reduce (multiply, lst)      #Reduce function
print("Product of all numbers in a list is :",product)