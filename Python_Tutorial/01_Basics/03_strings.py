# Advanced String Operations and Methods

# ================== STRING CREATION ==================
# Single/double/triple quotes - triple quotes for multi-line strings
single = 'Hello'
double = "Hello"
multi_line = """This is a
multi-line string"""

# Raw string (ignores escape characters)
path = r"C:\Users\Name\nFolder"  # Treats \n as literal characters

# String from bytes
text = b"Hello".decode()       # Convert bytes to string
byte_data = "Hello".encode() # Convert string to bytes

# ================== INDEXING & SLICING ==================
word = "Python"
print(f"=== Indexing ===")
print(f"word = '{word}'")
print(f"word[0] = '{word[0]}'")         # First: 'P'
print(f"word[-1] = '{word[-1]}'")      # Last: 'n'
print(f"word[0:3] = '{word[0:3]}'")      # First 3: 'Pyt'
print(f"word[:3] = '{word[:3]}'")      # Start to 3: 'Pyt'
print(f"word[2:] = '{word[2:]}'")      # 2 to end: 'thon'
print(f"word[::2] = '{word[::2]}'")    # Every 2nd: 'Pto'
print(f"word[::-1] = '{word[::-1]}'")  # Reverse: 'nohtyP'

# ================== STRING METHODS ==================
message = "  Hello Python World  "
print(f"\n=== Methods ===")
print(f"Original: '{message}'")
print(f"strip(): '{message.strip()}'")            # Remove whitespace
print(f"lower(): '{message.lower()}'")           # All lowercase
print(f"upper(): '{message.upper()}'")           # All uppercase
print(f"capitalize(): '{message.strip().capitalize()}'")  # First char capitalize
print(f"title(): '{message.strip().title()}'")  # Each word capitalize
print(f"swapcase(): '{message.swapcase()}'")    # Swap case

# Search and Replace
text = "I love programming in Python"
print(f"\n=== Search & Replace ===")
print(f"find('Python'): {text.find('Python')}")      # Index: 26
print(f"find('Java'): {text.find('Java')}")          # -1 (not found)
print(f"index('Python'): {text.index('Python')}")      # Index: 26 (raises error if not found)
print(f"count('Python'): {text.count('Python')}")    # Count: 2
print(f"replace('Python', 'Java'): {text.replace('Python', 'Java')}")

# Split and Join
sentence = "apple,banana,cherry,mango"
print(f"\n=== Split & Join ===")
print(f"split(','): {sentence.split(',')}")   # List
fruits = ["apple", "banana", "cherry"]
print(f"join: {','.join(fruits)}")           # String

# Check methods (return True/False)
test = "Hello123"
print(f"\n=== Check Methods ===")
print(f"'Hello123'.isalpha(): {test.isalpha()}")        # False (has digits)
print(f"'Hello123'.isdigit(): {test.isdigit()}")       # False
print(f"'hello'.islower(): {'hello'.islower()}")        # True
print(f"'HELLO'.isupper(): {'HELLO'.isupper()}")        # True
print(f"'Hello World'.istitle(): {'Hello World'.istitle()}")  # True
print(f"'   '.isspace(): {'   '.isspace()}")          # True
print(f"endswith('lo'): {'Hello'.endswith('lo')}")    # True
print(f"startswith('He'): {'Hello'.startswith('He')}") # True

# ================== STRING FORMATTING ==================
name = "Krrish"
age = 15

# f-strings (Python 3.6+) - recommended
print(f"\n=== Formatting ===")
print(f"f-string: I'm {name}, age {age}")

# .format() method
print("format() method: I'm {}, age {}".format(name, age))
print("format() with index: {0} is {1} years old".format(name, age))

# % formatting (older style)
print("%% style: I'm %s, age %d" % (name, age))

# f-string with conditions
score = 85
grade = "Pass" if score >= 50 else "Fail"
print(f"Grade: {grade}")

# f-string with expressions
print(f"Age in 5 years: {age + 5}")

# Padding and alignment
print(f"\n=== Padding ===")
print(f"{'hello':<10}")     # Left-align: 'hello     '
print(f"{'hello':>10}")    # Right-align: '     hello'
print(f"{'hello':^10}")    # Center: '  hello   '
print(f"{'hello':^10}")    # Center: '  hello   '
print(f"{42:05d}")        # Zero-pad: '00042'

# ================== ESCAPE SEQUENCES ==================
print(f"\n=== Escape Sequences ===")
print("Newline: line1\nline2")
print("Tab: col1\tcol2")
print("Backslash: \\")
print("Quote: \"")
print("Unicode: \u0041 for A")

# ================== REGEX-LIKE PATTERNS ==================
# Using endswith/startswith with tuple
filename = "document.pdf"
print(f"\n=== Patterns ===")
print(f"Ends with .pdf: {filename.endswith(('.pdf', '.doc'))}")
print(f"Starts with doc: {filename.startswith('doc')}")

# ================== PRACTICAL EXAMPLES ==================
print(f"\n=== Practical Examples ===")

# Palindrome check
word = "radar"
is_palindrome = word == word[::-1]
print(f"'{word}' is palindrome: {is_palindrome}")

# Count vowels
text = "Hello World"
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)
print(f"Vowels in '{text}': {vowel_count}")

# Reverse words
sentence = "Hello World"
reversed_sentence = " ".join(sentence.split()[::-1])
print(f"Reversed words: {reversed_sentence}")

# Check anagram (same letters, different order)
word1 = "listen"
word2 = "silent"
is_anagram = sorted(word1) == sorted(word2)
print(f"'{word1}' and '{word2}' are anagrams: {is_anagram}")

# Valid email check (simple)
email = "user@example.com"
has_at = "@" in email
has_dot = "." in email.split("@")[1] if has_at else False
print(f"Valid email: {has_at and has_dot}")