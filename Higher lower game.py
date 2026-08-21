import random
import os
import game_art
import game_database


# Display the game logo
print(game_art.game_logo)

# Initialize the score to 0
score = 0


# Function to display account information
def display_accountinfo(account):

    # Get the account name
    name = account["name"]

    # Get the account description
    description = account["description"]

    # Get the country
    country = account["country"]

    # Return the account information as a formatted string
    return f"{name}, a {description}, from {country}"


# Function to check whether the user's guess is correct
def check_answer(guess, followers_count_1, followers_count_2):

    # Check if account 1 has more followers
    if followers_count_1 > followers_count_2:

        # Return True if the user guessed account 1
        return guess == 1

    # Otherwise, account 2 has more followers
    else:

        # Return True if the user guessed account 2
        return guess == 2


# Select the first random account from the database
account_2 = random.choice(game_database.data)

# Variable used to control whether the game continues
continue_flag = True


# Continue playing while continue_flag is True
while continue_flag:

    # Move the previous account 2 to account 1
    account_1 = account_2

    # Select a new random account for account 2
    account_2 = random.choice(game_database.data)

    # Make sure account 1 and account 2 are different
    while account_1 == account_2:
        account_2 = random.choice(game_database.data)


    # Display the first account
    print(f"Compare 1 : {display_accountinfo(account_1)}")

    # Display the VS symbol
    print(game_art.vs)

    # Display the second account
    print(f"Compare 2 : {display_accountinfo(account_2)}")


    # Ask the user which account has more followers
    guess = int(input("Who has more followers? 1 or 2 : "))


    # Get the follower count of account 1
    followers_count_1 = account_1["follower_count"]

    # Get the follower count of account 2
    followers_count_2 = account_2["follower_count"]


    # Check whether the user's guess is correct
    is_correct = check_answer(
        guess,
        followers_count_1,
        followers_count_2
    )


    # Clear the console screen
    # "cls" is used for Windows
    # "clear" is used for Linux and Mac
    os.system("cls" if os.name == "nt" else "clear")


    # Display the game logo again
    print(game_art.game_logo)


    # If the user's answer is correct
    if is_correct:

        # Increase the score by 1
        score += 1

        # Display the current score
        print(f"You are right. Your score is : {score}")


    # If the user's answer is wrong
    else:

        # Display the final score
        print(f"You are wrong. Your final score is : {score}")

        # Stop the game
        continue_flag = False
