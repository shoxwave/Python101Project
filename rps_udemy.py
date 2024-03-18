import random

moves = ["rock", "paper", "scissors"]

def another_round():
    response = input("Would you like to play again?").lower()
    if "yes" in response:
        play_game()
    elif "no" in response:
        print("Goodbye!")
        exit()
    else:
        print("Sorry, I don't understand.")
    return response

def round(user_move, computer_move):
    user = user_move
    computer = computer_move
    if user == computer:
        print("It is a tie!")
    elif user == 'rock' and computer == 'scissors':
        print(f"{name} wins!")
    elif user == 'scissors' and computer == 'paper':
        print(f"{name} wins!")
    elif user == 'paper' and computer == 'rock':
        print(f"{name} wins!")
    else:
        print("Computer wins!")

def play_game():
    computer_move = random.choice(moves)
    user_move = input("Choose rock, paper, or scissors. To exit type quit. ")
    round(user_move, computer_move)
    another_round()

name = input("What is your name?")
play_game()