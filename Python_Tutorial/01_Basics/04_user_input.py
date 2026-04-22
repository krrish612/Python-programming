# User Input Practice

# Example 1: Simple input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Example 2: Number input
age = int(input("Enter your age: "))
print(f"You are {age} years old")

# Example 3: Calculate
birth_year = int(input("Enter birth year: "))
current_year = 2026
age = current_year - birth_year
print(f"You are {age} years old")

# Example 4: Simple calculator
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
print(f"Sum: {num1 + num2}")
print(f"Product: {num1 * num2}")

# Example 5: Your mini project
print("\n--- Temperature Converter ---")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")