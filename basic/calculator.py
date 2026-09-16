# simple Calculator to perform Arithmetic operations:

# Functions for each operation 

def add(a,b):
# Returns the addition of a and b
    return a+b

def sub(a,b):
# Return the subtraction of a and b
    return a-b

def multiply(a,b):
# Returns the multiplication of a and b
    return a*b

def diivision(a,b):
# Handles DivisionbyZero error
    if b ==0:
        print("Error!Divison by Zero is invalid:")
        return None
#  Returns the division of a and b
    else:
        return a/b

print("-" *30 )
print("Welcome to the Calculator!")
# Displaying the menu!
print("Select the operation!")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

# Taking input from the user
choice= input("Enter your choice(1,2,3,4)")
# Taking two numbers from user
num1=float(input("Enter the first number a: "))
num2=float(input("Enter the second number b: "))
print("-" *30 )

match choice:
    case '1':
        result=add(num1,num2)
        print("Result:",num1,'+',num2,'=',result)
    case '2':
        result=sub(num1,num2)
        print("Result:",num1,'-',num2,'=',result)
    case '3':
        result=multiply(num1,num2)
        print("Result:",num1,'*',num2,'=',result)
    case '4':
        result=diivision(num1,num2)
        if result is not None:
            print("Result:",num1,'/',num2,'=',result)
    case _:
        print("Invalid choice!Please select from 1,2,3, or 4.")
print("Thank you for using.")
print("Exit")
print("-"*30)



