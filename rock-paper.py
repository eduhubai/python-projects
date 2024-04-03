import random

computer_score = 0
human_score = 0
number_of_ties = 0
keep_playing = True

valid_choices = ["rock", "paper", "scissors"]

while keep_playing:
    while True:  # This loop ensures that the user inputs a valid choice
        human_choice = input('Enter human choice (rock, paper, scissors): ').lower()  # Automatically converts input to lowercase
        print('Human chooses ' + human_choice)
        if human_choice in valid_choices:
            break  # Exit the loop if valid choice is entered
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

    computer_choice = random.choice(valid_choices)  # Generate computer's choice
    print('The computer chooses ' + computer_choice)

    if human_choice == computer_choice:
        number_of_ties += 1
        print('Tie')
    elif (human_choice == 'rock' and computer_choice == 'scissors') or (human_choice == 'paper' and computer_choice == 'rock') or (human_choice == 'scissors' and computer_choice == 'paper'):
        human_score += 1
        print('Human wins')
    else:
        computer_score += 1
        print('Computer wins')

    print("Do you want to play again? (yes/no)")
    answer = input().lower()
    if answer != "yes":
        keep_playing = False

print("Thanks for playing!")
print('Computer score: ' + str(computer_score))
print('Human score: ' + str(human_score))
print('Ties: ' + str(number_of_ties))
