# Weight Converter Program

print("=== WEIGHT CONVERTER ===")
print("1. KG to Pounds")
print("2. Pounds to KG")

choice = input("Choose (1-2): ")

if choice == "1":
    kg = float(input("Enter weight in KG: "))
    pounds = kg * 2.20462
    print(f"{kg} KG = {pounds:.2f} Pounds")
elif choice == "2":
    pounds = float(input("Enter weight in Pounds: "))
    kg = pounds / 2.20462
    print(f"{pounds} Pounds = {kg:.2f} KG")
else:
    print("Invalid choice!")