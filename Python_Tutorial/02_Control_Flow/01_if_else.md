# Making Decisions (If-Else)

## Why Do We Need If-Else?
Programs need to make choices based on conditions.

## The Logic:
```
IF condition is true:
    Do something
ELSE:
    Do something else
```

## Basic If-Else

```python
age = 15

if age >= 18:
    print("You can vote")
else:
    print("Too young to vote")
```

## Multiple Conditions (elif)

```python
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Need improvement")
```

## Comparison Operators

| Symbol | Meaning |
|--------|---------|
| == | Equal to |
| != | Not equal |
| > | Greater than |
| < | Less than |
| >= | Greater or equal |
| <= | Less or equal |

## Combining Conditions (and, or, not)

```python
age = 20
has_license = True

if age >= 18 and has_license:
    print("Can drive!")
```

## Your Turn
Open `01_if_else.py` and try the exercises.