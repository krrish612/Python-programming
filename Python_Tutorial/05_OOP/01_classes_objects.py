# Advanced Object-Oriented Programming

from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any
from functools import wraps
import math

# ================== BASIC CLASS ==================
class Person:
    """Basic class with __init__ and __str__"""
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f"{self.name}, {self.age}"
    
    def __repr__(self) -> str:
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Krrish", 15)
print(f"Person: {person}")
print(f"repr: {repr(person)}")

# ================== ENCAPSULATION ==================
class BankAccount:
    """Class demonstrating encapsulation"""
    
    def __init__(self, owner: str, balance: float = 0):
        self.__balance = balance  # Private (name mangling)
        self.__owner = owner
    
    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}")
        else:
            print("Invalid amount")
    
    def withdraw(self, amount: float) -> bool:
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}")
            return True
        print("Insufficient funds")
        return False
    
    def get_balance(self) -> float:
        return self.__balance
    
    def __str__(self) -> str:
        return f"{self.__owner}: ${self.__balance:.2f}"

account = BankAccount("Krrish", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Balance: {account.get_balance()}")

# ================== INHERITANCE ==================
class Animal(ABC):  # Abstract base class
    """Animal base class"""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def make_sound(self) -> str:
        """Abstract method - must be overridden"""
        pass
    
    def move(self) -> str:
        return f"{self.name} moves"

class Dog(Animal):
    """Dog inherits from Animal"""
    
    def __init__(self, name: str, breed: str):
        super().__init__(name)  # Call parent __init__
        self.breed = breed
    
    def make_sound(self) -> str:
        return "Woof!"
    
    def fetch(self) -> str:
        return f"{self.name} fetches the ball"

class Cat(Animal):
    """Cat inherits from Animal"""
    
    def make_sound(self) -> str:
        return "Meow!"
    
    def climb(self) -> str:
        return f"{self.name} climbs the tree"

# Polymorphism - same method different behavior
animals = [Dog("Buddy", "Golden Retriever"), Cat("Whiskers")]
for animal in animals:
    print(f"{animal.name}: {animal.make_sound()}")

# ================== MULTIPLE INHERITANCE ==================
class Flyable:
    def fly(self) -> str:
        return "Flying!"

class Swimmable:
    def swim(self) -> str:
        return "Swimming!"

class Duck(Animal, Flyable, Swimmable):
    """Duck inherits from multiple classes"""
    
    def make_sound(self) -> str:
        return "Quack!"

duck = Duck("Donald")
print(f"{duck.name}: {duck.make_sound()}, {duck.fly()}, {duck.swim()}")

# Method Resolution Order (MRO)
print(f"\nMRO: {Duck.__mro__}")

# ================== MULTI-LEVEL INHERITANCE ==================
class Vehicle:
    def __init__(self, brand: str):
        self.brand = brand
    
    def start(self) -> str:
        return f"{self.brand} starts"

class Car(Vehicle):
    def __init__(self, brand: str, model: str):
        super().__init__(brand)
        self.model = model
    
    def drive(self) -> str:
        return f"{self.brand} {self.model} drives"

class ElectricCar(Car):
    def __init__(self, brand: str, model: str, battery: int):
        super().__init__(brand, model)
        self.battery = battery
    
    def charge(self) -> str:
        return f"Charging {self.battery}kWh battery"

tesla = ElectricCar("Tesla", "Model 3", 75)
print(f"{tesla.brand} {tesla.model}: {tesla.drive()}, {tesla.charge()}")

# ================== COMPOSITION ==================
class Engine:
    def start(self) -> str:
        return "Engine starts"

class Car2:
    def __init__(self):
        self.engine = Engine()  # Composition: HAS-A relationship
    
    def start(self) -> str:
        return self.engine.start()

car2 = Car2()
print(f"Car2: {car2.start()}")

# ================== DUCKS TYPING (Protocol) ==================
# Python doesn't enforce interfaces like Java
# Duck typing: "If it walks like a duck and quacks like a duck..."

class Bird:
    def quack(self) -> str:
        return "Quack!"

class Person2:
    def quack(self) -> str:
        return "I can quack too!"

def make_quack(obj) -> str:
    return obj.quack()  # Works if obj has quack() method

# Both work!
print(f"Bird: {make_quack(Bird())}")
print(f"Person: {make_quack(Person2())}")

# ================== CLASS VARIABLES ==================
class Student:
    school_name = "DAV Public School"  # Class variable (shared)
    total_students = 0
    
    def __init__(self, name: str):
        self.name = name  # Instance variable
        Student.total_students += 1
    
    @classmethod
    def get_total(cls) -> int:
        """Class method - can access class variables"""
        return cls.total_students
    
    @staticmethod
    def validate_age(age: int) -> bool:
        """Static method - doesn't need instance or class"""
        return 0 <= age <= 150

s1 = Student("Alice")
s2 = Student("Bob")
print(f"Total students: {Student.get_total()}")
print(f"Valid age 15: {Student.validate_age(15)}")

# ================== SPECIAL METHODS ==================
class Vector:
    """Demonstrating special/magic methods"""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: float) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar: float) -> 'Vector':
        return self.__mul__(scalar)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y
    
    def __len__(self) -> int:
        return 2
    
    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Index out of range")
    
    def __abs__(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(f"v1: {v1}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 2: {v1 * 2}")
print(f"2 * v1: {2 * v1}")
print(f"v1 == v2: {v1 == v2}")
print(f"len(v1): {len(v1)}")
print(f"v1[0]: {v1[0]}")
print(f"|v1|: {abs(v1)}")

# ================== PROPERTIES ==================
class Temperature:
    """Temperature with property"""
    
    def __init__(self, celsius: float):
        self.celsius = celsius
    
    @property
    def fahrenheit(self) -> float:
        return (self.celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value: float):
        self.celsius = (value - 32) * 5/9

temp = Temperature(0)  # Freezing point
print(f"Celsius: {temp.celsius}")
print(f"Fahrenheit: {temp.fahrenheit}")
temp.fahrenheit = 212  # Boiling point
print(f"After setter - Celsius: {temp.celsius}")

# ================== DESCRIPTOR ==================
class Positive:
    """Descriptor that enforces positive values"""
    
    def __init__(self, name: str):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        return getattr(obj, f"_positive_{self.name}", 0)
    
    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f"{self.name} must be positive")
        setattr(obj, f"_positive_{self.name}", value)

class PositiveValue:
    age = Positive("age")
    score = Positive("score")
    
    def __init__(self, age: int, score: int):
        self.age = age
        self.score = score

pv = PositiveValue(15, 100)
print(f"Age: {pv.age}, Score: {pv.score}")
# pv.age = -5  # This would raise ValueError

# ================== FACTORY PATTERN ==================
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height

class ShapeFactory:
    """Factory to create shapes"""
    
    @staticmethod
    def create_shape(shape_type: str, **kwargs) -> Shape:
        shapes = {
            "circle": Circle,
            "rectangle": Rectangle
        }
        return shapes[shape_type](**kwargs)

circle = ShapeFactory.create_shape("circle", radius=5)
rect = ShapeFactory.create_shape("rectangle", width=4, height=3)
print(f"Circle area: {circle.area():.2f}")
print(f"Rectangle area: {rect.area():.2f}")

# ================== SINGLETON PATTERN ==================
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.data = {}

s1 = Singleton()
s2 = Singleton()
print(f"Same instance: {s1 is s2}")

# ================== ABSTRACT BASE CLASS ==================
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Abstract payment processor"""
    
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass
    
    @abstractmethod
    def refund(self, transaction_id: str) -> bool:
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing ${amount} via Credit Card")
        return True
    
    def refund(self, transaction_id: str) -> bool:
        print(f"Refunding transaction {transaction_id}")
        return True

processor = CreditCardProcessor()
processor.process_payment(100.00)

# ================== MIXIN CLASSES ==================
class DebugMixin:
    """Mixin that adds debug functionality"""
    
    def debug(self) -> str:
        return f"DEBUG: {self.__class__.__name__} - {self.__dict__}"

class Logged(Animal, DebugMixin):
    """Animal with debug logging"""
    
    def __init__(self, name: str):
        super().__init__(name)
    
    def make_sound(self) -> str:
        self.debug()
        return "Sound!"

# ================== DATA CLASS (Python 3.7+) ==================
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    _id: int = field(default=0, repr=False)  # Won't show in repr
    
    def distance_to(self, other: 'Point') -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

p1 = Point(0, 0)
p2 = Point(3, 4)
print(f"Point: {p1}")
print(f"Distance: {p1.distance_to(p2)}")

# ================== PRACTICAL EXAMPLE ==================
class Inventory:
    """Product inventory system"""
    
    def __init__(self):
        self._items: Dict[str, int] = {}
    
    def add_item(self, name: str, quantity: int) -> None:
        self._items[name] = self._items.get(name, 0) + quantity
    
    def remove_item(self, name: str, quantity: int) -> bool:
        if self._items.get(name, 0) >= quantity:
            self._items[name] -= quantity
            if self._items[name] == 0:
                del self._items[name]
            return True
        return False
    
    def get_quantity(self, name: str) -> int:
        return self._items.get(name, 0)
    
    def __str__(self) -> str:
        return "\n".join(f"{k}: {v}" for k, v in self._items.items())

inventory = Inventory()
inventory.add_item("Apple", 10)
inventory.add_item("Banana", 5)
inventory.remove_item("Apple", 3)
print(f"\nInventory:\n{inventory}")