# 2D Lists

## What is a 2D List?
A list inside a list. Like a table with rows and columns.

## Creating a 2D List
```python
# 3x3 grid
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

## Accessing Elements
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])  # 1 (row 0, col 0)
print(matrix[1][2])  # 6 (row 1, col 2)
print(matrix[2][1])  # 8
```

## Modifying Elements
```python
matrix[0][0] = 10
print(matrix[0][0])  # 10
```

## Looping Through
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Print all elements
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# With index
for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        print(f"({i},{j}): {element}")
```

## Practical Use
```python
# Store grades for 3 students, each with 5 subjects
grades = [
    [90, 85, 88, 92, 87],  # Student 1
    [78, 82, 80, 85, 79],  # Student 2
    [95, 91, 89, 94, 90]   # Student 3
]

print(grades[0][0])  # Student 1, Subject 1
```