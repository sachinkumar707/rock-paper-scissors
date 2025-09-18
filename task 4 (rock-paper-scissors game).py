import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    print("===== Rock-Paper-Scissors Game =====")

    while True:
        print("\nChoices: rock | paper | scissors")
        user_choice = input("Enter your choice: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("💻 Computer wins this round!")
            computer_score += 1

        # Show current score
        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        # Ask to play again
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != "y":
            print("\n===== Final Score =====")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("🏆 Congratulations! You won the game!")
            elif user_score < computer_score:
                print("💻 Computer wins the game! Better luck next time.")
            else:
                print("🤝 It's a draw overall!")
            break


# Run Game
play_game()
