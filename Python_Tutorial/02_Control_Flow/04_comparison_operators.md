# Comparison Operators

## All Comparison Operators
| Operator | Meaning |
|----------|---------|
| == | Equal to |
| != | Not equal |
| > | Greater than |
| < | Less than |
| >= | Greater or equal |
| <= | Less or equal |

## Examples
```python
a = 10
b = 20

print(a == b)   # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True
```

## Chained Comparisons
```python
x = 5

# Python allows chaining
print(1 < x < 10)      # True
print(1 < x < 5)      # False

# Same as: 1 < x and x < 10
```

## Comparing Strings
```python
print("apple" == "apple")  # True
print("apple" == "APPLE")  # False (case sensitive)
print("apple" < "banana")  # True (alphabetical)
```

## Practical Example
```python
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(grade)
```