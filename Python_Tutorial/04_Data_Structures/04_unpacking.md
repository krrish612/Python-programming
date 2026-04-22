# Unpacking

## What is Unpacking?
Extract values from sequences into variables.

## Basic Unpacking
```python
# Unpack a tuple
coordinates = (10, 20, 30)
x, y, z = coordinates
print(x, y, z)  # 10 20 30
```

## Unpacking a List
```python
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(a, b, c)
```

## Unpacking with Asterisk
```python
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)    # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

## Swap Values
```python
a = 5
b = 10

# Old way (needs temp)
temp = a
a = b
b = temp

# Python way
a, b = b, a
```

## Unpacking in Functions
```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 2, 3, 4, 5])
```

## Practical Example
```python
# Unpack coordinates
x, y = 10, 20
print(f"Point: ({x}, {y})")