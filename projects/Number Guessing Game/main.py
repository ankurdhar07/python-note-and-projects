import random
print("\n\nWelcome to the number guessing game!")
print("\nChoose a number between 1 to 100")
print("\nYou have 5 attempts...\n")
secret_number = random.randint(1, 100)
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