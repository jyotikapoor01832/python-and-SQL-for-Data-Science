# Lambda function with filter,map,reduce
lst = [1,2,3,4,5]
print(lst)

#Example use with filter
even_list = list(filter(lambda x : (x%2==0) ,lst))        #filter function
print("Even numbers in list : ",even_list)

#Example use with map
new_lst = list(map(lambda x:(x**2),lst))
print("New list : ",new_lst)

#Example use with reduce
from functools import reduce
new_lst = reduce(lambda x,y: (x*y),lst)
print("After reduce : ",new_lst)