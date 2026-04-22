# Dictionary Practice

# Create a dictionary
person = {
    "name": "Krrish",
    "age": 15,
    "city": "Delhi"
}

print("Person:", person)

# Access values
print("Name:", person["name"])
print("Age:", person.get("age"))

# Add new key-value
person["school"] = "DAV Public School"
print("After adding:", person)

# Modify
person["age"] = 16
print("After modifying:", person)

# Loop through
print("\nAll details:")
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary with marks
marks = {
    "Math": 90,
    "Science": 85,
    "English": 78,
    "History": 92
}

print("\nMarks:", marks)

# Calculate average
total = sum(marks.values())
average = total / len(marks)
print(f"Average: {average}")

# Your turn - Find highest and lowest
highest = max(marks.values())
lowest = min(marks.values())
print(f"Highest: {highest}, Lowest: {lowest}")

# Find which subject
for subject, mark in marks.items():
    if mark == highest:
        print(f"Best subject: {subject}")