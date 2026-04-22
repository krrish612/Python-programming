# Inheritance

## What is Inheritance?
One class can inherit from another. Child class gets parent's features.

## Basic Example
```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Some sound")

# Child class
class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog("Buddy")
dog.speak()  # Woof!
```

## Using Parent's Methods
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent __init__
        self.breed = breed

dog = Dog("Buddy", "Labrador")
print(dog.name, dog.breed)
```

## Multiple Levels
```python
class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass
```

## Multiple Parents
```python
class Actor:
    def act(self):
        print("Acting")

class Singer:
    def sing(self):
        print("Singing")

class Star(Actor, Singer):
    pass

star = Star()
star.act()
star.sing()
```

## Check Inheritance
```python
print(issubclass(Dog, Animal))  # True
print(issubclass(Dog, int))   # False