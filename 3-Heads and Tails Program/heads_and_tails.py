#Load the random module
import random

# Generate a random choice
random_heads_or_tails = random.randint(0, 1)

# Print the result based on the random value
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
