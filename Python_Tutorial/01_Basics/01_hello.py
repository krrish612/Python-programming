# Advanced Basics: Variables, Type Hints, and f-strings

# Type hints (available from Python 3.5+) - helps code readability and IDE support
name: str = "Krrish"
age: int = 15
is_learning: bool = True
height: float = 5.8

# Multiple variable assignment - assign same value to multiple variables
x = y = z = 0

# Unpacking - extract values from iterables
coordinates = (10, 20, 30)
a, b, c = coordinates

# Walrus operator (:=) - assign and use in same expression (Python 3.8+)
# This evaluates the expression and assigns it to the variable in one step
if (score := 85) >= 80:
    print(f"Passing score: {score}")

# f-strings with advanced formatting
pi: float = 3.14159
print(f"Pi: {pi:.2f}")              # :.2f = 2 decimal places → 3.14
print(f"Pi: {pi:.5f}")             # :.5f = 5 decimal places → 3.14159
print(f"Integer: {age:05d}")       # :05d = zero-pad to 5 digits → 00015

# f-string with debug self-test (Python 3.8+) - shows variable name and value
print(f"{name=} {age=} {is_learning=}")

# Conversion functions
binary: str = bin(42)             # Convert to binary → '0b101010'
hexadecimal: str = hex(255)      # Convert to hex → '0xff'
octal: str = oct(64)             # Convert to octal → '0o100'

# String formatting with alignment
print(f"{'Name':<10} {'Age':>5}")  # Left-align in 10 chars, Right-align in 5
print(f"{name:<10} {age:>5}")

# f-string conditional - show different text based on condition
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# f-string with nested variables
user = {"name": "Krrish", "age": 15}
print(f"User: {user['name']}, Age: {user['age']}")

# f-string with function calls
message = "hello world"
print(f"Upper: {message.upper()}")
print(f"Word count: {len(message.split())}")

# Using format spec with multiplication
multiplier = 5
print(f"5 x 7 = {multiplier * 7}")

print("\n=== Output ===")
print(f"Hello, {name}!")
print(f"Learning Python: {is_learning}")
print(f"Height: {height}")