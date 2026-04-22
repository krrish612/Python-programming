# Advanced Weight Converter with Multiple Units, BMI, and Body Metrics

import math
from dataclasses import dataclass
from typing import Optional, Dict, List
from enum import Enum

# ================== UNIT DEFINITIONS ==================
class WeightUnit(Enum):
    KILOGRAM = "kg"
    GRAM = "g"
    POUND = "lb"
    OUNCE = "oz"
    STONE = "st"
    MILLIGRAM = "mg"
    TONNE = "t"
    NEWTON = "N"

# Conversion factors to kilograms
TO_KG = {
    WeightUnit.KILOGRAM: 1,
    WeightUnit.GRAM: 0.001,
    WeightUnit.POUND: 0.453592,
    WeightUnit.OUNCE: 0.0283495,
    WeightUnit.STONE: 6.35029,
    WeightUnit.MILLIGRAM: 0.000001,
    WeightUnit.TONNE: 1000,
    WeightUnit.NEWTON: 0.101972,  # Force to mass (9.8 m/s²)
}

# ================== CONVERTER ENGINE ==================
class WeightConverter:
    """Advanced weight converter"""
    
    def __init__(self):
        self.history: List[Dict] = []
    
    def convert(self, value: float, from_unit: WeightUnit, to_unit: WeightUnit) -> float:
        """Convert between weight units"""
        # Convert to kg first, then to target unit
        kg_value = value * TO_KG[from_unit]
        result = kg_value / TO_KG[to_unit]
        
        self.history.append({
            "value": value,
            "from": from_unit.value,
            "to": to_unit.value,
            "result": result
        })
        
        return result
    
    def convert_all(self, value: float, from_unit: WeightUnit) -> Dict[str, float]:
        """Convert to all units"""
        kg_value = value * TO_KG[from_unit]
        return {
            unit.value: kg_value / TO_KG[unit]
            for unit in WeightUnit
        }
    
    def get_history(self) -> List[Dict]:
        """Get conversion history"""
        return self.history

# ================== BODY METRICS ==================
@dataclass
class BodyMetrics:
    """Body measurements and calculations"""
    height_cm: float
    weight_kg: float
    age: int = 0
    gender: str = "neutral"  # "male", "female", "neutral"
    
    def bmi(self) -> float:
        """Calculate Body Mass Index"""
        height_m = self.height_cm / 100
        return self.weight_kg / (height_m ** 2)
    
    def bmi_category(self) -> str:
        """Get BMI category"""
        bmi = self.bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    
    def ideal_weight(self) -> tuple[float, float]:
        """Calculate ideal weight range (BMI 18.5-25)"""
        height_m = self.height_cm / 100
        min_kg = 18.5 * (height_m ** 2)
        max_kg = 25 * (height_m ** 2)
        return (min_kg, max_kg)
    
    def bmr(self) -> float:
        """Basal Metabolic Rate ( calories/day)"""
        # Mifflin-St Jeor Equation
        if self.gender == "male":
            return (10 * self.weight_kg) + (6.25 * self.height_cm) - (5 * self.age) + 5
        elif self.gender == "female":
            return (10 * self.weight_kg) + (6.25 * self.height_cm) - (5 * self.age) - 161
        else:
            # Gender neutral
            return (10 * self.weight_kg) + (6.25 * self.height_cm) - (5 * self.age) - 78
    
    def tdee(self, activity_level: float = 1.2) -> float:
        """Total Daily Energy Expenditure"""
        # Activity multipliers:
        # Sedentary: 1.2
        # Lightly active: 1.375
        # Moderately active: 1.55
        # Very active: 1.725
        # Extra active: 1.9
        return self.bmr() * activity_level
    
    def water_intake(self) -> float:
        """Recommended daily water intake (liters)"""
        # ~35ml per kg of body weight
        return self.weight_kg * 0.035
    
    def calorie_deficit(self, target_weight: float, weeks: int) -> float:
        """Calculate daily calorie deficit for target weight loss"""
        # 1 kg fat = 7700 calories
        kg_loss = self.weight_kg - target_weight
        total_calories = kg_loss * 7700
        daily_deficit = total_calories / (weeks * 7)
        return daily_deficit

# ================== FOOD CALORIE DATABASE ==================
class FoodDatabase:
    """Common food calories (per 100g)"""
    
    FOODS = {
        "apple": 52,
        "banana": 89,
        "rice": 130,
        "chicken breast": 165,
        "egg": 155,
        "milk": 42,
        "bread": 265,
        "rice": 130,
        "potato": 77,
        "onion": 40,
        "tomato": 18,
        "carrot": 41,
        "cheese": 402,
        "yogurt": 59,
        "beef": 250,
        "fish": 136,
    }
    
    @classmethod
    def get_calories(cls, food: str, grams: float = 100) -> Optional[float]:
        """Get calories for food amount"""
        food = food.lower()
        if food in cls.FOODS:
            return cls.FOODS[food] * (grams / 100)
        return None

# ================== EXERCISE CALORIES ==================
class ExerciseDatabase:
    """Calories burned per hour per kg (approximate)"""
    
    EXERCISES = {
        "walking": 0.8,
        "running": 10.0,
        "cycling": 8.0,
        "swimming": 10.0,
        "yoga": 2.5,
        "weightlifting": 5.0,
        "dancing": 7.0,
        "hiking": 7.0,
    }
    
    @classmethod
    def calories_burned(cls, exercise: str, weight_kg: float, minutes: int) -> Optional[float]:
        """Calculate calories burned"""
        exercise = exercise.lower()
        if exercise in cls.EXERCISES:
            cal_per_min = cls.EXERCISES[exercise] * (weight_kg / 60)  # Per minute per 60kg
            return cal_per_min * minutes
        return None

# ================== MAIN INTERFACE ==================
def main():
    converter = WeightConverter()
    
    print("=== ADVANCED WEIGHT CONVERTER ===")
    print("1. Simple conversion")
    print("2. Convert to all units")
    print("3. BMI Calculator")
    print("4. Body metrics")
    print("5. Food calories")
    print("6. Exercise calories")
    print("7. Exit")
    
    while True:
        choice = input("\nChoice: ")
        
        # SIMPLE CONVERSION
        if choice == "1":
            try:
                value = float(input("Weight: "))
                print("\nFrom: (1) kg (2) g (3) lb (4) oz (5) st")
                from_choice = int(input("Choice: "))
                print("To: (1) kg (2) g (3) lb (4) oz (5) st")
                to_choice = int(input("Choice: "))
                
                units = [
                    WeightUnit.KILOGRAM,
                    WeightUnit.GRAM,
                    WeightUnit.POUND,
                    WeightUnit.OUNCE,
                    WeightUnit.STONE
                ]
                from_unit = units[from_choice - 1]
                to_unit = units[to_choice - 1]
                
                result = converter.convert(value, from_unit, to_unit)
                print(f"\n{value} {from_unit.value} = {result:.4f} {to_unit.value}")
            
            except (ValueError, IndexError):
                print("Invalid input!")
        
        # CONVERT TO ALL
        elif choice == "2":
            try:
                value = float(input("Weight: "))
                print("\nFrom: (1) kg (2) g (3) lb (4) oz")
                from_choice = int(input("Choice: "))
                
                units = [
                    WeightUnit.KILOGRAM,
                    WeightUnit.GRAM,
                    WeightUnit.POUND,
                    WeightUnit.OUNCE
                ]
                from_unit = units[from_choice - 1]
                
                results = converter.convert_all(value, from_unit)
                print(f"\n{value} {from_unit.value} converted:")
                for unit, result in results.items():
                    if unit != "N":  # Skip Newton
                        print(f"  {unit}: {result:.4f}")
            
            except (ValueError, IndexError):
                print("Invalid input!")
        
        # BMI
        elif choice == "3":
            try:
                height = float(input("Height (cm): "))
                weight = float(input("Weight (kg): "))
                
                metrics = BodyMetrics(height, weight)
                
                print(f"\n=== BMI RESULTS ===")
                print(f"BMI: {metrics.bmi():.1f}")
                print(f"Category: {metrics.bmi_category()}")
                
                min_w, max_w = metrics.ideal_weight()
                print(f"Ideal range: {min_w:.1f} - {max_w:.1f} kg")
            
            except ValueError:
                print("Invalid input!")
        
        # BODY METRICS
        elif choice == "4":
            try:
                height = float(input("Height (cm): "))
                weight = float(input("Weight (kg): "))
                age = int(input("Age: "))
                gender = input("Gender (m/f): ").lower()
                
                metrics = BodyMetrics(height, weight, age, gender)
                
                print(f"\n=== BODY METRICS ===")
                print(f"BMI: {metrics.bmi():.1f} ({metrics.bmi_category()})")
                print(f"BMR: {metrics.bmr():.0f} calories/day")
                print(f"TDEE (sedentary): {metrics.tdee():.0f} cal/day")
                print(f"TDEE (active): {metrics.tdee(1.55):.0f} cal/day")
                print(f"Water: {metrics.water_intake():.1f} liters/day")
                
                print(f"\nTarget weight loss:")
                target = float(input("Target weight (kg): "))
                weeks = int(input("Weeks: "))
                deficit = metrics.calorie_deficit(target, weeks)
                print(f"Calorie deficit needed: {deficit:.0f} cal/day")
            
            except ValueError:
                print("Invalid input!")
        
        # FOOD CALORIES
        elif choice == "5":
            food = input("Food name: ")
            grams = float(input("Grams: "))
            calories = FoodDatabase.get_calories(food, grams)
            if calories:
                print(f"{grams}g of {food} = {calories:.0f} calories")
            else:
                print("Food not in database")
        
        # EXERCISE CALORIES
        elif choice == "6":
            exercise = input("Exercise: ")
            weight = float(input("Your weight (kg): "))
            minutes = int(input("Minutes: "))
            calories = ExerciseDatabase.calories_burned(exercise, weight, minutes)
            if calories:
                print(f"Calories burned: {calories:.0f}")
            else:
                print("Exercise not in database")
        
        elif choice == "7":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()