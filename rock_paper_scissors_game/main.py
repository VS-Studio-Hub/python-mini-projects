import random

emojis = {"r": "🪨", "p": "📄", "s": "✂️"}
choices = ("r", "p", "s")
nextGameChoice = ("y", "n")


def getUserChoice():
    while True:
        playerChoice = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if playerChoice in choices:
            return playerChoice
        else:
            print("Invalid choice!")
            continue


def displayChoices(playerChoice, computerChoice):
    print(f"you chose {emojis[playerChoice]}")
    print(f"Computer chose {emojis[computerChoice]}")


def determineWinner(playerChoice, computerChoice):
    if playerChoice == computerChoice:
        print("Draw!")
    elif playerChoice == "r" and computerChoice == "p":
        print("you lose!")
    elif playerChoice == "r" and computerChoice == "s":
        print("you win!")
    elif playerChoice == "p" and computerChoice == "r":
        print("you win!")
    elif playerChoice == "p" and computerChoice == "s":
        print("you lose!")
    elif playerChoice == "s" and computerChoice == "r":
        print("you lose!")
    elif playerChoice == "s" and computerChoice == "p":
        print("you win!")


def playGame():
    while True:
        playerChoice = getUserChoice()

        computerChoice = random.choice(choices)

        displayChoices(playerChoice, computerChoice)
        determineWinner(playerChoice, computerChoice)

        nextGame = input("continue? (y/n) ").lower()
        if nextGame not in nextGameChoice:
            print("Invalid choice!")
            continue

        if nextGame == "n":
            print("Thanks for playing!")
            break


playGame()
