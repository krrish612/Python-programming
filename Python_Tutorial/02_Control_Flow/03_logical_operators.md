# Logical Operators

## What Are They?
Combine multiple conditions using AND, OR, NOT.

## AND - Both Must Be True
```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive!")
# False if either is False
```

## OR - At Least One Must Be True
```python
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No work today!")
# True if either is True
```

## NOT - Flip the Result
```python
is_raining = True

if not is_raining:
    print("Go outside!")
else:
    print("Stay inside!")
```

## Combining All Three
```python
age = 20
has_money = True
has_permission = False

if age >= 18 and (has_money or has_permission):
    print("Allowed!")
```

## Short-Circuit Evaluation
```python
# Python stops at first False with AND
# Python stops at first True with OR

result = True and False and print("Never prints")
print(result)  # False
```

## Practical Example
```python
temp = 25
is_raining = False

if temp > 20 and temp < 30 and not is_raining:
    print("Perfect weather!")
```