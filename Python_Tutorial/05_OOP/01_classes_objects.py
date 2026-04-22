# Class and Object Practice

# Example 1: Simple class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"Hi, I'm {self.name}, {self.age} years old")

student1 = Student("Krrish", 15)
student1.intro()

# Example 2: Bank Account
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds!")
    
    def show_balance(self):
        print(f"Balance: {self.balance}")

# Test it
account = BankAccount("Krrish", 1000)
account.deposit(500)
account.withdraw(200)
account.show_balance()

# Example 3: Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")