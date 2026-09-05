import json
from random import choice

# getting words from JSON file
with open('words.json', 'r') as file:
    json_data = json.load(file)
    words = json_data['words']


def join_method(hidden_word):
    return "".join(hidden_word)

secret_word = choice(words).upper()
hidden = list("_" * len(secret_word))
print(f"Hidden word: {join_method(hidden)}")

while "_" in hidden:
    guess = input("Enter a letter: ").upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess not in secret_word:
        print("Sorry!!! Your letter is not there :( \nPlease enter a different letter.")
        continue

    for i, char in enumerate(secret_word):
        if char == guess and hidden[i] == '_':
            hidden[i] = char
            print(f"Hidden word: {join_method(hidden)}")
            break
    else:
        print("You already found all of those letters.")
print(f"Finally! you found the fruit: {join_method(hidden)}")