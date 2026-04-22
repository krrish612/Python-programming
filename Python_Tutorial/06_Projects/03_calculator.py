# Advanced Calculator with History, Functions, Variables, and Unit Conversions

import math
import cmath
import random
from typing import Callable, Dict, Optional, Union
from collections import defaultdict
from functools import lru_cache

# ================== CALCULATOR ENGINE ==================
class Calculator:
    """Advanced calculator engine"""
    
    def __init__(self):
        self.history: list[dict] = []
        self.variables: Dict[str, float] = {}
        self.functions: Dict[str, Callable] = {}
        self.last_result: Optional[float] = None
        
        # Register built-in functions
        self._register_functions()
    
    def _register_functions(self) -> None:
        """Register built-in functions"""
        self.functions = {
            # Math functions
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "asin": math.asin,
            "acos": math.acos,
            "atan": math.atan,
            "sqrt": math.sqrt,
            "log": math.log,
            "log10": math.log10,
            "log2": math.log2,
            "exp": math.exp,
            "abs": abs,
            "floor": math.floor,
            "ceil": math.ceil,
            "round": round,
            "fact": math.factorial,
            "gcd": math.gcd,
            "pow": pow,
            "max": max,
            "min": min,
            
            # Random functions
            "rand": random.random,
            "randint": random.randint,
        }
    
    def set_variable(self, name: str, value: float) -> None:
        """Store variable"""
        self.variables[name] = value
    
    def get_variable(self, name: str) -> Optional[float]:
        """Get variable"""
        return self.variables.get(name)
    
    def evaluate(self, expression: str) -> Optional[float]:
        """Evaluate mathematical expression"""
        expression = expression.strip().lower()
        
        try:
            # Check for variable assignment
            if "=" in expression and "!" not in expression:
                parts = expression.split("=", 1)
                if len(parts) == 2:
                    var_name = parts[0].strip()
                    value = self._evaluate(parts[1])
                    if value is not None:
                        self.set_variable(var_name, value)
                        return value
            
            # Check for variable recall (e.g., x = 5, then ans = x * 2)
            # Replace variables in expression
            for var_name, value in self.variables.items():
                expression = expression.replace(var_name, str(value))
            
            # Replace "ans" with last result
            if "ans" in expression:
                expression = expression.replace("ans", str(self.last_result or 0))
            
            result = self._evaluate(expression)
            
            if result is not None:
                self.last_result = result
                self.history.append({
                    "expression": expression,
                    "result": result
                })
            
            return result
        
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def _evaluate(self, expression: str) -> Optional[float]:
        """Internal evaluation"""
        # Handle built-in functions (e.g., sqrt(16))
        for func_name, func in self.functions.items():
            if expression.startswith(func_name + "("):
                args_str = expression[len(func_name)+1:-1]
                args = [float(x.strip()) for x in args_str.split(",")]
                return float(func(*args))
        
        # Handle power (e.g., 2^10)
        if "^" in expression:
            expression = expression.replace("^", "**")
        
        # Handle implicit multiplication (e.g., 5(3) or (2)(3))
        import re
        expression = re.sub(r'(\d)\(', r'\1*(', expression)
        expression = re.sub(r'\)(\d)', r')*\1', expression)
        expression = re.sub(r'\)(\()', r')*(', expression)
        
        # Use eval safely
        result = eval(expression, {"__builtins__": {}, "math": math, "cmath": cmath}, {})
        
        if isinstance(result, complex):
            return result.real
        
        return float(result)
    
    def get_history(self, limit: int = 10) -> list[dict]:
        """Get calculation history"""
        return self.history[-limit:]
    
    def clear_history(self) -> None:
        """Clear history"""
        self.history = []
    
    def get_vars(self) -> Dict[str, float]:
        """Get all variables"""
        return self.variables.copy()

# ================== UNIT CONVERTERS ==================
class UnitConverter:
    """Unit conversion functions"""
    
    # Length
    @staticmethod
    def km_to_miles(km: float) -> float:
        return km * 0.621371
    
    @staticmethod
    def miles_to_km(miles: float) -> float:
        return miles / 0.621371
    
    @staticmethod
    def m_to_feet(m: float) -> float:
        return m * 3.28084
    
    @staticmethod
    def feet_to_m(feet: float) -> float:
        return feet / 3.28084
    
    # Weight
    @staticmethod
    def kg_to_lbs(kg: float) -> float:
        return kg * 2.20462
    
    @staticmethod
    def lbs_to_kg(lbs: float) -> float:
        return lbs / 2.20462
    
    # Temperature
    @staticmethod
    def c_to_f(c: float) -> float:
        return (c * 9/5) + 32
    
    @staticmethod
    def f_to_c(f: float) -> float:
        return (f - 32) * 5/9
    
    @staticmethod
    def c_to_k(c: float) -> float:
        return c + 273.15
    
    @staticmethod
    def k_to_c(k: float) -> float:
        return k - 273.15
    
    # Volume
    @staticmethod
    def liters_to_gallons(liters: float) -> float:
        return liters * 0.264172
    
    @staticmethod
    def gallons_to_liters(gallons: float) -> float:
        return gallons / 0.264172
    
    # Data
    @staticmethod
    def bytes_to_kb(bytes: float) -> float:
        return bytes / 1024
    
    @staticmethod
    def kb_to_mb(kb: float) -> float:
        return kb / 1024
    
    @staticmethod
    def gb_to_bytes(gb: float) -> float:
        return gb * 1024 * 1024 * 1024

# ================== CONVERSION MENU ==================
def conversion_menu():
    """Unit conversion menu"""
    converter = UnitConverter()
    
    while True:
        print("\n=== CONVERSIONS ===")
        print("1. Length (km/miles, m/feet)")
        print("2. Weight (kg/lbs)")
        print("3. Temperature (°C/°F/K)")
        print("4. Volume (liters/gallons)")
        print("5. Data (GB/MB/KB)")
        print("6. Back to main")
        
        choice = input("\nChoice: ")
        
        try:
            if choice == "1":
                val = float(input("Value: "))
                print(f"{val} km = {converter.km_to_miles(val):.4f} miles")
                print(f"{val} m = {converter.m_to_feet(val):.4f} feet")
            
            elif choice == "2":
                val = float(input("Value: "))
                print(f"{val} kg = {converter.kg_to_lbs(val):.4f} lbs")
                print(f"{val} lbs = {converter.lbs_to_kg(val):.4f} kg")
            
            elif choice == "3":
                val = float(input("Value: "))
                print(f"{val}°C = {converter.c_to_f(val):.4f}°F")
                print(f"{val}°C = {converter.c_to_k(val):.4f}K")
                print(f"{val}°F = {converter.f_to_c(val):.4f}°C")
            
            elif choice == "4":
                val = float(input("Value: "))
                print(f"{val} liters = {converter.liters_to_gallons(val):.4f} gallons")
                print(f"{val} gallons = {converter.gallons_to_liters(val):.4f} liters")
            
            elif choice == "5":
                val = float(input("Value (GB): "))
                kb = val * 1024 * 1024
                print(f"{val} GB = {kb:.0f} KB")
                print(f"{val} GB = {val * 1024:.0f} MB")
            
            elif choice == "6":
                break
        
        except ValueError:
            print("Enter a number!")

# ================== BASE CONVERTER ==================
class BaseConverter:
    """Convert between number bases"""
    
    @staticmethod
    def to_binary(n: int) -> str:
        return bin(n)[2:]
    
    @staticmethod
    def to_octal(n: int) -> str:
        return oct(n)[2:]
    
    @staticmethod
    def to_hex(n: int) -> str:
        return hex(n)[2:]
    
    @staticmethod
    def from_binary(s: str) -> int:
        return int(s, 2)
    
    @staticmethod
    def from_octal(s: str) -> int:
        return int(s, 8)
    
    @staticmethod
    def from_hex(s: str) -> int:
        return int(s, 16)

# ================== MAIN CALCULATOR ==================
def main():
    calc = Calculator()
    converter = UnitConverter()
    base = BaseConverter()
    
    print("=== ADVANCED CALCULATOR ===")
    print("Type 'help' for commands, 'quit' to exit")
    
    while True:
        expression = input("\n> ").strip()
        
        if not expression:
            continue
        
        if expression.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        
        elif expression.lower() == "help":
            print("""
=== HELP ===
Basic: +, -, *, /
Power: ^ or **
Mod: %

Functions: sqrt(x), sin(x), cos(x), 
         log(x), exp(x), fact(x)

Conversions: convert - unit converter
Base: base - number base converter

Variables: store x = 5
Recall: ans - last result

History: history - show last calculations
Vars: vars - show stored variables
Clear: clear - clear history
""")
        
        elif expression.lower() == "convert":
            conversion_menu()
        
        elif expression.lower() == "base":
            print("\n=== BASE CONVERTER ===")
            n = int(input("Enter decimal: "))
            print(f"Binary: {base.to_binary(n)}")
            print(f"Octal: {base.to_octal(n)}")
            print(f"Hex: {base.to_hex(n)}")
            print("Binary to decimal:", base.from_binary(str(n)))
        
        elif expression.lower() == "history":
            print("\n=== HISTORY ===")
            for item in calc.get_history():
                print(f"{item['expression']} = {item['result']}")
        
        elif expression.lower() == "vars":
            print("\n=== VARIABLES ===")
            for name, value in calc.get_vars().items():
                print(f"{name} = {value}")
        
        elif expression.lower() == "clear":
            calc.clear_history()
            print("History cleared!")
        
        else:
            result = calc.evaluate(expression)
            if result is not None:
                # Round very small/large numbers
                if abs(result) > 1e10 or (abs(result) < 1e-6 and result != 0):
                    print(f"{result:.4e}")
                elif result == int(result):
                    print(int(result))
                else:
                    print(f"{result:.6f}")

if __name__ == "__main__":
    main()