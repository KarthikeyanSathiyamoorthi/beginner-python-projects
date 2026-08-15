from random import choice

default_choices = ['r', 'p', 's']
beats_conditions = {'r': 's', 'p': 'r', 's': 'p'}
names = {'r': "Rock", 'p': 'Paper', 's': 'Scissors'}

def input_method(prompt):
    return input(prompt).lower()

def is_user_win(user, computer):
    return beats_conditions[user] == computer 

def play():
    user_choice = input_method("What's your choice? 'r' for Rock, 'p' for Paper and 's' for Scissors \n")
    while user_choice not in default_choices:
        user_choice = input_method("Please select either one of these choices: 'r' for Rock, 'p' for Paper and 's' for Scissors \n")

    computer_choice = choice(default_choices)

    if user_choice == computer_choice:
        print(f"It's a tie :( \nMy choice is also '{names[computer_choice]}'")
    elif is_user_win(user_choice, computer_choice):
        print(f"You won :| \nMy choice is '{names[computer_choice]}'")
    else:
        print(f"You lost :) \nMy choice is '{names[computer_choice]}'")


def main():
    while True:
        play()
        if input_method("Play again? (y/n) \n") != 'y':
            break

if __name__ == "__main__":
    main()