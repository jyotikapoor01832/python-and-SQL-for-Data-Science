import sys

lst = ['b',0,2]
for entry in lst:
    try:
        print("The entry is : ",entry)
        r = 1 / int(entry)
    except:
        print("Oops!", sys.exc_info()[0], "occured")
        print("Next entry")
        print("**********************")
print("The reciprocal of ",entry ,"is ",r)