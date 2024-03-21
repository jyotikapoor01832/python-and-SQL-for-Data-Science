number_lst = range(-10,11)   #Create a list from -10 to 10
print(list(number_lst))

def find_positive_number(num):   #This function return positive number if num is positive
    if num>0:
        return num
positive_num = list(filter(find_positive_number, number_lst))   #Filter function
print(positive_num)
                    