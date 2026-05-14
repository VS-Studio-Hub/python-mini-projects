import random
while True:
    choice = input("Roll the dice? (y/n);").lower()
    if choice == "y":
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        print(f'({x},{y})')
    elif choice == "n":
        print("Thank for playing!")
        break
    else:
        print("Invalid choice!")
