import logo
import random

def game_intro():
    print(logo.logoArt)
    print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty.\n")
    difficulty = input("Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempts = 10
        print("You have 10 attempts remaining to guess the number.")
    elif difficulty == "hard":
        attempts = 5
        print("You have 5 attempts remaining to guess the number.")
    else:
        print("Invalid choice. Defaulting to easy mode.")
        attempts = 10
    return attempts

attempts = game_intro()

def game_logic(attempts):
    number_to_guess = random.randint(1,100)
    game_over = False
    
    while game_over == False and attempts != 0:
        user_guess = int(input("Make a guess:  "))
        if user_guess > number_to_guess:
            print("Too high. Guess again...")
            attempts -= 1
            print(f"You have {attempts} remaining to guess the number.")
            if attempts == 0:
                print("You lost! ")
                game_over = True
        elif user_guess < number_to_guess:
            print("Too low. Guess again...")
            attempts -= 1
            print(f"You have {attempts} remaining to guess the number.")
            if attempts == 0:
                print("You lost")
                game_over = False
        else:
            if user_guess == number_to_guess:
                print("You win!!!")
                game_over = True
        
game_logic(attempts)
        




