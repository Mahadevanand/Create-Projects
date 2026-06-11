import random
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def set_difficulty(level_chosen):
    if level_chosen == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen == "hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        return None


def check_answer(guessed_number, answer, attempts):
    if guessed_number < answer:
        print("Too low.")
        return attempts - 1
    elif guessed_number > answer:
        print("Too high.")
        return attempts - 1
    else:
        print(f"You guessed it right! The answer was {answer}.")
        return attempts


def game():
    print("I'm thinking of a number between 1 and 50.")

    answer = random.randint(1, 50)

    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = set_difficulty(level)

    if attempts is None:
        print("Invalid difficulty choice.")
        return

    guessed_number = 0

    while guessed_number != answer and attempts > 0:
        print(f"\nYou have {attempts} attempts remaining.")

        guessed_number = int(input("Make a guess: "))

        attempts = check_answer(guessed_number, answer, attempts)

        if guessed_number != answer and attempts > 0:
            print("Guess again.")

    if attempts == 0:
        print(f"\nYou've run out of guesses. You lose!")
        print(f"The answer was {answer}.")


game()
