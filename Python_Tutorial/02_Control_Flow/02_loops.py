# Loop Practice

# Example 1: Print 1 to 10
print("1 to 10:")
for i in range(1, 11):
    print(i)

# Example 2: Print multiplication table
print("\n--- 5 Times Table ---")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Example 3: While loop
print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Go!")

# Example 4: Sum of numbers
total = 0
for i in range(1, 101):
    total += i
print("\nSum of 1 to 100:", total)

# Example 5: Find factorial
num = int(input("\nEnter number for factorial: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"{num}! = {fact}")

# Example 6: Your turn - Even numbers
print("\nEven numbers between 1 and 20:")
for i in range(2, 21, 2):
    print(i, end=" ")
print()