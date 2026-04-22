# String Practice

# 1. Creating strings
name = "Krrish"
print("Name:", name)

# 2. Combining strings
first_name = "Krrish"
last_name = "Tripathi"
full_name = first_name + " " + last_name
print("Full name:", full_name)

# 3. String methods
message = "hello python"
print("Upper:", message.upper())
print("Lower:", message.lower())
print("Capitalize:", message.capitalize())

# 4. Replacing
text = "I love programming"
new_text = text.replace("programming", "Python")
print("Replaced:", new_text)

# 5. Getting parts
word = "Python"
print("First letter:", word[0])
print("Last letter:", word[-1])
print("First 3:", word[0:3])

# 6. Checking
print("'thon' in Python:", "thon" in word)
print("Length:", len(word))

# 7. f-Strings
name = "Krrish"
age = 15
country = "India"
print(f"I'm {name}, {age} years old from {country}")

# 8. Your Turn!
# Create a sentence about yourself using f-strings
my_school = "DAV Public School"
my_grade = "10th"
print(f"I study in {my_school} in grade {my_grade}")