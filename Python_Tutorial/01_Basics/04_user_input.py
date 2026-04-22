# Advanced User Input Handling and Validation

import sys
import ast
from typing import Optional, List, Tuple

# ================== BASIC INPUT ==================
def get_name() -> str:
    """Get name with default handling"""
    name = input("Enter your name: ").strip() or "Guest"
    return name

def get_age() -> int:
    """Get validated integer age"""
    while True:
        try:
            age = int(input("Enter your age: "))
            if 0 <= age <= 150:
                return age
            print("Please enter a valid age (0-150)")
        except ValueError:
            print("Invalid number. Try again.")

# ================== VALIDATION FUNCTIONS ==================
def validate_email(email: str) -> bool:
    """Check if email is valid"""
    if "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    username, domain = parts
    if not username or not domain:
        return False
    if "." not in domain:
        return False
    return True

def validate_phone(phone: str) -> bool:
    """Check if phone number is valid (10 digits)"""
    cleaned = phone.replace("-", "").replace(" ", "")
    return cleaned.isdigit() and len(cleaned) == 10

def validate_range(value: int, min_val: int, max_val: int) -> bool:
    """Check if value is in range"""
    return min_val <= value <= max_val

# ================== INPUT CONVERTERS ==================
def get_float(prompt: str) -> float:
    """Get float with validation"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_int_with_default(prompt: str, default: int) -> int:
    """Get integer with default value"""
    user_input = input(prompt).strip()
    if not user_input:
        return default
    try:
        return int(user_input)
    except ValueError:
        return default

def get_choice(prompt: str, options: List[str]) -> str:
    """Get user choice from options"""
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print(f"Invalid. Options: {', '.join(options)}")

# ================== MENU SYSTEM ==================
def display_menu(title: str, options: List[str], prompt: str = "Choose: ") -> int:
    """Display numbered menu and return selection"""
    print(f"\n=== {title} ===")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= len(options):
                return choice
            print(f"Enter 1-{len(options)}")
        except ValueError:
            print("Enter a number.")

# ================== BATCH INPUT ==================
def get_multiple_ints(prompt: str, count: int) -> List[int]:
    """Get multiple integers"""
    numbers = []
    while len(numbers) < count:
        try:
            num = int(input(f"{prompt} ({len(numbers)+1}/{count}): "))
            numbers.append(num)
        except ValueError:
            print("Invalid number.")
    return numbers

def get_comma_separated_ints(prompt: str) -> List[int]:
    """Get list of integers separated by commas"""
    while True:
        user_input = input(prompt)
        try:
            return [int(x.strip()) for x in user_input.split(",")]
        except ValueError:
            print("Invalid input. Use: 1, 2, 3")

# ================== PASSWORD INPUT (HIDDEN) ==================
def get_password(prompt: str = "Password: ") -> str:
    """Get password without displaying input"""
    password = input(prompt)
    return password

# ================== FILE INPUT ==================
def read_from_file(filename: str) -> Optional[List[str]]:
    """Read lines from file"""
    try:
        with open(filename, 'r') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None

def write_to_file(filename: str, content: str) -> bool:
    """Write content to file"""
    try:
        with open(filename, 'w') as f:
            f.write(content)
        return True
    except IOError as e:
        print(f"Error writing file: {e}")
        return False

# ================== ADVANCED CALCULATOR ==================
def parse_expression(expr: str) -> Tuple[float, str, float]:
    """Parse 'num1 op num2' format"""
    expr = expr.strip()
    operators = ['+', '-', '*', '/', '**', '//', '%']
    
    for op in operators:
        if op in expr:
            parts = expr.split(op)
            if len(parts) == 2:
                try:
                    num1 = float(parts[0].strip())
                    num2 = float(parts[1].strip())
                    return (num1, op, num2)
                except ValueError:
                    raise ValueError("Invalid numbers")
    
    raise ValueError("No operator found")

def calculate(a: float, op: str, b: float) -> Optional[float]:
    """Perform calculation"""
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else None,
        '**': lambda x, y: x ** y,
        '//': lambda x, y: x // y,
        '%': lambda x, y: x % y,
    }
    func = operations.get(op)
    if func:
        return func(a, b)
    return None

# ================== TEMPERATURE CONVERTER ==================
def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit"""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius"""
    return (f - 32) * 5/9

def kelvin_to_celsius(k: float) -> float:
    """Convert Kelvin to Celsius"""
    return k - 273.15

def celsius_to_kelvin(c: float) -> float:
    """Convert Celsius to Kelvin"""
    return c + 273.15

# ================== DEMO ==================
if __name__ == "__main__":
    print("=== Name ===")
    name = get_name()
    print(f"Hello, {name}!")
    
    print("\n=== Age ===")
    age = get_age()
    print(f"You are {age} years old")
    
    print("\n=== Menu ===")
    choice = display_menu("Main Menu", ["Start Game", "Settings", "Exit"])
    print(f"You chose option {choice}")
    
    print("\n=== Calculator ===")
    expr = input("Enter (e.g., 5 + 3): ")
    try:
        num1, op, num2 = parse_expression(expr)
        result = calculate(num1, op, num2)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")