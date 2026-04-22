# Advanced Loop Patterns and Iterations

from typing import List, Generator, Iterator
import itertools

# ================== FOR LOOPS ==================
# Basic iteration
print("=== For Loops ===")
for i in range(1, 6):
    print(i, end=" ")
print()

# range(start, stop, step)
print("\nEven numbers 2-10:")
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# ================== WHILE LOOPS ==================
# With break and continue
print("\n=== While Loops ===")
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip 3
    print(count, end=" ")
print()

# Infinite loop with break
# while True:
#     user_input = input("Enter 'quit' to exit: ")
#     if user_input == "quit":
#         break

# ================== ENUMERATE ==================
# Get index and value simultaneously
print("\n=== Enumerate ===")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Start from 1
for index, fruit in enumerate(fruits, 1):
    print(f"{index}: {fruit}")

# ================== ZIP ==================
# Iterate over multiple lists
print("\n=== Zip ===")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# Different lengths - stops at shortest
colors = ["red", "green"]
for name, age, color in zip(names, ages, colors):
    print(f"{name}, {age}, {color}")

# ================== LIST COMPREHENSION ==================
# Basic
squares = [x**2 for x in range(1, 6)]
print(f"\nSquares: {squares}")

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(f"Evens: {evens}")

# Nested comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# Dictionary comprehension
word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
print(f"Word lengths: {word_lengths}")

# Set comprehension
unique_lengths = {len(word) for word in ["hello", "hi", "hey"]}
print(f"Unique lengths: {unique_lengths}")

# ================== GENERATOR EXPRESSION ==================
# Memory efficient (doesn't create full list)
print("\n=== Generators ===")
squares_gen = (x**2 for x in range(5))
for sq in squares_gen:
    print(sq, end=" ")
print()

# ================== ITERTOOLS ==================
# Infinite counter
print("\n=== Itertools ===")
counter = itertools.count(start=1, step=2)
for i in range(5):
    print(next(counter), end=" ")
print()

# Cycle through values
colors = itertools.cycle(["red", "green", "blue"])
for i in range(6):
    print(next(colors), end=" ")
print()

# Chain multiple iterables
combined = itertools.chain([1, 2], [3, 4], [5])
print(f"Chain: {list(combined)}")

# permutations (all orderings)
perms = itertools.permutations([1, 2, 3], 2)
print(f"Permutations: {list(perms)}")

# combinations (all selections)
combs = itertools.combinations([1, 2, 3], 2)
print(f"Combinations: {list(combs)}")

# ================== ADVANCED ITERATION ==================
# Slice iterator
print("\n=== Advanced Iteration ===")
sliced = itertools.islice(range(10), 2, 8, 2)
print(f"Slice [2:8:2]: {list(sliced)}")

# Group by (need sorted data)
groups = itertools.groupby([1, 2, 2, 3, 3, 3])
for key, group in groups:
    print(f"Key: {key}, Count: {len(list(group))}")

# ================== PRACTICAL PATTERNS ==================
print("\n=== Practical Patterns ===")

# Sum with condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = sum(x for x in numbers if x % 2 == 0)
print(f"Sum of evens: {total}")

# Find first matching
numbers = [1, 2, 3, 4, 5]
first_even = next((x for x in numbers if x % 2 == 0), None)
print(f"First even: {first_even}")

# All/Any with conditions
print(f"All positive: {all(x > 0 for x in [1, 2, 3])}")
print(f"Any negative: {any(x < 0 for x in [-1, 2, 3])}")

# ================== NESTED LOOPS ==================
# Break with label (simulated)
print("\n=== Nested Loops ===")
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
        if j == 1:
            break  # Only breaks inner loop
    print()

# ================== WHILE WITH ELSE ==================
# Else runs when condition becomes false
print("\n=== While-Else ===")
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop completed!")

# ================== FOR WITH ELSE ==================
# Else runs if loop completes normally (no break)
print("\n=== For-Else ===")
for i in range(3):
    print(i)
else:
    print("Loop completed!")

# ================== FACTORIAL ==================
def factorial(n: int) -> int:
    """Calculate factorial using loop"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"\n5! = {factorial(5)}")

# ================== FIBONACCI ==================
def fibonacci(n: int) -> List[int]:
    """Generate Fibonacci sequence"""
    fibs = [0, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:n]

print(f"Fibonacci(10): {fibonacci(10)}")

# ================== PRIME CHECK ==================
def is_prime(n: int) -> bool:
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"Prime 17: {is_prime(17)}")
print(f"Prime 18: {is_prime(18)}")

# Find primes in range
primes = [x for x in range(2, 21) if is_prime(x)]
print(f"Primes 1-20: {primes}")

# ================== PASSWORD GENERATOR ==================
import random
import string

def generate_password(length: int = 12) -> str:
    """Generate random password"""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

print(f"\nPassword: {generate_password()}")

# ================== PAGINATION ==================
def paginate(items: List, page_size: int) -> Generator[List, None, None]:
    """Yield pages of items"""
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]

items = list(range(1, 11))
print(f"Pages: {list(paginate(items, 3))}")  # This creates a list from generator

# ================== FILE ITERATION (Line by Line) ==================
# Simulated line iteration
lines = ["Line 1", "Line 2", "Line 3"]
for i, line in enumerate(lines, 1):
    print(f"{i}: {line}")

# ================== ADVANCED SORTING ==================
print("\n=== Advanced Sorting ===")
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 25}
]

# Sort by age, then name
sorted_people = sorted(people, key=lambda x: (x["age"], x["name"]))
print(f"Sorted: {sorted_people}")

# Reverse sort
descending = sorted(people, key=lambda x: x["age"], reverse=True)
print(f"Descending: {descending}")