# Car Game
start = False
engine_on = False

print("=== CAR GAME ===")
print("Commands: start, stop, quit")

while True:
    command = input("\n> ").lower()
    
    if command == "start":
        if engine_on:
            print("Car is already started!")
        else:
            engine_on = True
            print("Engine started.")
    elif command == "stop":
        if not engine_on:
            print("Car is already stopped!")
        else:
            engine_on = False
            print("Engine stopped.")
    elif command == "quit":
        print("Goodbye!")
        break
    else:
        print("Unknown command. Try: start, stop, quit")