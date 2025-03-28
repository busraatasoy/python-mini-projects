# Load the random module
import random

# List of friends
friends = ["Eda", "Furkan", "Mustafa", "Kasım", "Defne"]

# Option 1: Using the choice() function
chosen_friend = random.choice(friends)
print(f"The chosen one to pay the bill is: {chosen_friend}")

# Option 2: Using randint() function
random_index = random.randint(0, 4)
print(f"The chosen one to pay the bill is: {friends[random_index]}")
