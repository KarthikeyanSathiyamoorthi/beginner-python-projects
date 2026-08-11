import math

def guess_number_by_computer(x, num_in_my_mind):
    max_attempts = math.ceil(math.log2(x))
    isGuessed = False
    first_param = 1
    second_param = x
    print(f"My guessed number is this: {num_in_my_mind}")
    num_of_attempts = 0

    while not isGuessed and num_of_attempts < max_attempts:
        random_number = (first_param + second_param) // 2
        num_of_attempts += 1
        my_response = input(f"My Guessing number is this {random_number}. Is it Correct? ").lower()
        if my_response == 'h':
            second_param = random_number - 1
        elif my_response == 'l':
            first_param = random_number + 1
        elif my_response == 'c':
            isGuessed = True
            print(f"Yah! I have guessed the number {random_number} correctly in {num_of_attempts} attempts !!!")
            break
        else:
            print("Please enter 'h' (too high), 'l' (too low), or 'c' (correct).")
            num_of_attempts -= 1

    else:
        print(f"Out of attempts! The number was {num_in_my_mind}")


guess_number_by_computer(1000, 557)