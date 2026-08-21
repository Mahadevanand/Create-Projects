import random

# Number of attempts allowed for each difficulty level
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


# Function to set the number of attempts based on difficulty
def set_difficulty(level_chosen):

    # Easy level gives 10 attempts
    if level_chosen == "easy":
        return EASY_LEVEL_ATTEMPTS

    # Hard level gives 5 attempts
    elif level_chosen == "hard":
        return HARD_LEVEL_ATTEMPTS

    # Return None if the difficulty is invalid
    else:
        return None


# Function to check whether the user's guess is correct
def check_answer(guessed_number, answer, attempts):

    # If the guess is smaller than the answer
    if guessed_number < answer:
        print("Too low.")
        return attempts - 1

    # If the guess is greater than the answer
    elif guessed_number > answer:
        print("Too high.")
        return attempts - 1

    # If the guess is correct
    else:
        print(f"You guessed it right! The answer was {answer}.")
        return attempts


# Main function for the guessing game
def game():

    # Display the game instructions
    print("I'm thinking of a number between 1 and 50.")

    # Generate a random number between 1 and 50
    answer = random.randint(1, 50)

    # Ask the user to choose a difficulty level
    level = input(
        "Choose a difficulty. Type 'easy' or 'hard': "
    ).lower()

    # Get the number of attempts based on the selected difficulty
    attempts = set_difficulty(level)

    # Check if the user entered an invalid difficulty
    if attempts is None:
        print("Invalid difficulty choice.")
        return

    # Initialize guessed_number
    guessed_number = 0

    # Continue the game while the guess is incorrect
    # and the user still has attempts
    while guessed_number != answer and attempts > 0:

        # Display the number of remaining attempts
        print(f"\nYou have {attempts} attempts remaining.")

        # Ask the user to enter a guess
        guessed_number = int(input("Make a guess: "))

        # Check the guess and update the number of attempts
        attempts = check_answer(
            guessed_number, answer, attempts
        )

        # If the guess is incorrect and attempts are remaining,
        # ask the user to guess again
        if guessed_number != answer and attempts > 0:
            print("Guess again.")

    # If the user has no attempts left, the game is over
    if attempts == 0:
        print("\nYou've run out of guesses. You lose!")

        # Display the correct answer
        print(f"The answer was {answer}.")


# Start the game
game()
