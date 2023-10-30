# First, let us import the two files, art & data!
import art 
import game_data
# We should also import random module because we want 
# to randomly compare every time
import random

# Let's print the main logo for the game 
print(art.logo)

# Randomly pick someone for choice a
choice_a = random.choice(game_data.data)

# Randomly pick someone for choice b
choice_b = random.choice(game_data.data)

# print out the first person 
print(f"A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")

# print out the VS logo in between
print(art.vs)

# print out second person
print(f"B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")

# Ask user who has more followers
decision = input("Who has more followers? Type 'A' or 'B': ")