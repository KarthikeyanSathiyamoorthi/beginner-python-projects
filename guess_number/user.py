from random import randint

def guess_number(x):
    random_num = randint(1, x)
    num_of_attempts = 0

    while num_of_attempts < 7:
        try: 
            guessed_num = int(input("Enter the guessed number: "))
            num_of_attempts += 1
            if guessed_num > random_num:
                print("It's too high !!!")
            elif guessed_num < random_num:
                print("It's too low !!!")
            else:
                print(f"Yah! You have guessed the number {guessed_num} correctly in {num_of_attempts} attempts !!!")
                break

        except ValueError:
            print("Please enter a valid number")
            continue
    else:
        print(f"Out of attempts! The number was {random_num}.")

guess_number(100)
