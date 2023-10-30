# IMPORTS

# First, let us import the two files, art & data!
import art 
import game_data
# We should also import random module because we want 
# to randomly compare every time
import random

# ------------------------------------------------------------------
# START GAME

# Let's print the main logo for the game 
print(art.logo)

# Randomly pick someone for choice a
choice_a = random.choice(game_data.data)

# Randomly pick someone for choice b
choice_b = random.choice(game_data.data)

# ---------------------------------------------------------------------------------------------
# Functionalities 

# We can use a boolean to make the user keep going until they lose
user_correct = True 

# Use a var to keep track of user score
score = 0

while user_correct:
    # print out the first person 
    print(f"A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")

    # print out the VS logo in between
    print(art.vs)

    # print out second person
    print(f"B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")

    # Ask user who has more followers
    decision = input("Who has more followers? Type 'A' or 'B': ")
    if decision == 'A':
        if choice_a['follower_count'] > choice_b['follower_count']:
            score += 1
            print(f"You're correct! Current score: {score}")
            choice_b = random.choice(game_data.data)
        else:
            print(f"Sorry, that's wrong! Final Score: {score}")
            user_correct = False
    else:
        if choice_a['follower_count'] < choice_b['follower_count']:
            score += 1
            print(f"You're correct! Current score: {score}")
            choice_a = random.choice(game_data.data)
        else:
            print(f"Sorry, that's wrong! Final Score: {score}")
            user_correct = False





