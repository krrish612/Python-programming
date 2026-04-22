# Operator Precedence

## What Does It Mean?
When you have multiple operations, which one runs first?

## The Order (PEMDAS)
```
P - Parentheses ()
E - Exponents **
M - Multiplication *
D - Division /
A - Addition +
S - Subtraction -
```

## Examples
```python
# Without parentheses
result = 2 + 3 * 4
print(result)  # 14 (not 20!)

# With parentheses
result = (2 + 3) * 4
print(result)  # 20

# Left to right for same precedence
result = 10 - 5 - 3
print(result)  # 2 (not 8!)
```

## Practice
```python
print(2 * 3 + 4 / 2)    # 8.0
print((2 + 3) ** 2)      # 25
print(10 - 2 * 3)        # 4