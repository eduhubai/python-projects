import random
from ascii_art import win_art, lose_art, tie_art, rock, paper, scissors

# Initialize scores and gameplay variables
computer_score = 0
your_score = 0
number_of_ties = 0
keep_playing = True

# List of valid choices for the game
valid_choices = ["rock", "paper", "scissors"]

# Main game loop
while keep_playing:
    print("\n\n")  # Add some space before starting the round
    print("=" * 48)  # A clear divider line for visual separation
    print("NEW ROUND\n")

    while True:  # This inner loop ensures the user inputs a valid choice
        # Prompt user for input, automatically converting it to lowercase to simplify comparison
        your_choice = input(
            'Enter your choice (rock, paper, scissors): ').lower()
        print('You chose ' + your_choice)

        if your_choice == 'rock':
            print(rock)
        elif your_choice == 'paper':
            print(paper)
        elif your_choice == 'scissors':
            print(scissors)

        # Check if the choice is one of the valid options
        if your_choice in valid_choices:
            break  # Exit the loop if the choice is valid
        else:
            # Inform the user their choice was invalid and prompt again
            print("\nInvalid choice. Please enter rock, paper, or scissors.\n")

    # Generate computer's choice randomly from the valid options
    computer_choice = random.choice(valid_choices)
    print("\nThe computer chooses " + computer_choice)
    if computer_choice == 'rock':
        print(rock)
    elif computer_choice == 'paper':
        print(paper)
    elif computer_choice == 'scissors':
        print(scissors)

    # Compare player's and computer's choices to determine the outcome
    print("\n" + "-" * 48)  # Divider before showing the outcome
    if your_choice == computer_choice:
        number_of_ties += 1
        your_score += 0.5
        computer_score += 0.5
        print("It's a tie!!!")
    elif (your_choice == 'rock' and computer_choice == 'scissors') \
            or (your_choice == 'paper' and computer_choice == 'rock') \
            or (your_choice == 'scissors' and computer_choice == 'paper'):
        your_score += 1
        print('You won the round!')
    else:
        computer_score += 1
        print('Computer won the round!')

    # Display the current score after each round
    print("\nCurrent score--> You: " + str(your_score) +
          " - " + str(computer_score) + " Computer")
    print("=" * 48)  # A clear divider line after the round score

    # Ask the player if they want to play another round
    print("Do you want to play again? (yes/no)")
    answer = input().lower()
    if answer != "yes":
        keep_playing = False  # Exit the main loop if the player doesn't want to continue

# Final score and game outcome
print("\n" + "=" * 48)
print("Final score--> You: " + str(your_score) +
      " - " + str(computer_score) + " Computer\n")
if your_score > computer_score:
    print(win_art)
elif computer_score > your_score:
    print(lose_art)
else:
    print(tie_art)
