import random

score = 0

def game():
    global score
    options = ["rock", "paper", "scissors"]
    print(f"Lets start the game, following are the options: \n {options}")
    user = input("what do you pick\n").strip().lower()
    computer = random.choice(options)

    #    WHEN USER INPUT IS ROCK
    if user == 'rock' and computer == 'rock':
        print("\n")
        print(f"{user} and {computer} = Draw")
        print(f" current score: {score}")
        
    elif user == 'rock' and computer == 'scissors':
        print(f"{user} and {computer} = Win")
        score = 1+ score
        print(f"1 point earned, current score is {score}")

    elif user == 'rock' and computer == 'paper':
        print(f"{user} and {computer} = Lose")
        print(f" current score: {score}")
   
   #    WHEN USER INPUT IS PAPER
    elif user == 'paper' and computer == 'paper':
        print(f"{user} and {computer} = Draw")
        print(f" current score: {score}")

    elif user == 'paper' and computer == 'rock':
        print(f"{user} and {computer} = Win")
        score = 1+ score
        print(f"1 point earned, current score is {score}")

    elif user == 'paper' and computer== 'scissors':
        print(f"{user} and {computer} = Lose")
        print(f" current score: {score}")
    
    #    WHEN USER INPUT IS PAPER
    elif user == 'scissors' and computer == 'scissors':
        print(f"{user} and {computer} = Draw")
        print(f" current score: {score}")

    elif user == 'scissors' and computer == 'paper':
        print(f"{user} and {computer} = Win")
        score = 1+ score
        print(f"1 point earned, current score is {score}")

    elif user == 'scissors' and computer== 'rock':
        print(f"{user} and {computer} = Lose")
        print(f" current score: {score}")
    
    again = input("Do you want to continue (yes/no):\n").strip().lower()
    if again =="yes":
        game()
    else:
        print(f"This is your total score: {score}, See you again")


game()