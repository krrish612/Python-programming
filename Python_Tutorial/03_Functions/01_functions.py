# Advanced Functions: Decorators, Generators, and Design Patterns

from functools import wraps, lru_cache, reduce, partial
from typing import Callable, Optional, List, Any, Union
import time
import random

# ================== BASIC FUNCTIONS ==================
def greet(name: str) -> str:
    """Basic greeting function"""
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# ================== DEFAULT ARGUMENTS ==================
def greet_with_default(name: str = "Guest", greeting: str = "Hello") -> str:
    """Function with default parameters"""
    return f"{greeting}, {name}!"

# Mutable default warning!
# Don't do this: def bad_append(item, lst=[]) - creates same list each call
def good_append(item: Any, lst: Optional[List] = None) -> List:
    """Correct way to handle mutable defaults"""
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# ================== *ARGS AND **KWARGS ==================
def print_all(*args, **kwargs) -> None:
    """*args = positional, **kwargs = named arguments"""
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

def sum_all(*numbers: int) -> int:
    """Sum any number of arguments"""
    return sum(numbers)

def create_user(**details) -> dict:
    """Create user from keyword arguments"""
    return details

# ================== HIGHER-ORDER FUNCTIONS ==================
# Functions that take/return functions

def apply_twice(func: Callable, value: Any) -> Any:
    """Apply function twice"""
    return func(func(value))

def create_multiplier(factor: int) -> Callable:
    """Return a function that multiplies by factor"""
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier

double = create_multiplier(2)
print(f"Double 5: {double(5)}")

# ================== LAMBDA FUNCTIONS ==================
# Anonymous functions (one-liner)
square = lambda x: x ** 2
add_three = lambda a, b, c: a + b + c

# With sorted
pairs = [(1, 5), (3, 2), (5, 1)]
sorted_by_second = sorted(pairs, key=lambda x: x[1])
print(f"Sorted by second: {sorted_by_second}")

# ================== CLOSURES ==================
# Function that remembers values from enclosing scope

def make_counter():
    """Counter using closure"""
    count = 0
    
    def counter():
        nonlocal count  # Modify outer variable
        count += 1
        return count
    
    return counter

counter = make_counter()
print(f"Counter: {counter()}, {counter()}, {counter()}")

def make_power(exponent: int) -> Callable:
    """Create power function"""
    def power_fn(base: int) -> int:
        return base ** exponent
    return power_fn

square_fn = make_power(2)
cube_fn = make_power(3)
print(f"5 squared: {square_fn(5)}")
print(f"5 cubed: {cube_fn(5)}")

# ================== DECORATORS ==================
# Functions that modify other functions

def timer(func: Callable) -> Callable:
    """Decorator to time function execution"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    """Example function that takes time"""
    time.sleep(0.1)
    return "Done"

# Multiple decorators
def logger(func: Callable) -> Callable:
    """Log function calls"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
@timer
def add(a: int, b: int) -> int:
    """Add with decorators"""
    return a + b

# Decorator with arguments
def retry(max_attempts: int = 3, delay: float = 1.0):
    """Retry decorator"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3)
def unreliable():
    """Function that might fail"""
    if random.random() < 0.5:
        raise ValueError("Random failure!")
    return "Success!"

# ================== GENERATORS ==================
# Functions that yield values instead of returning

def count_up_to(n: int):
    """Generator that counts up"""
    count = 1
    while count <= n:
        yield count
        count += 1

for i in count_up_to(5):
    print(i, end=" ")
print()

def fibonacci_gen(n: int):
    """Fibonacci generator"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(f"Fibonacci: {list(fibonacci_gen(10))}")

def infinite_counter():
    """Infinite generator"""
    count = 0
    while True:
        yield count
        count += 1

# Use with next()
gen = infinite_counter()
print(f"First: {next(gen)}, Second: {next(gen)}")

# ================== BUILT-IN FUNCTOOLS ==================
# lru_cache - Memoization (cache results)
@lru_cache(maxsize=None)
def fibonacci_cached(n: int) -> int:
    """Fibonacci with memoization"""
    if n < 2:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

# reduce - Apply function cumulatively
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"\nReduce product: {product}")

# partial - Create function with some arguments preset
def power(base: int, exponent: int) -> int:
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)
print(f"5 squared: {square(5)}")
print(f"5 cubed: {cube(5)}")

# ================== RECURSIVE FUNCTIONS ==================
def factorial(n: int) -> int:
    """Recursive factorial"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci_recursive(n: int) -> int:
    """Recursive Fibonacci (slow without cache)"""
    if n < 2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# ================== TYPE HINTS ==================
# Function with full type hints
def process_items(items: List[int], transform: Callable[[int], int]) -> List[int]:
    """Process items with transformation function"""
    return [transform(item) for item in items]

result = process_items([1, 2, 3], lambda x: x * 2)
print(f"Processed: {result}")

# ================== VARIADIC FUNCTIONS ==================
def average(*numbers: float) -> Optional[float]:
    """Calculate average of any number of floats"""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

print(f"Average: {average(1, 2, 3, 4, 5)}")

# ================== ANNOTATIONS ==================
def annotated_func(x: int, y: int) -> int:
    """Function with parameter annotations"""
    return x + y

# Access annotations
print(f"Annotations: {annotated_func.__annotations__}")

# ================== ERROR HANDLING IN FUNCTIONS ==================
def safe_divide(a: float, b: float) -> Union[float, str]:
    """Divide with error handling"""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid types"

# ================== FUNCTION COMPOSITION ==================
def compose(f: Callable, g: Callable) -> Callable:
    """Compose two functions: (f ∘ g)(x) = f(g(x))"""
    return lambda x: f(g(x))

def add_one(x: int) -> int:
    return x + 1

def double(x: int) -> int:
    return x * 2

composed = compose(add_one, double)
print(f"Compose (add_one ∘ double)(5): {composed(5)}")  # 5*2+1 = 11

# ================== FUNCTION AS DATA ==================
def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    """Apply any operation to two numbers"""
    return operation(a, b)

def multiply(a: int, b: int) -> int:
    return a * b

print(f"Apply multiply: {apply_operation(5, 3, multiply)}")
print(f"Apply lambda: {apply_operation(5, 3, lambda a, b: a - b)}")

# ================== CALLABLE CHECKING ==================
print(f"\n=== Callable Check ===")
print(f"greet callable: {callable(greet)}")
print(f"123 callable: {callable(123)}")