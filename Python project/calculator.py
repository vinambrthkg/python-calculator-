import math
def log(num):
    return math.log(num)

def add(a,b):
    return a + b 

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
       return "division by zero is undefined"
    return a / b

def square(num):
    return num ** 2

def square_root(num):
    if num < 0:
        return "square root is not defined for negative numbers"
    else:
        return num ** 0.5 
    
def factorial(num):
    f=1
    for i in range(1,num+1):
        f*=i
    return f

def floor_division(a, b):
    if b == 0:
       return "division by zero is undefined"
    return a // b

print("simple calculator")
print("select operation")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("5. floor division")
print("6. square")
print("7. square root")
print("8. factorial")
print("9. log base 10")

choose=input("enter your choice (1-9): ")

if choose in ["1", "2", "3", "4", "5"]:
    num1= float(input("enter first number: "))
    num2= float(input("enter second number: "))
    if   choose == "1":
        print("result:", add(num1, num2))
    elif choose == "2":
        print("result:", subtract(num1, num2))
    elif choose == "3":
        print("result:", multiply(num1, num2))
    elif choose == "4":
        print("result:", divide(num1, num2))
    elif choose == "5":
     print("result:", floor_division(num1, num2))     
elif choose == "6":
     num=float(input("enter a number to find square: "))
     print("result:", square(num))
elif choose == "7":
     num=float(input("enter a number to find square root"))
     print("result:", square_root(num))
elif choose == "8": 
     num=int(input("enter a number to find its factorial"))
     print("result:", factorial(num))
elif choose == "9":
     num=float(input("enter the number to find log base 10"))    
     print("result:", math.log(num)) 
else: 
        print("invalid choice. please select between 1 to 9.")