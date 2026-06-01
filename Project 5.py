import random
print("Welcome to the number guessing game")
number_to_guess = random.randint(1,10)
guess = None
while guess != number_to_guess:
    try:
        guess = int(input("Enter your guess(1-10):"))
    except ValueError:
        print("Please enter a valid number.")
    print("You finished the while statement.")
    continue
if guess < number_to_guess:
    print("Too low! Try again.")
elif guess > number_to_guess:
    print("Too high! Try again.")
else:
    print(f"Congratulations! You guessed the number: {number_to_guess}")