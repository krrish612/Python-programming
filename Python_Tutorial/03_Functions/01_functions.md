# Functions - Reusable Code Blocks

## Why Functions?
Functions are like recipes - write once, use many times.

## Creating a Function
```python
def greet():
    print("Hello!")
    
greet()  # Call the function
```

## Function with Input (Parameter)
```python
def greet(name):
    print(f"Hello, {name}!")
    
greet("Krrish")
greet("Python")
```

## Function with Output (Return)
```python
def add(a, b):
    return a + b
    
result = add(5, 3)
print(result)  # 8
```

## Multiple Parameters
```python
def full_name(first, last):
    return first + " " + last
    
name = full_name("Krrish", "Tripathi")
print(name)
```

## Default Parameters
```python
def greet(name="Friend"):
    print(f"Hello, {name}!")
    
greet()           # Hello, Friend!
greet("Krrish")   # Hello, Krrish!
```

## Multiple Return Values
```python
def math_op(a, b):
    return a + b, a - b, a * b
    
add, sub, mul = math_op(10, 5)
```