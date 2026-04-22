# Math Functions

## Built-in Math Functions
```python
# Absolute value
print(abs(-5))        # 5

# Round number
print(round(3.7))     # 4
print(round(3.7, 1))  # 3.7 (1 decimal)

# Power
print(pow(2, 3))      # 8 (same as 2**3)

# Min and Max
print(min(1, 5, 3))   # 1
print(max(1, 5, 3))   # 5
```

## Math Module (More Functions)
```python
import math

print(math.sqrt(16))     # 4.0 (square root)
print(math.ceil(3.2))   # 4 (round up)
print(math.floor(3.7))   # 3 (round down)
print(math.pow(2, 3))   # 8.0
print(math.pi)         # 3.14159...
print(math.e)         # 2.71828...
```

## Using Floor and Ceiling
```python
price = 9.99
print(math.ceil(price))   # 10
print(math.floor(price)) # 9