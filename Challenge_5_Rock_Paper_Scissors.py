import random
computer_score = 0
human_score = 0
number_of_ties = 0
keep_playing = True

valid_choices = ["rock", "paper", "scissors"]
while True:
    human_choice = input('enter human choice (rock, paper, scissors): ')
    print('human chooses ' + human_choice)
    if human_choice.lower() in valid_choices:  # Check for lowercase too
        break  # Exit the loop if valid choice is entered
    else:
        print("Invalid choice. Please enter rock, paper, or scissors.")

    computer_choice = random.choice(
        ['rock', 'paper', 'scissors'])  # change this line
    print('the computer chooses ' + computer_choice)

    if (human_choice == computer_choice):
        number_of_ties += 1
        print('tie')
    elif ((human_choice == 'rock' and computer_choice == 'paper') or (human_choice == 'paper' and computer_choice == 'scissors') or (human_choice == 'scissors' and computer_choice == 'rock')):
        computer_score += 1
        print('computer wins')
    else:
        human_score += 1
        print('human wins')
    print("Do you want to play again?")

    answer = input()
    if answer == "no":
        keep_playing = False
    print("Thanks for playing!")
print('computer score: ' + str(computer_score))
print('human score: ' + str(human_score))
print('ties: ' + str(number_of_ties))
