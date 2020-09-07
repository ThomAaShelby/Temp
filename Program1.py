def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b


operation = input("Enter: 1 for addition\n 2 for subtraction\n 3 for multiplication\n 4 for division")

x = float(input("Enter first number"))
y = float(input("Enter second number"))

if operation == "1":
    print("IN ADD")
    print(addition(x, y))

elif operation == "2":
    print(subtraction(x, y))

elif operation == "3":
    print(multiplication(x, y))

elif operation == "4":
    print(division(x, y))