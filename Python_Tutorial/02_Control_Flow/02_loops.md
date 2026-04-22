# Loops - Doing Things Again and Again

## Why Loops?
Instead of writing the same code 100 times, use a loop.

## For Loop - When You Know How Many Times

```python
# Print 1 to 5
for i in range(1, 6):
    print(i)

# Print each letter
for letter in "Python":
    print(letter)
```

## Range Function
```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)    # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8 (step of 2)
```

## While Loop - When You Don't Know

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## Break and Continue
```python
# Break - stop the loop
for i in range(10):
    if i == 5:
        break  # Stop at 5
    print(i)

# Continue - skip this iteration
for i in range(5):
    if i == 2:
        continue  # Skip 2
    print(i)  # Prints 0,1,3,4
```

## Practical Example
```python
# Find sum of 1 to 10
total = 0
for i in range(1, 11):
    total += i
print(total)  # 55
```