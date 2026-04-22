# Advanced Conditional Logic and Pattern Matching

# ================== BASIC CONDITIONALS ==================
age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Ternary operator (inline if-else)
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# ================== CHAINED COMPARISONS ==================
x = 5
# Check if x is between 1 and 10 (multiple comparisons in one line)
if 1 <= x <= 10:
    print("x is between 1 and 10")

# Multiple conditions
has_income = True
has_credit = False
has_collateral = True

# AND - all must be true
if has_income and has_credit:
    print("Eligible for loan")

# OR - at least one must be true
if has_income or has_credit or has_collateral:
    print("Some qualification met")

# ================== MATCH-CASE (Python 3.10+) ==================
# Similar to switch-case in other languages
status_code = 200

# match status_code:
#     case 200:
#         print("OK")
#     case 404:
#         print("Not Found")
#     case 500:
#     case 502:
#         print("Server Error")
#     case _:
#         print("Unknown")

# ================== TRUTHY AND FALSY VALUES ==================
# Falsy values: None, 0, "", [], {}, set()
# Truthy values: everything else

# Check for empty string
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("Hello, Guest")

# Check for empty list
items = []
if items:
    print(f"You have {len(items)} items")
else:
    print("No items")

# Check for None (important for optional values)
value = None
if value is not None:
    print(f"Value: {value}")
else:
    print("No value")

# ================== SHORT-CIRCUIT EVALUATION ==================
# and/or with short-circuit (stops evaluating as soon as result is determined)

# and: returns first falsy or last value
result = True and True and False and True
print(f"True and True and False and True = {result}")  # False
result = True and True and True
print(f"True and True and True = {result}")  # True

# or: returns first truthy or last value
result = False or False or True or False
print(f"False or False or True or False = {result}")  # True

# Practical: provide default value
name = ""
display_name = name or "Guest"
print(f"Display name: {display_name}")

# ================== NESTED CONDITIONALS ==================
score = 85
if score >= 60:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    else:
        grade = "C"
else:
    grade = "F"
print(f"Grade: {grade}")

# More efficient (single if-elif chain)
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# ================== LOGICAL OPERATIONS ==================
# XOR (Exclusive OR) - true when exactly one is true
a = True
b = False
xor = (a and not b) or (not a and b)
print(f"True XOR False = {xor}")

def xor_operation(x: bool, y: bool) -> bool:
    return bool(x) != bool(y)

# ================== IDENTITY VS EQUALITY ==================
# is vs == 
# == checks value equality
# is checks memory address (identity)

a = [1, 2, 3]
b = [1, 2, 3]
print(f"a == b: {a == b}")  # True (same values)
print(f"a is b: {a is b}")  # False (different objects)

c = a
print(f"a is c: {a is c}")  # True (same object)

# Use is for None comparison (not ==)
value = None
if value is None:
    print("value is None")

# ================== DECISION TREES ==================
def get_ticket_price(age: int, student: bool, member: bool) -> float:
    """Calculate ticket price based on multiple factors"""
    base_price = 100
    
    # Age discount
    if age < 12:
        discount = 0.5
    elif age > 65:
        discount = 0.3
    else:
        discount = 0
    
    # Student discount (additional)
    if student:
        discount += 0.2
    
    # Member discount (additional)
    if member:
        discount += 0.15
    
    # Cap discount at 100%
    discount = min(discount, 1.0)
    
    return base_price * (1 - discount)

print(f"Ticket price: {get_ticket_price(15, True, False)}")

# ================== VALIDATION PATTERNS ==================
def validate_user_input(username: str, age: int, email: str) -> tuple[bool, List[str]]:
    """Validate user input and return errors"""
    errors = []
    
    # Username validation
    if not username:
        errors.append("Username required")
    elif len(username) < 3:
        errors.append("Username must be 3+ characters")
    elif len(username) > 20:
        errors.append("Username must be 20 or fewer characters")
    elif not username.isalnum() and "_" not in username:
        errors.append("Username must be alphanumeric")
    
    # Age validation
    if age < 0:
        errors.append("Age cannot be negative")
    elif age < 13:
        errors.append("Must be 13 or older")
    elif age > 150:
        errors.append("Invalid age")
    
    # Email validation
    if "@" not in email:
        errors.append("Invalid email format")
    
    return (len(errors) == 0, errors)

valid, errors = validate_user_input("john_doe", 15, "john@example.com")
print(f"Valid: {valid}, Errors: {errors}")

# ================== PATTERN MATCHING (Dict) ==================
def get_day_type(day: str) -> str:
    """Get type of day"""
    weekend_days = {"saturday", "sunday"}
    days_off = {**weekend_days, "holiday"}
    
    if day.lower() in weekend_days:
        return "Weekend"
    elif day.lower() in days_off:
        return "Day Off"
    else:
        return "Weekday"

# ================== GUARD CLAUSES ==================
def process_user(user: dict) -> str:
    """Process user with early returns (guard clauses)"""
    
    # Guard clauses - check invalid conditions first
    if not user:
        return "No user data"
    
    if not user.get("name"):
        return "No name"
    
    if user.get("age", 0) < 18:
        return "Too young"
    
    # Main logic
    return f"Processing {user['name']}"

# ================== RECURSIVE CONDITIONALS ==================
def fizzbuzz(n: int) -> str:
    """FizzBuzz problem"""
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

# Test
for i in range(1, 16):
    print(fizzbuzz(i), end=" ")
print()

# ================== CALCULATOR WITH CONDITIONALS ==================
def advanced_calc(a: float, op: str, b: float) -> Optional[float]:
    """Calculator with error handling"""
    
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            print("Error: Division by zero")
            return None
        return a / b
    elif op == "**":
        return a ** b
    elif op == "//":
        if b == 0:
            print("Error: Division by zero")
            return None
        return a // b
    elif op == "%":
        return a % b
    else:
        print(f"Unknown operator: {op}")
        return None

print(f"10 + 5 = {advanced_calc(10, '+', 5)}")
print(f"10 / 0 = {advanced_calc(10, '/', 0)}")
print(f"2 ** 10 = {advanced_calc(2, '**', 10)}")