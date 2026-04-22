# Advanced List Operations and Functional Programming

from typing import List, Optional, Callable, Iterator
import itertools
import collections

# ================== BASIC OPERATIONS ==================
fruits = ["apple", "banana", "cherry", "mango"]
print(f"Fruits: {fruits}")
print(f"First: {fruits[0]}")
print(f"Last: {fruits[-1]}")

# ================== LIST COMPREHENSIONS ==================
# Basic
squares = [x**2 for x in range(1, 6)]
print(f"\nSquares: {squares}")

# With condition
evens = [x for x in range(20) if x % 2 == 0]
print(f"Evens: {evens}")

# Nested
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matrix: {matrix}")

# Multiple sources
pairs = [(a, b) for a in [1, 2] for b in [3, 4]]
print(f"Pairs: {pairs}")

# Dictionary from list
word_to_len = {word: len(word) for word in ["hello", "world"]}
print(f"Word lengths: {word_to_len}")

# ================== ITERTOOLS FOR LISTS ==================
# Cycle through list
print("\n=== Itertools ===")
colors = ["red", "green", "blue"]
cycled = itertools.islice(itertools.cycle(colors), 5)
print(f"Cycle: {list(cycled)}")

# Repeat
repeated = list(itertools.repeat("hello", 3))
print(f"Repeat: {repeated}")

# Chain
combined = list(itertools.chain([1, 2], [3, 4], [5]))
print(f"Chain: {combined}")

# Groupby (needs sorted data)
groups = itertools.groupby([1, 1, 2, 2, 3])
for key, group in groups:
    print(f"Key: {key}, List: {list(group)}")

# ================== FUNCTIONAL OPERATIONS ==================
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"\nFilter evens: {evens}")

# Map
doubled = list(map(lambda x: x * 2, nums))
print(f"Map doubled: {doubled}")

# Reduce (imported from functools)
from functools import reduce
total = reduce(lambda x, y: x + y, nums)
print(f"Reduce sum: {total}")

# All/Any
print(f"All positive: {all(x > 0 for x in nums)}")
print(f"Any even: {any(x % 2 == 0 for x in nums)}")

# ================== LIST METHODS ==================
print("\n=== List Methods ===")
items = [1, 2, 3]

# Append (add to end)
items.append(4)
print(f"Append: {items}")

# Extend (add multiple)
items.extend([5, 6])
print(f"Extend: {items}")

# Insert at index
items.insert(0, 0)
print(f"Insert: {items}")

# Remove first occurrence
items.remove(3)
print(f"Remove: {items}")

# Pop (remove and return)
popped = items.pop()
print(f"Pop: {popped}, List: {items}")

# Clear
copied = items.copy()
items.clear()
print(f"Clear: {items}, Copy: {copied}")

# ================== SLICING ==================
nums = list(range(10))
print(f"\n=== Slicing ===")
print(f"Original: {nums}")
print(f"[2:5]: {nums[2:5]}")
print(f"[:3]: {nums[:3]}")
print(f"[5:]: {nums[5:]}")
print(f"[::2]: {nums[::2]}")  # Every 2nd
print(f"[::-1]: {nums[::-1]}")  # Reverse
print(f"[1:8:2]: {nums[1:8:2]}")

# ================== SORTING ==================
print("\n=== Sorting ===")
names = ["Charlie", "Alice", "Bob"]
print(f"Original: {names}")
print(f"Sorted: {sorted(names)}")
print(f"Reverse: {sorted(names, reverse=True)}")
print(f"By length: {sorted(names, key=len)}")

# Sort in place
items = [3, 1, 4, 1, 5, 9, 2, 6]
items.sort()
print(f"Sort: {items}")
items.sort(reverse=True)
print(f"Reverse sort: {items}")

# Sort with custom key - sort by last character
words = ["apple", "banana", "cherry"]
words.sort(key=lambda x: x[-1])
print(f"Sort by last: {words}")

# ================== FINDING ==================
fruits = ["apple", "banana", "cherry", "banana"]
print(f"\n=== Finding ===")
print(f"Index: {fruits.index('banana')}")
print(f"Count: {fruits.count('banana')}")
print(f"In list: {'cherry' in fruits}")

# Find first even
nums = [1, 2, 3, 4, 5]
first_even = next((x for x in nums if x % 2 == 0), None)
print(f"First even: {first_even}")

# ================== DEQUE (DOUBLE-ENDED QUEUE) ==================
from collections import deque

dq = deque([1, 2, 3])
print(f"\n=== Deque ===")
dq.append(4)           # Add to right
dq.appendleft(0)        # Add to left
print(f"After appends: {dq}")
dq.pop()               # Remove from right
dq.popleft()          # Remove from left
print(f"After pops: {dq}")

# Rotate
dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)          # Rotate right by 2
print(f"Rotate 2: {dq}")

# ================== ADVANCED PATTERNS ==================
print("\n=== Advanced Patterns ===")

# Flatten nested list
nested = [[1, 2], [3, 4], [5]]
flattened = [item for sublist in nested for item in sublist]
print(f"Flatten: {flattened}")

# Remove duplicates (preserve order)
items = [1, 2, 2, 3, 1, 4, 3]
unique = list(dict.fromkeys(items))
print(f"Unique: {unique}")

# Partition (split by condition)
def partition(items: List, condition: Callable) -> tuple[List, List]:
    """Split list into two based on condition"""
    true_list = [item for item in items if condition(item)]
    false_list = [item for item in items if not condition(item)]
    return true_list, false_list

evens, odds = partition([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(f"Evens: {evens}, Odds: {odds}")

# Chunk (split into fixed-size lists)
def chunk(items: List, size: int) -> List[List]:
    return [items[i:i+size] for i in range(0, len(items), size)]

chunks = chunk([1, 2, 3, 4, 5, 6, 7], 3)
print(f"Chunks: {chunks}")

# ================== STACK AND QUEUE ==================
print("\n=== Stack & Queue ===")

# Stack (LIFO)
stack = []
stack.append(1)  # push
stack.append(2)
stack.append(3)
print(f"Pop: {stack.pop()}")  # 3
print(f"Pop: {stack.pop()}")  # 2

# Queue (FIFO) - use collections.deque for efficiency
from collections import deque
queue = deque()
queue.append(1)  # enqueue
queue.append(2)
queue.append(3)
print(f"Dequeue: {queue.popleft()}")  # 1
print(f"Dequeue: {queue.popleft()}")  # 2

# ================== MATRIX OPERATIONS ==================
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"\n=== Matrix ===")
print(f"Row 1: {matrix[0]}")
print(f"Column 1: {[row[0] for row in matrix]}")

# Transpose
transposed = list(map(list, zip(*matrix)))
print(f"Transpose: {transposed}")

# Spiral order
def spiral_order(matrix: List[List[int]]) -> List[int]:
    """Get spiral order of matrix"""
    if not matrix:
        return []
    
    result = []
    while matrix:
        # Top row
        result.extend(matrix.pop(0))
        # Right column
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        # Bottom row (reversed)
        if matrix:
            result.extend(matrix.pop()[::-1])
        # Left column (reversed)
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    
    return result

# ================== COMPARATORS ==================
print("\n=== Comparators ===")

# Sort by multiple keys - tuples work naturally
pairs = [(1, 5), (3, 2), (5, 1), (1, 3)]
print(f"Sort: {sorted(pairs)}")  # Sorts by first, then second

# Named tuple sort
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
points = [Point(1, 5), Point(3, 2), Point(1, 3)]
print(f"Sort points: {sorted(points)}")

# ================== COUNTER ==================
from collections import Counter

words = ["hello", "world", "hello", "python", "hello"]
counter = Counter(words)
print(f"\n=== Counter ===")
print(f"Counts: {counter}")
print(f"Most common: {counter.most_common(2)}")
print(f"hello count: {counter['hello']}")

# Update
counter.update(["python", "python"])
print(f"After update: {counter}")