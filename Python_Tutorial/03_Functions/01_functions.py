# Function Practice

# Example 1: Simple function
def say_hello():
    print("Hello!")

say_hello()

# Example 2: Function with parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Krrish")

# Example 3: Function with return
def add(a, b):
    return a + b

result = add(10, 5)
print("Sum:", result)

# Example 4: Multiple parameters
def full_name(first, last):
    return first + " " + last

print(full_name("Krrish", "Tripathi"))

# Example 5: Default parameter
def welcome(greeting="Hello", name="Friend"):
    return f"{greeting}, {name}!"

print(welcome())
print(welcome("Hi", "Krrish"))

# Example 6: Calculator function
def calculator(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        return "Error: Divide by zero"
    return "Invalid operation"

print(calculator(10, "+", 5))
print(calculator(10, "*", 5))

# Example 7: Your turn!
def is_even(num):
    if num % 2 == 0:
        return True
    return False

print(is_even(10))
print(is_even(7))