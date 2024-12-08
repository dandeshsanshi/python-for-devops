# Wrting a python code to calculate addition, subtraction, multiplication and division of two numbers
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# addition = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2

# print("Addition:", addition)
# print("Subtraction:", subtraction)
# print("Multiplication:", multiplication)
# print("Division:", division)

num1 = 20
num2 = 10

def addition():
    addition = num1 + num2
    print("num1:", num1)
    print("num2:", num2)
    print("After addition the result is:", addition)

def subtraction():
    print("Inside subtraction function")
    subtarction = num1 - num2
    print("num1:", num1)
    print("num2:", num2)
    print("After subtarction the result is:", subtarction)

def multiplication():
    print("Inside multiplication function")
    multiplication = num1 * num2
    print("num1:", num1)
    print("num2:", num2)
    print("After multiplication the result is:", multiplication)

def division():
    print("Inside division function")
    print("num1:", num1)
    print("num2:", num2)
    division = num1 / num2
    print("After division the result is:", division)

# Call the functions
addition()  
subtraction()
multiplication()
division()