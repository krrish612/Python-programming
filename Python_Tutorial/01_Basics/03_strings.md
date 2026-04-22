# Strings - Working with Text

## What is a String?
String = Text inside quotes

```python
name = "Krrish"
message = 'Hello friend'
empty = ""
```

## Combining Strings (Concatenation)

```python
first = "Hello"
second = "World"
combined = first + " " + second
print(combined)  # Hello World
```

## String Methods (Built-in Tools)

```python
text = "hello python"

print(text.upper())       # HELLO PYTHON
print(text.lower())       # hello python
print(text.capitalize())  # Hello python
print(text.replace("python", "world")) # hello world
```

## Getting Parts (Slicing)

```python
word = "Python"
print(word[0])    # P (first letter)
print(word[1])    # y (second letter)
print(word[-1])  # n (last letter)
print(word[0:3])  # Pyt (first to 3rd)
```

## Checking Content

```python
text = "Hello"
print("lo" in text)    # True (lo is in Hello)
print("hi" in text)   # False
print(len(text))     # 5 (length)
```

## f-Strings (Insert Variables)

```python
name = "Krrish"
age = 15
print(f"My name is {name} and I am {age} years old")