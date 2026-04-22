# Dictionaries - Key-Value Pairs

## What is a Dictionary?
Like a real dictionary - word (key) has meaning (value).

```python
student = {
    "name": "Krrish",
    "age": 15,
    "grade": "10th"
}
```

## Accessing Values
```python
print(student["name"])      # Krrish
print(student.get("age"))   # 15
```

## Adding/Modifying
```python
student["school"] = "DAV"  # Add new
student["age"] = 16         # Modify
```

## Dictionary Methods
```python
print(student.keys())     # All keys
print(student.values())   # All values
print(student.items())    # All pairs
```

## Loop Through Dictionary
```python
for key, value in student.items():
    print(f"{key}: {value}")
```

## Practical Example
```python
marks = {
    "Math": 90,
    "Science": 85,
    "English": 78
}

total = sum(marks.values())
print(f"Total: {total}")
```