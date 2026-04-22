# Packages

## What is a Package?
A folder containing multiple modules. Like a folder of related files.

## Structure
```
my_package/
    __init__.py      # Makes it a package
    module1.py
    module2.py
    subfolder/
        __init__.py
        module3.py
```

## __init__.py
Makes Python treat the folder as a package. Can be empty or contain initialization code.

## Using Packages
```python
# Import from package
from my_package import module1
module1.my_function()

# Import specific
from my_package.module1 import my_function

# Import with alias
import my_package.module1 as m1
```

## Example Package
```
math_utils/
    __init__.py
    basic.py
    advanced.py
```

```python
# basic.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# advanced.py
def power(base, exp):
    return base ** exp
```

```python
# Using the package
from math_utils import basic, advanced
print(basic.add(5, 3))
print(advanced.power(2, 3))
```

## Why Use Packages?
1. Organize code
2. Avoid name conflicts
3. Share reusable code
4. Build large applications