# List Methods

## Adding Elements
```python
fruits = ["apple", "banana"]

fruits.append("cherry")      # Add at end
fruits.insert(1, "orange")  # Add at position
fruits.extend(["grape", "mango"])  # Add multiple
```

## Removing Elements
```python
fruits = ["apple", "banana", "cherry"]

fruits.remove("banana")  # Remove by value
fruits.pop()           # Remove last item
fruits.clear()        # Remove all
del fruits[0]         # Remove by index
```

## Finding Elements
```python
fruits = ["apple", "banana", "cherry"]

print(fruits.index("banana"))  # 1 (position)
print(fruits.count("apple")) # 1 (how many)
```

## Organizing
```python
numbers = [3, 1, 4, 1, 5]

numbers.sort()              # Sort in place
numbers.reverse()            # Reverse
sorted(numbers)             # Return new sorted list
```

## Copying Lists
```python
original = [1, 2, 3]
copy = original.copy()      # New list
copy = list(original)      # Also works
copy = original[:]         # Slice copy
```

## List Methods Summary
| Method | What it does |
|--------|-------------|
| append() | Add item at end |
| insert() | Add at position |
| extend() | Add multiple items |
| remove() | Remove by value |
| pop() | Remove last item |
| sort() | Sort the list |
| reverse() | Reverse the list |
| copy() | Make a copy |