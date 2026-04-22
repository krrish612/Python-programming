# Number Guessing Game
import random

print("=== NUMBER GUESSING GAME ===")
print("I'm thinking of a number between 1 and 100")
print("Try to guess it!")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("\nYour guess: "))
    attempts += 1
    
    if guess == number:
        print(f"🎉 Correct! You got it in {attempts} attempts!")
        break
    elif guess < number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")