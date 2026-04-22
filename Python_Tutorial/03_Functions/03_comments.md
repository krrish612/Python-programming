# Comments

## What Are Comments?
Notes in code that Python ignores. For humans to read.

## Single Line Comment
```python
# This is a comment
print("Hello")  # This prints Hello
```

## Multi Line Comment
```python
# This is a
# multi-line
# comment

# Or use triple quotes (docstring)
"""
This is also
a multi-line
comment
"""
```

## Why Use Comments?
1. Explain complex code
2. Remind yourself what you did
3. Help others understand your code
4. Disable code temporarily

## Types of Comments
```python
# TODO: Add more features
# FIXME: This code has a bug
# NOTE: Important information
```

## Bad vs Good Comments
```python
# Bad - obvious comment
x = x + 1  # Increment x

# Good - explains WHY
x = x + 1  # Add 1 for 0-based index
```

## Docstrings
```python
def greet(name):
    """This function greets a person."""
    return f"Hello, {name}!"
```

## When to Comment
- WHY you did something
- Complex logic
- TODO tasks
- NOT what code does (code should be clear)