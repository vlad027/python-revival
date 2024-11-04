import random
import art
import game_data

print(art.logo)

def ask_user():
    user_choice = input("Who has more followers? Type 'a' or 'b':  ").lower()
    while user_choice not in ['a', 'b']:
        user_choice = input("Invalid input. Please type 'a' or 'b': ").lower()
    return user_choice

def match_making(option_to_exclude=None):
    option = random.choice(game_data.data)
    while option == option_to_exclude:
        option = random.choice(game_data.data)
    return option

def check_result(first, second, user_guess):
    if user_guess == "a" and first["follower_count"] > second["follower_count"]:
        return True
    elif user_guess == "b" and second["follower_count"] > first["follower_count"]:
        return True 
    else:
        return False
    
def display(option_a, option_b):
    print(f"Compare A: {option_a['name']}, {option_a['description']}, {option_a['country']}")
    print(art.vs)
    print(f"Compare B: {option_b['name']}, {option_b['description']}, {option_b['country']}")

def game_logic():
    score = 0
    option_a = match_making()
    keepGoing = True
    while keepGoing:
        option_b = match_making(option_to_exclude=option_a)
        display(option_a, option_b)
        user_guess = ask_user()
        result = check_result(option_a, option_b, user_guess)
        if result:
            score += 1
            print(f"You're right! Current score: {score}.")
            option_a = option_b
        else:
            print(f"Game over. Your final score is: {score}.")
            keepGoing = False

game_logic()
