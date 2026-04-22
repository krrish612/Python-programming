# Lists - Ordered Collections

## What is a List?
A list is like a shopping list - ordered items in order.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["apple", 1, True, 3.14]
```

## Accessing Items
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple (first)
print(fruits[-1])  # cherry (last)
```

## Modifying List
```python
fruits = ["apple", "banana"]
fruits[0] = "mango"     # Change item
fruits.append("cherry")  # Add at end
fruits.insert(1, "kiwi") # Add at position
fruits.remove("banana")  # Remove item
fruits.pop()            # Remove last item
```

## List Operations
```python
numbers = [1, 2, 3]
print(len(numbers))    # 3
print(2 in numbers)   # True
numbers.sort()        # Sort ascending
numbers.reverse()     # Reverse
```

## Looping Through List
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
# With index
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

## List Comprehension
```python
squares = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]
```