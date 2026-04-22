# List Practice

# Create a list
fruits = ["apple", "banana", "cherry", "mango"]
print("Fruits:", fruits)

# Access items
print("First:", fruits[0])
print("Last:", fruits[-1])

# Modify
fruits[0] = "orange"
print("Modified:", fruits)

# Add items
fruits.append("grape")
fruits.insert(1, "kiwi")
print("After adding:", fruits)

# Remove items
fruits.remove("banana")
print("After removing:", fruits)

# Loop through
print("\nAll fruits:")
for fruit in fruits:
    print("-", fruit)

# List length
print("\nTotal fruits:", len(fruits))

# Check if exists
if "mango" in fruits:
    print("Mango is in the list!")

# Numbers list
numbers = [5, 2, 8, 1, 9]
print("\nNumbers:", numbers)
numbers.sort()
print("Sorted:", numbers)

# List comprehension - square numbers
squares = [x**2 for x in range(1, 6)]
print("\nSquares:", squares)

# Your turn - Average of list
marks = [85, 90, 78, 92, 88]
total = sum(marks)
average = total / len(marks)
print(f"\nMarks: {marks}")
print(f"Average: {average}")