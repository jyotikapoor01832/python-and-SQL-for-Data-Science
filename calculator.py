def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

print("-------Select Option-------")
print("1.Addition")
print("2.Substrication")
print("3.Multiplication")
print("4.Division")

choice=int(input("Choose option 1/2/3/4 : "))

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

if choice==1:
    print(f"Addition of {num1} , {num2} is : " , addition(num1,num2))
elif choice==2:
    print(f"Substraction of {num1} , {num2} is : " , subtraction(num1,num2))
elif choice==3:
    print(f"Multiplication of {num1} , {num2} is : " , multiplication(num1,num2))
elif choice==4:
    print(f"Division of {num1} , {num2} is : ",division(num1,num2))
else:
    print("Invalid option!")
