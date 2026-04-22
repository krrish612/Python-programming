# Exceptions

## What Are Exceptions?
Errors that stop your program. Handle them to prevent crashes.

## Basic Try-Except
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## Multiple Exceptions
```python
try:
    num = int(input("Enter number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid number!")
```

## Catch All Exceptions
```python
try:
    result = 10 / 0
except Exception as e:
    print(f"Error: {e}")
```

## Try-Except-Finally
```python
try:
    file = open("data.txt")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("Done!")
```

## Raise Your Own Exception
```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
```

## Practical Example
```python
while True:
    try:
        age = int(input("Enter age: "))
        if age < 0:
            print("Age cannot be negative!")
            continue
        print(f"You are {age} years old")
        break
    except ValueError:
        print("Please enter a valid number!")
```