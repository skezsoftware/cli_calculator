def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if operation == "add":
    result = add(a, b)
elif operation == "subtract":
    result = subtract(a, b)
elif operation == "multiply":
    result = multiply(a, b)
elif operation == "divide":
    result = divide(a, b)
else:
    print("Invalid operation you IDIOT")
    exit(1)

print(f"The result is: {result}")
