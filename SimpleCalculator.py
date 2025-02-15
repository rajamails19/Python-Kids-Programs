def calculator():
    print("Let's do some math! ➕ ➖ ✖️ ➗")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose +, -, *, or /: ")
    
    if operation == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == '*':
        print(f"{num1} × {num2} = {num1 * num2}")
    elif operation == '/':
        print(f"{num1} ÷ {num2} = {num1 / num2}")
