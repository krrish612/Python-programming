# Advanced Number Guessing Game with Levels, Hints, and Scoring

import random
import math
from enum import Enum
from dataclasses import dataclass
from typing import Optional, List
import time

# ================== DIFFICULTY LEVELS ==================
class Difficulty(Enum):
    EASY = (1, 50, 10)       # Range 1-50, 10 attempts
    MEDIUM = (1, 100, 7)     # Range 1-100, 7 attempts
    HARD = (1, 500, 5)       # Range 1-500, 5 attempts
    EXPERT = (1, 1000, 5)    # Range 1-1000, 5 attempts
    
    def __init__(self, min_val: int, max_val: int, attempts: int):
        self.min_val = min_val
        self.max_val = max_val
        self.attempts = attempts

# ================== GAME STATS ==================
@dataclass
class GameStats:
    """Track game statistics"""
    games_played: int = 0
    games_won: int = 0
    best_attempts: int = float('inf')
    total_attempts: int = 0
    
    def win_rate(self) -> float:
        if self.games_played == 0:
            return 0.0
        return (self.games_won / self.games_played) * 100

# ================== HINT SYSTEM ==================
class HintSystem:
    """Provide hints to the player"""
    
    @staticmethod
    def get_hint(guess: int, target: int, attempts_left: int) -> str:
        """Generate hint based on current state"""
        difference = abs(target - guess)
        
        if attempts_left <= 2:
            # Critical hints
            if guess < target:
                return "You're VERY close! Go higher!"
            else:
                return "You're VERY close! Go lower!"
        
        if difference > target // 4:
            if guess < target:
                return "Cold! Try a much higher number"
            else:
                return "Cold! Try a much lower number"
        else:
            if guess < target:
                return "Warm! Try a bit higher"
            else:
                return "Warm! Try a bit lower"
    
    @staticmethod
    def get_range_hint(target: int, min_val: int, max_val: int) -> str:
        """Hint about the range"""
        midpoint = (min_val + max_val) // 2
        if target < midpoint:
            return f"It's between {min_val} and {midpoint}"
        else:
            return f"It's between {midpoint} and {max_val}"
    
    @staticmethod
    def get_prime_hint(target: int) -> Optional[str]:
        """Hint if target is prime"""
        if target > 1:
            is_prime = all(target % i for i in range(2, int(math.sqrt(target)) + 1)
            if is_prime:
                return "The number is PRIME!"

# ================== MAIN GAME ==================
class NumberGame:
    """Advanced number guessing game"""
    
    def __init__(self):
        self.stats = GameStats()
        self.difficulty = Difficulty.MEDIUM
        self.target = 0
        self.attempts_left = 0
        self.guesses: List[int] = []
        self.game_history: List[dict] = []
    
    def set_difficulty(self, level: str) -> bool:
        """Set difficulty level"""
        try:
            self.difficulty = Difficulty[level.upper()]
            return True
        except KeyError:
            return False
    
    def start_new_game(self) -> None:
        """Start a new game"""
        self.target = random.randint(
            self.difficulty.min_val,
            self.difficulty.max_val
        )
        self.attempts_left = self.difficulty.attempts
        self.guesses = []
    
    def make_guess(self, guess: int) -> tuple[bool, str]:
        """Process a guess"""
        if guess < self.difficulty.min_val or guess > self.difficulty.max_val:
            return False, f"Guess must be between {self.difficulty.min_val} and {self.difficulty.max_val}"
        
        self.guesses.append(guess)
        self.attempts_left -= 1
        
        if guess == self.target:
            return True, f"🎉 Correct! You got it in {len(self.guesses)} attempts!"
        elif self.attempts_left == 0:
            return False, f"Game over! The number was {self.target}"
        else:
            hint = HintSystem.get_hint(guess, self.target, self.attempts_left)
            return False, hint
    
    def get_stats_display(self) -> str:
        """Get stats display"""
        return (
            f"\n=== STATISTICS ===\n"
            f"Games Played: {self.stats.games_played}\n"
            f"Win Rate: {self.stats.win_rate():.1f}%\n"
            f"Best Score: {self.stats.best_attempts} attempts\n"
            f"Average: {self.stats.total_attempts / max(1, self.stats.games_played):.1f}"
        )
    
    def save_game(self) -> dict:
        """Save current game state"""
        return {
            "difficulty": self.difficulty.name,
            "target": self.target,
            "attempts": self.difficulty.attempts,
            "guesses": self.guesses
        }
    
    def load_game(self, saved: dict) -> bool:
        """Load saved game"""
        try:
            self.difficulty = Difficulty[saved["difficulty"]]
            self.target = saved["target"]
            self.attempts_left = saved["attempts"]
            self.guesses = saved["guesses"]
            return True
        except (KeyError, ValueError):
            return False

# ================== AI PLAYER ==================
class AIPlayer:
    """AI that plays the guessing game optimally"""
    
    def __init__(self, difficulty: Difficulty):
        self.difficulty = difficulty
        self.low = difficulty.min_val
        self.high = difficulty.max_val
        self.attempts = 0
    
    def make_guess(self, target: int) -> int:
        """Binary search - optimal strategy"""
        self.attempts += 1
        
        # Binary search
        guess = (self.low + self.high) // 2
        
        if guess < target:
            self.low = guess + 1
        elif guess > target:
            self.high = guess - 1
        
        return guess
    
    def reset(self) -> None:
        """Reset for new game"""
        self.low = self.difficulty.min_val
        self.high = self.difficulty.max_val
        self.attempts = 0

# ================== TOURNAMENT ==================
def play_tournament() -> None:
    """Play a tournament against AI"""
    game = NumberGame()
    ai = AIPlayer(Difficulty.MEDIUM)
    
    print("=== TOURNAMENT: YOU vs AI ===")
    print("Best of 7 rounds wins!\n")
    
    human_wins = 0
    ai_wins = 0
    
    for round_num in range(1, 8):
        print(f"=== Round {round_num}/7 ===")
        target = random.randint(1, 100)
        
        # AI plays first
        ai_guess = ai.make_guess(target)
        ai_attempts = ai.attempts
        
        # Human plays
        game.start_new_game()
        
        print(f"AI guessed in {ai_attempts} attempts")
        print(f"Your turn! Target: 1-100")
        
        human_won = False
        for attempt in range(1, 8):
            try:
                guess = int(input(f"Attempt {attempt}: "))
                if guess == target:
                    print(f"🎉 Won in {attempt} attempts!")
                    human_won = True
                    break
                elif guess < target:
                    print("Higher!")
                else:
                    print("Lower!")
            except ValueError:
                print("Invalid input!")
        
        if human_won and ai_attempts < attempt:
            human_wins += 1
            print("You win this round!")
        elif ai_attempts <= attempt:
            ai_wins += 1
            print(f"AI wins! It was {target}")
        else:
            human_wins += 1
            print("You win this round!")
        
        ai.reset()
    
    print(f"\n=== FINAL SCORE ===")
    print(f"You: {human_wins}")
    print(f"AI: {ai_wins}")

# ================== DEMO ==================
if __name__ == "__main__":
    game = NumberGame()
    
    # Select difficulty
    print("=== NUMBER GUESSING GAME ===")
    print("Select difficulty: EASY, MEDIUM, HARD, EXPERT")
    
    level = input("Choice: ").strip().upper() or "MEDIUM"
    if not game.set_difficulty(level):
        print("Invalid, using MEDIUM")
        game.set_difficulty("MEDIUM")
    
    print(f"\nRange: {game.difficulty.min_val}-{game.difficulty.max_val}")
    print(f"Attempts: {game.difficulty.attempts}")
    
    # Play game
    game.start_new_game()
    
    while True:
        try:
            guess = int(input(f"\nYour guess ({game.attempts_left} left): "))
            
            correct, message = game.make_guess(guess)
            print(message)
            
            if correct:
                game.stats.games_won += 1
                game.stats.games_played += 1
                game.stats.total_attempts += len(game.guesses)
                game.stats.best_attempts = min(
                    game.stats.best_attempts,
                    len(game.guesses)
                )
                
                print(game.get_stats_display())
                
                play_again = input("\nPlay again? (y/n): ").lower()
                if play_again != 'y':
                    break
                
                game.start_new_game()
            
            elif "Game over" in message:
                game.stats.games_played += 1
                print(game.get_stats_display())
                
                play_again = input("\nPlay again? (y/n): ").lower()
                if play_again != 'y':
                    break
                
                game.start_new_game()
        
        except ValueError:
            print("Enter a number!")
    
    print("Thanks for playing!")