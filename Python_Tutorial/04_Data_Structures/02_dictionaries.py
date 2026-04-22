# Advanced Dictionary Operations and Patterns

from typing import Dict, List, Any, Optional, Callable
from collections import defaultdict, Counter, OrderedDict
import json

# ================== BASIC OPERATIONS ==================
person = {"name": "Krrish", "age": 15, "city": "Delhi"}
print(f"Person: {person}")
print(f"Name: {person['name']}")
print(f"Get with default: {person.get('country', 'Unknown')}")

# ================== DICTIONARY COMPREHENSIONS ==================
# Basic
squares = {x: x**2 for x in range(1, 6)}
print(f"\nSquares: {squares}")

# With condition
word_lengths = {word: len(word) for word in ["hello", "world", "python"] if len(word) > 4}
print(f"Word lengths: {word_lengths}")

# From two lists
keys = ["name", "age", "city"]
values = ["Krrish", 15, "Delhi"]
data = dict(zip(keys, values))
print(f"From zip: {data}")

# ================== DICT METHODS ==================
print("\n=== Dict Methods ===")
person = {"name": "Krrish", "age": 15}

# Keys, values, items
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Update (merge or add)
person.update({"age": 16, "school": "DAV"})
print(f"After update: {person}")

# Pop (remove and return)
age = person.pop("age")
print(f"Popped age: {age}")

# Pop item (random pair)
last_item = person.popitem()
print(f"Pop item: {last_item}")

# Set default (if key not exists)
person = {}
person.setdefault("name", "Guest")
person.setdefault("age", 0)
print(f"Set default: {person}")

# ================== NESTED DICTIONS ==================
print("\n=== Nested Dictionaries ===")
students = {
    "Alice": {"age": 15, "marks": {"math": 90, "science": 85}},
    "Bob": {"age": 16, "marks": {"math": 75, "science": 80}}
}
print(f"Students: {students}")
print(f"Alice's math: {students['Alice']['marks']['math']}")

# Add to nested
students["Charlie"] = {"age": 15, "marks": {}}
students["Charlie"]["marks"]["english"] = 95

# ================== DEFAULTDICT ==================
from collections import defaultdict

# Auto-create missing keys with default value
dd = defaultdict(list)
dd["fruits"].append("apple")
dd["fruits"].append("banana")
dd["numbers"].append(1)
print(f"\n=== Defaultdict ===")
print(f"Defaultdict: {dict(dd)}")

# Counter as defaultdict
word_count = defaultdict(int)
words = "hello world hello python hello"
for word in words.split():
    word_count[word] += 1
print(f"Word count: {dict(word_count)}")

# ================== ORDERED DICT ==================
from collections import OrderedDict

# Maintains insertion order (Python 3.7+: regular dict also does)
od = OrderedDict()
od["first"] = 1
od["second"] = 2
od["third"] = 3
print(f"\n=== OrderedDict ===")
print(f"Order: {list(od.keys())}")

# Move to end
od.move_to_end("first")
print(f"After move: {list(od.keys())}")

# Pop last
last = od.popitem(last=True)
print(f"Pop last: {last}")

# ================== MERGING DICTIONARIES ==================
print("\n=== Merging ===")

# Python 3.9+ (| and |=)
# dict1 | dict2  # Merge

# Python 3.5+ (** unpacking)
merged = {**{"a": 1}, **{"b": 2}}
print(f"Merged: {merged}")

# Update method
dict1 = {"a": 1}
dict1.update({"b": 2, "a": 10})  # Overwrites existing
print(f"After update: {dict1}")

# ================== DICTIONARY OPERATIONS ==================
marks = {"math": 90, "science": 85, "english": 78}

# Check existence
print(f"\n=== Operations ===")
print(f"Has math: {'math' in marks}")

# Get all keys/values
print(f"Keys: {list(marks.keys())}")
print(f"Values: {list(marks.values())}")
print(f"Items: {list(marks.items())}")

# Filter
passing = {k: v for k, v in marks.items() if v >= 60}
print(f"Passing: {passing}")

# ================== INVERT DICTIONARY ==================
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(f"Inverted: {inverted}")

# Handle duplicate values
original = {"a": 1, "b": 2, "c": 1}
inverted = defaultdict(list)
for k, v in original.items():
    inverted[v].append(k)
inverted = dict(inverted)
print(f"Inverted (list): {inverted}")

# ================== GROUP BY ==================
from itertools import groupby

# Group by first letter
words = ["apple", "banana", "apricot", "blueberry", "cherry"]
words.sort(key=lambda x: x[0])
grouped = {k: list(v) for k, v in groupby(words, key=lambda x: x[0])}
print(f"\n=== Group By ===")
print(f"Grouped: {grouped}")

# ================== COUNTER FOR STATISTICS ==================
from collections import Counter

marks = [90, 85, 78, 92, 88, 90, 85, 78]
counter = Counter(marks)
print(f"\n=== Counter ===")
print(f"Most common: {counter.most_common(3)}")
print(f"90 count: {counter[90]}")

# Operations
marks2 = [90, 85, 80]
counter2 = Counter(marks2)
combined = counter + counter2
print(f"Combined: {dict(combined)}")

# ================== JSON DICTIONARY ==================
# Convert to/from JSON
data = {"name": "Krrish", "age": 15, " hobbies": ["coding", "gaming"]}

json_str = json.dumps(data)
print(f"\n=== JSON ===")
print(f"JSON: {json_str}")

parsed = json.loads(json_str)
print(f"Parsed: {parsed}")

# Pretty print
print(json.dumps(data, indent=2))

# ================== SORTED DICTIONARY ==================
person = {"Zebra": 3, "Apple": 1, "Mango": 2}

# Sort by keys
sorted_by_key = dict(sorted(person.items()))
print(f"\n=== Sorted ===")
print(f"By key: {sorted_by_key}")

# Sort by values
sorted_by_value = dict(sorted(person.items(), key=lambda x: x[1]))
print(f"By value: {sorted_by_value}")
print(f"By value: {sorted(person.items(), key=lambda x: x[1])}")

# ================== PRACTICAL PATTERNS ==================
print("\n=== Practical Patterns ===")

# Frequency map
text = "hello world hello python"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(f"Frequency: {freq}")

# Using defaultdict
freq = defaultdict(int)
for word in text.split():
    freq[word] += 1
print(f"Frequency: {dict(freq)}")

# Lookup table
def get_day_type(day: str) -> str:
    """Get day type from dictionary"""
    days_off = {"saturday", "sunday", "holiday"}
    return days_off.get(day.lower(), "Weekday")

print(f"Day type: {get_day_type('sunday')}")

# Nested lookup
data = {"user": {"profile": {"email": "test@example.com"}}}
email = data.get("user", {}).get("profile", {}).get("email", "N/A")
print(f"Email: {email}")

# ================== DICTIONARY VIEW ==================
person = {"name": "Krrish", "age": 15}

# Views reflect changes
keys = person.keys()
print(f"\n=== Views ===")
print(f"Keys: {keys}")
person["city"] = "Delhi"
print(f"Keys after add: {keys}")  # Automatically updated

# ================== FROMKEYS ==================
# Create dict with same value
keys = ["a", "b", "c"]
value = 0
new_dict = dict.fromkeys(keys, value)
print(f"\n=== From Keys ===")
print(f"New dict: {new_dict}")

# ================== COPY ==================
original = {"name": "Krrish", "marks": [90, 85]}
shallow = original.copy()
shallow["name"] = "Bob"
shallow["marks"].append(80)
print(f"\n=== Copy ===")
print(f"Original: {original}")  # marks also changed!

# Deep copy
import copy
original = {"name": "Krrish", "marks": [90, 85]}
deep = copy.deepcopy(original)
deep["marks"].append(80)
print(f"Original after deep: {original}")  # Unchanged

# ================== PRACTICAL EXAMPLE ==================
print("\n=== Practical Example ===")

# Student gradebook
gradebook = {}
gradebook["Alice"] = {"math": 90, "science": 85}
gradebook["Bob"] = {"math": 75, "science": 80}

# Average for each student
for student, marks in gradebook.items():
    avg = sum(marks.values()) / len(marks)
    print(f"{student}: {avg:.2f}")

# Find highest subject
all_subjects = {}
for marks in gradebook.values():
    for subject, score in marks.items():
        if subject not in all_subjects or score > all_subjects[subject]:
            all_subjects[subject] = score
print(f"Highest per subject: {all_subjects}")