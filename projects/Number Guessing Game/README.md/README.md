# Number Guessing Game 🎯

A simple yet fun Python command-line game where the player has to guess a secret number within a limited number of attempts.

---

## 📌 Description
In this game, the computer randomly selects a number between **1 and 50**, and you have **5 attempts** to guess it.  
The program will give hints if your guess is too high or too low.

---

## ✨ Features
- Randomly generated secret number.
- Limited attempts (5 chances).
- Interactive hints after each guess.
- Simple and beginner-friendly Python project.

---

## 🛠️ Installation
1. Make sure **Python 3.x** is installed on your system.
2. Download or clone this repository:
   git clone https://github.com/yourusername/number-guessing-game.git
3. Navigate to the project folder:
cd number-guessing-game

▶️ How to Run:

Run the script using Python:
python number_guessing_game.py

📂 Code:

import random

print("\n\nWelcome to the number guessing game!")
print("\nChoose a number between 1 to 100")
print("\nYou have 5 attempts...\n")

secret_number = random.randint(1, 50)

for chance in range(1, 6):
    guess = int(input(f"\nAttempts Left {chance} - Enter your number :"))
    if guess == secret_number:
        print("\nYayy! You entered the correct number!")
        break
    elif guess < secret_number:
        print("Too Low!")
    else:
        print("Too High!")

print(f"\n\nThe secret number was : {secret_number}\n")


📸 Example Output:

Welcome to the number guessing game!

Choose a number between 1 to 100
You have 5 attempts...

Attempts Left 1 - Enter your number : 25
Too Low!

Attempts Left 2 - Enter your number : 40
Too High!

Attempts Left 3 - Enter your number : 35
Yayy! You entered the correct number!

The secret number was : 35

📄 License
This project is licensed under the MIT License - feel free to modify and use it.

👤 Author
Ankur Dhar
📧 Email: ankurdhar69@gmail.com
💻 GitHub: ankurdhar07