import art
import random
import game_data

is_game_over = False
score = 0
print(art.logo)

while not is_game_over:

    guess1 = random.choice(game_data.data)
    print(f"Compare A: {list(guess1.values())[0]}, a {list(guess1.values())[2]}, from {list(guess1.values())[3]}")
    print(art.vs)
    guess2 = random.choice(game_data.data)
    if guess1 == guess2:
        guess2 = random.choice(game_data.data)
    print(f"Against B: {list(guess2.values())[0]}, a {list(guess2.values())[2]}, from {list(guess2.values())[3]}")
    a_or_b = input("Who has more followers? Type 'A' or 'B': ").title()
    print("\n"*20)
    a = list(guess1.values())[1]
    b = list(guess2.values())[1]
    if (a > b) and (a_or_b == "A"):
        score += 1
        print(art.logo)
        print(f"You're right! Current score: {score}")
    elif (a < b) and (a_or_b == "B"):
        score += 1
        print(art.logo)
        print(f"You're right! Current score: {score}")
    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        is_game_over = True