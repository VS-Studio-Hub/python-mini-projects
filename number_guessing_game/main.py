import random

numberToGuess = random.randint(1, 100)

while True:
    try:
        guess = int(input("guess the numner betweeen 1 to 100: "))
        if guess == numberToGuess:
            print("Congratulations! you guessed the number.")
            break

        elif guess < numberToGuess:
            print("Too low!")

        elif guess > numberToGuess:
            print("Too high!")

        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number")
