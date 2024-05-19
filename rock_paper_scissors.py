import random
choices = ["rock", "paper", "scissors"]

def play_game():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice in choices:
        computer_choice = random.choice(choices)
        print(f"computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock":
            print("You win!" if computer_choice == "scissors" else "computer wins")
        elif user_choice == "paper":
            print("You win!" if computer_choice == "rock" else "computer wins")
        elif user_choice == "scissors":
            print("You win!" if computer_choice == "paper" else "computer wins")
    else:
        print("invalid choice!")

def main():
    try:
        num_games = int(input("How many times do you want to play the game? "))
        for _ in range(num_games):
            play_game()
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()