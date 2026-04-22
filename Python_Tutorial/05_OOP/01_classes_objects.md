# Classes and Objects

## What is OOP?
Object-Oriented Programming - organize code using objects.

## What is a Class?
A blueprint for creating objects. Like a form/form.

## Creating a Class
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"Hi, I'm {self.name}")
```

## Creating Object
```python
student1 = Student("Krrish", 15)
student1.intro()
```

## More Methods
```python
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result
    
calc = Calculator()
print(calc.add(5))
print(calc.add(3))
```

## Variables in Class
```python
class Student:
    school_name = "DAV Public"  # Class variable
    
    def __init__(self, name):
        self.name = name  # Instance variable
        
student = Student("Krrish")
print(student.school_name)
```