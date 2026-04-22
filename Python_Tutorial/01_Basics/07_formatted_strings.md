# Formatted Strings

## What Are Formatted Strings?
Insert variables into strings easily using f-strings.

## f-Strings (Recommended)
```python
name = "Krrish"
age = 15

# f-string
print(f"My name is {name} and I am {age} years old")

# Calculations inside
print(f"In 5 years, I will be {age + 5}")
```

## Other Formatting Methods
```python
name = "Krrish"
age = 15

# .format() method
print("My name is {} and I am {} years old".format(name, age))

# Position arguments
print("{0} is {1} years old".format(name, age))

# Named arguments
print("{n} is {a} years old".format(n=name, a=age))
```

## String Formatting
```python
price = 100.1234

# Round numbers
print(f"Price: {price:.2f}")  # 100.12

# Pad numbers
print(f"{10:05d}")  # 00010

# Thousands separator
print(f"{1000000:,}")  # 1,000,000
```

## F-Strings with Expressions
```python
import math

radius = 5
area = math.pi * radius ** 2

print(f"Area: {area:.2f}")
print(f"Pi is approximately {math.pi:.4f}")
```