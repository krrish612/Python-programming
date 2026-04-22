# Getting User Input

## input() - Ask User for Information

```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

## Converting Input
`input()` always returns text (string). Convert as needed:

```python
age_text = input("Your age? ")
age = int(age_text)        # Convert to number

price = float(input("Price? "))  # For decimals
```

## Type Conversion

```python
# String to Integer
num = int("10")      # 10

# Integer to String
text = str(10)      # "10"

# String to Float
decimal = float("3.14")  # 3.14
```

## Practical Example

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hi {name}!")
print(f"You will be {age + 5} years old in 5 years")
```