# Higher Lower Game

A simple Python console game where the player guesses which celebrity has more followers.

## Features
- Random account comparison
- Score tracking
- ASCII art interface
- Continuous gameplay until a wrong answer

## Technologies Used
- Python
- random module
- os module

## Project Structure
```
main.py
game_art.py
game_database.py
```

## How to Run

1. Clone the repository

```bash
git clone https://github.com/yourusername/Higher-Lower-Game.git
```

2. Open the project folder

```bash
cd Higher-Lower-Game
```

3. Run the game

```bash
python main.py
```

## Example

```
Compare 1: Cristiano Ronaldo
VS
Compare 2: Taylor Swift

Who has more followers? 1 or 2:
```

## Author

Your Name
Mahdevanand

code: 

import random
import os
import game_art
import game_database

print(game_art.game_logo)
score=0

def display_accountinfo(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, followers_count_1, followers_count_2):
    if followers_count_1 > followers_count_2:
        return guess == 1
    else:
        return guess == 2


account_2 = random.choice(game_database.data)
continue_flag = True
while continue_flag:
    account_1 = account_2
    account_2 = random.choice(game_database.data)
    while account_1 == account_2:
        account_2 = random.choice(game_database.data)

    print(f"Compare 1 : {display_accountinfo(account_1)}")
    print(game_art.vs)
    print(f"Compare 2 : {display_accountinfo(account_2)}")


    guess = int(input("Who has more followers? 1 or 2 : "))

    followers_count_1 = account_1["follower_count"]
    followers_count_2 = account_2["follower_count"]

    is_correct=check_answer(guess, followers_count_1, followers_count_2)
    os.system("cls" if os.name == "nt" else "clear")
    print(game_art.game_logo)
    if is_correct:
        score+=1
        print(f"You are right. Your score is : {score}")
    else:
        print(f"You are wrong. Your final score is : {score}")
        continue_flag = False


