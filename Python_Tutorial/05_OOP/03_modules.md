# Modules

## What is a Module?
A file containing Python code. Import it to use in other files.

## Built-in Modules (Come with Python)
```python
import math
print(math.sqrt(16))   # 4.0

import random
print(random.randint(1, 10))

import datetime
print(datetime.date.today())
```

## Import Styles
```python
# Import entire module
import math
print(math.sqrt(16))

# Import specific function
from math import sqrt
print(sqrt(16))

# Import with alias
import math as m
print(m.sqrt(16))

# Import everything (not recommended)
from math import *
```

## Creating Your Module
```python
# Save as mymodule.py
def greet(name):
    return f"Hello, {name}!"

# Use it
import mymodule
print(mymodule.greet("Krrish"))
```

## Module Search Path
Python looks for modules in:
1. Current directory
2. Python's built-in modules
3. Path in sys.path

```python
import sys
print(sys.path)
```

## Useful Built-in Modules
| Module | What it does |
|--------|-------------|
| math | Math functions |
| random | Random numbers |
| datetime | Dates and times |
| os | Operating system |
| json | JSON handling |
| re | Regular expressions |