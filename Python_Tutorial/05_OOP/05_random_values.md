# Random Values

## Random Module
```python
import random

# Random integer
print(random.randint(1, 10))     # 1 to 10 (inclusive)

# Random float between 0 and 1
print(random.random())            # 0.0 to 1.0

# Random float in range
print(random.uniform(1, 10))    # 1.0 to 10.0

# Random choice from list
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))

# Shuffle list
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(cards)

# Multiple random choices
print(random.choices(fruits, k=2))  # 2 random choices

# Sample without replacement
print(random.sample(fruits, 2))    # 2 unique choices
```

## Seed (Reproducible Random)
```python
random.seed(42)
print(random.randint(1, 100))  # Always same number

random.seed(42)
print(random.randint(1, 100))  # Same again!
```

## Practical Example
```python
import random

# Generate random password
import string

def generate_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

print(generate_password(12))
```