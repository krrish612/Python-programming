# Nested Loops

## What Are Nested Loops?
A loop inside another loop.

## Basic Example
```python
# Print 3x3 pattern
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()
```

## Multiplication Table
```python
# 1 to 5 tables
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()
```

## 2D List Traversal
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
```

## Finding Prime Numbers
```python
primes = []
for num in range(2, 21):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19]
```

## Pattern Printing
```python
# Triangle
for i in range(1, 6):
    print("*" * i)