# Tuples

## What is a Tuple?
Like a list but CANNOT be changed (immutable).

## Creating a Tuple
```python
# Using parentheses
coordinates = (10, 20)

# Without parentheses (also works)
point = 5, 10, 15

# Empty tuple
empty = ()

# Single element (needs comma!)
single = (5,)  # Not (5)
```

## Accessing Elements
```python
point = (10, 20, 30)

print(point[0])   # 10
print(point[-1]) # 30
print(point[0:2]) # (10, 20)
```

## Tuple Methods
```python
point = (10, 20, 30)

print(point.index(20))  # 1 (position)
print(point.count(10)) # 1 (how many times)
print(len(point))        # 3
```

## Cannot Modify Tuple
```python
point = (10, 20)
point[0] = 15  # ERROR! Cannot change
```

## When to Use Tuples
- Coordinates (x, y)
- RGB colors (255, 0, 0)
- Return multiple values from function
- Dictionary keys (unlike lists)

## Tuple vs List
| Feature | Tuple | List |
|---------|-------|------|
| Change | No | Yes |
| Speed | Faster | Slower |
| Syntax | () | [] |