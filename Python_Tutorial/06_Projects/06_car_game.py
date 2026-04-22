# Advanced Car Game with Physics, Customization, and Multiple Game Modes

import time
import random
from enum import Enum
from dataclasses import dataclass
from typing import Optional, Dict, List
from collections import defaultdict

# ================== CAR ENUMS ==================
class CarState(Enum):
    OFF = "off"
    IDLE = "idle"
    RUNNING = "running"
    ACCELERATING = "accelerating"
    BRAKING = "braking"
    REVERSING = "reversing"

class Gear(Enum):
    P = "Park"
    R = "Reverse"
    N = "Neutral"
    D = "Drive"
    L = "Low"

# ================== CAR PARTS ==================
@dataclass
class CarSpecs:
    """Car specifications"""
    max_speed: float = 180.0
    acceleration: float = 5.0  # m/s²
    braking: float = 8.0  # m/s²
    weight: float = 1500  # kg
    horsepower: float = 150
    fuel_capacity: float = 50.0  # liters

@dataclass
class CarPart:
    """Car part with stats"""
    name: str
    level: int = 1
    max_level: int = 5
    
    def upgrade(self) -> bool:
        """Upgrade part"""
        if self.level < self.max_level:
            self.level += 1
            return True
        return False
    
    def get_bonus(self) -> float:
        """Get performance bonus"""
        return (self.level - 1) * 0.2  # 20% per level

# ================== CAR CLASS ==================
class Car:
    """Car with physics simulation"""
    
    def __init__(self, name: str = "My Car"):
        self.name = name
        self.state = CarState.OFF
        self.gear = Gear.P
        self.speed = 0.0  # km/h
        self.rpm = 0  # revolutions per minute
        self.fuel = 50.0
        self.odometer = 0
        self.specs = CarSpecs()
        
        # Parts
        self.parts = {
            "engine": CarPart("Engine"),
            "tires": CarPart("Tires"),
            "brakes": CarPart("Brakes"),
            "transmission": CarPart("Transmission"),
        }
        
        # Stats
        self.stats = {
            "races_won": 0,
            "races_lost": 0,
            "total_distance": 0,
            "fuel_used": 0,
        }
        
        # Achievements
        self.achievements: List[str] = []
    
    def start(self) -> str:
        """Start the car"""
        if self.state == CarState.OFF:
            self.state = CarState.IDLE
            self.rpm = 800  # Idle RPM
            return f"{self.name} started!"
        return "Car is already running!"
    
    def stop(self) -> str:
        """Stop the car"""
        if self.speed > 0:
            return "Stop the car first!"
        
        self.state = CarState.OFF
        self.rpm = 0
        return f"{self.name} stopped!"
    
    def shift(self, gear: Gear) -> str:
        """Shift gear"""
        if self.state == CarState.OFF:
            return "Start the car first!"
        
        if self.speed > 5 and gear != Gear.N:
            return "Stop or slow down to shift!"
        
        old_gear = self.gear
        self.gear = gear
        
        # Update RPM based on gear
        if gear == Gear.P:
            self.rpm = 0
        elif gear == Gear.R:
            self.rpm = 1500
        elif gear == Gear.N:
            self.rpm = 1000
        elif gear == Gear.D:
            self.rpm = 2000
        elif gear == Gear.L:
            self.rpm = 3000
        
        return f"Gear: {old_gear.value} → {gear.value}"
    
    def accelerate(self, seconds: float = 1.0) -> str:
        """Accelerate"""
        if self.state == CarState.OFF:
            return "Start the car first!"
        
        if self.gear == Gear.P or self.gear == Gear.N:
            return "Put in gear first!"
        
        # Calculate acceleration
        accel = self.specs.acceleration
        rpm_bonus = (self.rpm - 800) / 1000  # RPM affects acceleration
        
        # Apply upgrades
        engine_level = self.parts["engine"].level
        accel *= (1 + (engine_level - 1) * 0.2)
        
        # Calculate speed increase
        speed_increase = (accel + rpm_bonus) * seconds * 3.6  # Convert m/s to km/h
        
        old_speed = self.speed
        self.speed = min(self.speed + speed_increase, self.specs.max_speed)
        
        # Consume fuel
        fuel_usage = (self.speed / 100) * 0.1 * seconds
        self.fuel = max(0, self.fuel - fuel_usage)
        
        # Update state
        if self.speed > 0:
            self.state = CarState.RUNNING
        
        return f"Speed: {old_speed:.1f} → {self.speed:.1f} km/h"
    
    def brake(self, seconds: float = 1.0) -> str:
        """Apply brakes"""
        if self.speed == 0:
            return "Already stopped!"
        
        brake_force = self.specs.braking
        
        # Apply upgrades
        brake_level = self.parts["brakes"].level
        brake_force *= (1 + (brake_level - 1) * 0.15)
        
        speed_decrease = brake_force * seconds * 3.6
        old_speed = self.speed
        self.speed = max(0, self.speed - speed_decrease)
        
        if self.speed == 0:
            self.state = CarState.IDLE
        
        return f"Speed: {old_speed:.1f} → {self.speed:.1f} km/h"
    
    def reverse(self) -> str:
        """Shift to reverse"""
        if self.gear == Gear.R:
            return "Already in reverse!"
        
        if self.speed > 5:
            return "Stop to reverse!"
        
        return self.shift(Gear.R)
    
    def upgrade_part(self, part_name: str) -> str:
        """Upgrade a car part"""
        if part_name not in self.parts:
            return "Part not found!"
        
        part = self.parts[part_name]
        if part.upgrade():
            return f"{part.name} upgraded to level {part.level}!"
        return f"{part.name} already at max level!"
    
    def get_stats(self) -> str:
        """Get car stats"""
        return f"""
=== {self.name} ===
Speed: {self.speed:.1f} km/h
RPM: {self.rpm}
Gear: {self.gear.value}
Fuel: {self.fuel:.1f}L
Odometer: {self.odometer:.0f} km

Parts:
  Engine: {self.parts['engine'].level}/5
  Tires: {self.parts['tires'].level}/5
  Brakes: {self.parts['brakes'].level}/5
  Transmission: {self.parts['transmission'].level}/5

Stats:
  Races won: {self.stats['races_won']}
  Races lost: {self.stats['races_lost']}
  Total distance: {self.stats['total_distance']:.0f} km
"""
    
    def refuel(self) -> str:
        """Refuel the car"""
        self.fuel = self.specs.fuel_capacity
        return "Tank full!"
    
    def add_achievement(self, achievement: str) -> None:
        """Add achievement"""
        if achievement not in self.achievements:
            self.achievements.append(achievement)
            print(f"🏆 Achievement unlocked: {achievement}")

# ================== RACE TRACK ==================
@dataclass
class RaceResult:
    """Race result"""
    winner: str
    time: float
    opponent_time: float
    distance: float

class RaceTrack:
    """Race track"""
    
    def __init__(self):
        self.tracks = {
            "oval": {"name": "Oval Track", "length": 5, "difficulty": 1},
            "street": {"name": "Street Circuit", "length": 10, "difficulty": 2},
            "circuit": {"name": "Race Circuit", "length": 20, "difficulty": 3},
            "drag": {"name": "Drag Strip", "length": 0.4, "difficulty": 1},
        }
    
    def race(self, car1: Car, car2: Car, track_name: str) -> RaceResult:
        """Race two cars"""
        if track_name not in self.tracks:
            track_name = "oval"
        
        track = self.tracks[track_name]
        distance = track["length"]
        
        # Simulate race
        car1.speed = 0
        car2.speed = 0
        
        # Start race
        car1.state = CarState.RUNNING
        car2.state = CarState.RUNNING
        car1.shift(Gear.D)
        car2.shift(Gear.D)
        
        # Race loop
        car1_distance = 0
        car2_distance = 0
        race_time = 0
        
        while car1_distance < distance and car2_distance < distance:
            # Accelerate
            car1.accelerate(0.1)
            car2.accelerate(0.1)
            
            # Update distance
            car1_distance += car1.speed * 0.1 / 3600  # km
            car2_distance += car2.speed * 0.1 / 3600
            
            race_time += 0.1
        
        # Determine winner
        if car1_distance >= car2_distance:
            winner = car1.name
            car1.stats["races_won"] += 1
            car2.stats["races_lost"] += 1
            result = RaceResult(winner, race_time, race_time, distance)
        else:
            winner = car2.name
            car2.stats["races_won"] += 1
            car1.stats["races_lost"] += 1
            result = RaceResult(winner, race_time, race_time, distance)
        
        return result

# ================== DRIVING GAME ==================
class DrivingGame:
    """Main driving game"""
    
    def __init__(self):
        self.car = Car("My Car")
        self.track = RaceTrack()
        self.garage: List[Car] = []
        self.garage.append(self.car)
    
    def drive(self):
        """Driving simulation"""
        print("\n=== DRIVING SIM ===")
        print("Commands: start, stop, accel, brake, shift, stats, quit")
        
        while True:
            command = input("\n> ").lower()
            
            if command == "start":
                print(self.car.start())
            
            elif command == "stop":
                print(self.car.stop())
            
            elif command == "accel":
                duration = float(input("Seconds: ") or "1")
                print(self.car.accelerate(duration))
            
            elif command == "brake":
                duration = float(input("Seconds: ") or "1")
                print(self.car.brake(duration))
            
            elif command == "shift":
                print("Gear: P, R, N, D, L")
                gear = input("Gear: ").upper()
                try:
                    gear_enum = Gear[gear]
                    print(self.car.shift(gear_enum))
                except KeyError:
                    print("Invalid gear!")
            
            elif command == "stats":
                print(self.car.get_stats())
            
            elif command == "refuel":
                print(self.car.refuel())
            
            elif command == "quit":
                break
    
    def race(self):
        """Race against AI"""
        print("\n=== RACE MODE ===")
        print(f"Available tracks: {', '.join(self.track.tracks.keys())}")
        
        track_name = input("Track: ") or "oval"
        track = self.track.tracks.get(track_name)
        
        if not track:
            print("Invalid track!")
            return
        
        # Create opponent
        opponent = Car("Racer AI")
        opponent.specs.horsepower = random.randint(140, 200)
        
        print(f"\nRacing on {track['name']} ({track['length']} km)")
        print("Go!", "🏎️" * 10)
        
        result = self.track.race(self.car, opponent, track_name)
        
        print(f"\n🏆 Winner: {result.winner}")
        print(f"Time: {result.time:.2f}s")
    
    def customize(self):
        """Customize car"""
        while True:
            print("\n=== GARAGE ===")
            print(self.car.get_stats())
            
            print("\nUpgrade: engine, tires, brakes, transmission")
            print("Commands: back")
            
            choice = input("\nUpgrade: ")
            
            if choice == "back":
                break
            
            print(self.car.upgrade_part(choice))
    
    def achievements(self):
        """Check achievements"""
        print("\n=== ACHIEVEMENTS ===")
        
        # Check for new achievements
        if self.car.stats["races_won"] >= 10:
            self.car.add_achievement("Win 10 races")
        
        if self.car.stats["races_won"] >= 50:
            self.car.add_achievement("Win 50 races")
        
        if self.car.odometer >= 1000:
            self.car.add_achievement("Drive 1000 km")
        
        if any(p.level >= 3 for p in self.car.parts.values()):
            self.car.add_achievement("Upgrade a part to level 3")
        
        print("\nYour achievements:")
        for ach in self.car.achievements:
            print(f"  🏆 {ach}")
        
        if not self.car.achievements:
            print("No achievements yet!")

# ================== MAIN MENU ==================
def main():
    game = DrivingGame()
    
    while True:
        print("""
=== CAR GAME ===
1. Drive
2. Race
3. Garage
4. Achievements
5. Exit
""")
        
        choice = input("Choice: ")
        
        if choice == "1":
            game.drive()
        
        elif choice == "2":
            game.race()
        
        elif choice == "3":
            game.customize()
        
        elif choice == "4":
            game.achievements()
        
        elif choice == "5":
            print("Thanks for playing! 🏎️")
            break

if __name__ == "__main__":
    main()