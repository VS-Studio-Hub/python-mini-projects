def weightInput():
    weight = input("Weight: ")
    return float(weight)


def weightConverter(weight):
    while True:
        weightIndicator = input("(L)bs or (K)g: ").upper()

        if weightIndicator == "L":
            kg = weight / 2.20462
            print(f"You are {kg:.2f} kilograms.")
            break

        elif weightIndicator == "K":
            lbs = weight * 2.20462
            print(f"You are {lbs:.2f} pounds.")
            break

        else:
            print("Invalid choice!")


def playConverter():
    while True:
        weight = weightInput()
        weightConverter(weight)

        userExit = input("Do you want to exit? (Y/N): ").upper()

        if userExit == "Y":
            print("Thank you for using the converter!")
            break

        elif userExit == "N":
            continue

        else:
            print("Invalid choice!")


playConverter()