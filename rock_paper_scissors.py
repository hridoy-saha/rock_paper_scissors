import random
choices = ["rock","paper","scissors"]
user_choice = input("Enter your choice (rock,paper,scissors:")
if user_choice in choices:
    computer_choice = random.choice(choices)
    print(f"computer chose:{computer_choice}")
    if user_choice == computer_choice:
         print("it's a tie!")
    elif user_choice == "rock":
         print("you win!" if computer_choice == "scissors" else "computer wins")
    elif user_choice == "paper":
         print("you win!" if computer_choice == "rock" else "computer wins")
    else:
         print("you win!" if computer_choice == "paper" else "computer wins")
else:
     print("invalid choice!")              

