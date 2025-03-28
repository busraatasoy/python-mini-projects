print(" 🍕 Welcome to Python Pizza Deliveries! 🍕")

size = input("What size pizza do you want? S, M or L: \n").upper()
pepperoni = input("Do you want pepperoni on your pizza 🌶 ? Y or N: \n").upper()
extra_cheese = input("Do you want extra cheese 🧀? Y or N: \n").upper()


# Check for invalid inputs
if size not in ["S", "M", "L"]:
    print("You have chosen an invalid size. 🔴 Please enter S, M, or L.")
    exit()
if pepperoni not in ["Y", "N"] or extra_cheese not in ["Y", "N"]:
    print("You have chosen an invalid choice! 🔴 Please enter Y or N.")
    exit()


# Work out how much they need to pay based on their size choice.
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

# Work out how much to add to their bill based on their pepperoni choice.

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: 💲{bill}.")
