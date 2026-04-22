# Advanced Math Operations and Functions

import math
import random
from decimal import Decimal, getcontext

# ================== BASIC OPERATIONS ==================
a, b = 10, 3
print(f"10 + 3 = {a + b}")       # Addition
print(f"10 - 3 = {a - b}")      # Subtraction
print(f"10 * 3 = {a * b}")     # Multiplication
print(f"10 / 3 = {a / b}")     # Division (float)

# Floor division (round down) vs Ceiling division (round up)
print(f"10 // 3 = {a // b}")    # Floor: 3
print(f"(-10) // 3 = {(-10) // b}")  # Floor: -4 (rounds toward negative infinity)

# Modulus (remainder) - very useful for:
# 1. Checking even/odd: n % 2 == 0
# 2. Wrapping values: (value % max)
# 3. Cyclic patterns
print(f"10 % 3 = {a % b}")     # Modulus: 1
print(f"17 % 5 = {17 % 5}")    # Modulus: 2

# Power
print(f"2^10 = {2 ** 10}")      # 1024
print(f"2^10 = {pow(2, 10)}") # Same using pow()

# ================== ADVANCED OPERATIONS ==================
# Divmod - returns both quotient and remainder
quotient, remainder = divmod(17, 5)
print(f"divmod(17, 5) = ({quotient}, {remainder})")  # (3, 2)

# Integer operations
c, d = 17, 5
print(f"17 // 5 = {c // d}")   # Floor division: 3
print(f"17 % 5 = {c % d}")    # Remainder: 2

# ================== MATH MODULE FUNCTIONS ==================
x = 2.9
print(f"\n=== Math Module ===")
print(f"floor({x}) = {math.floor(x)}")   # Round down: 2
print(f"ceil({x}) = {math.ceil(x)}")   # Round up: 3
print(f"sqrt(64) = {math.sqrt(64)}")  # Square root: 8.0
print(f"pow(2, 10) = {math.pow(2, 10)}") # Power: 1024.0 (always float)
print(f"fabs(-5) = {math.fabs(-5)}")   # Absolute value: 5.0 (float)

# Trigonometry (input in radians)
print(f"sin(0) = {math.sin(0)}")        # 0.0
print(f"cos(0) = {math.cos(0)}")       # 1.0
print(f"tan(0) = {math.tan(0)}")       # 0.0

# Constants
print(f"pi = {math.pi}")              # 3.14159...
print(f"e = {math.e}")                # 2.71828...

# ================== LOGARITHMS ==================
print(f"\n=== Logarithms ===")
print(f"log(e) = {math.log(math.e)}")       # 1.0 (natural log)
print(f"log10(100) = {math.log10(100)}")     # 2.0 (base 10)
print(f"log2(8) = {math.log2(8)}")          # 3.0 (base 2)

# ================== DEEPER MATHS ==================
# Precision with Decimal (for financial/ scientific calculations)
getcontext().prec = 10
result = Decimal(1) / Decimal(7)
print(f"\n=== Precision ===")
print(f"Decimal 1/7: {result}")

# Factorial
print(f"5! = {math.factorial(5)}")          # 120
print(f"0! = {math.factorial(0)}")          # 1 (by definition)

# GCD (Greatest Common Divisor) - essential for fractions
print(f"gcd(48, 18) = {math.gcd(48, 18)}")  # 6

# LCM (Least Common Multiple)
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)
print(f"lcm(4, 6) = {lcm(4, 6)}")          # 12

# ================== COMPLEX NUMBERS ==================
z = 3 + 4j  # j represents imaginary unit (i)
print(f"\n=== Complex Numbers ===")
print(f"Real: {z.real}, Imag: {z.imag}")   # 3.0, 4.0
print(f"abs(z) = {abs(z)}")               # Magnitude: 5

# ================== RANDOM MODULE ==================
print(f"\n=== Random Module ===")
print(f"random() = {random.random()}")        # 0.0 to 1.0 (float)
print(f"randint(1, 10) = {random.randint(1, 10)}")  # 1 to 10 (inclusive)
print(f"randrange(1, 10, 2) = {random.randrange(1, 10, 2)}")  # Odd numbers 1-9
print(f"choice(['a', 'b', 'c']) = {random.choice(['a', 'b', 'c'])}")
print(f"shuffle([1,2,3]) = {random.sample([1,2,3], 3)}")  # Shuffled list

# ================== PRACTICAL EXAMPLES ==================
print(f"\n=== Practical Examples ===")

# Calculate age in days
age_years = 15
age_days = age_years * 365
print(f"Age in days: {age_days}")

# Circle calculations
radius = 7
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"Circle - Area: {area:.2f}, Circumference: {circumference:.2f}")

# Distance between two points (Pythagorean theorem)
x1, y1 = 0, 0
x2, y2 = 3, 4
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"Distance from (0,0) to (3,4): {distance}")