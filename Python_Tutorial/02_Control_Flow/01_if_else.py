# If-Else Practice

# Example 1: Check age
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Example 2: Even or Odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Example 3: Grade system
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A - Excellent!")
elif score >= 80:
    print("Grade: B - Good!")
elif score >= 70:
    print("Grade: C - Average")
elif score >= 60:
    print("Grade: D - Below average")
else:
    print("Grade: F - Fail")

# Example 4: Login check
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid credentials")

# Example 5: Your turn - Calculator
print("\n--- Simple Calculator ---")
num1 = float(input("First number: "))
op = input("Operation (+ - * /): ")
num2 = float(input("Second number: "))

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operation")