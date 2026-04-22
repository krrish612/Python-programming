# Simple Calculator
def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        return "Cannot divide by zero!"
    return "Invalid operation"

print("=== SIMPLE CALCULATOR ===")

while True:
    expression = input("\nEnter (e.g., 5 + 3) or 'quit': ")
    
    if expression.lower() == "quit":
        print("Goodbye!")
        break
    
    parts = expression.split()
    
    if len(parts) != 3:
        print("Use format: number operator number")
        continue
    
    try:
        a = float(parts[0])
        op = parts[1]
        b = float(parts[2])
        result = calculate(a, op, b)
        print(f"Result: {result}")
    except ValueError:
        print("Invalid number!")