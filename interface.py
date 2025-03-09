import argparse

#Define functions for basic aritmetic operations
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

#Set up argument parsing
parser = argparse.ArgumentParser(description="Simple CLI Calculator")
parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Operation to perform")
parser.add_argument("a", type=float, help="First number")
parser.add_argument("b", type=float, help="Second number")

#Parse arguements
args = parser.parse_args()

#Perform the requested operation
if args.operation == "add":
    result = add(args.a, args.b)
elif args.operation == "subtract":
    result = subtract(args.a, args.b)
elif args.operation == "multiply":
    result = multiply(args.a, args.b)
elif args.operation == "divide":
    result = divide(args.a, args.b)

print(f"The result is: {result}")