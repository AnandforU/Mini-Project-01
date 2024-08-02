import random

def number_guessing_game():
    while True:
            x = int(input("Enter the lower bound of the range (X): "))
            y = int(input("Enter the upper bound of the range (Y): "))
            if x < y:
                break
            else:
                print("The lower bound must be less than the upper bound. Try again.")

    random_number = random.randint(x, y)
    attempts = 0

    print(f"Guess the number between {x} and {y}")

    while True:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == random_number:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
            elif guess < random_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

if __name__ == "__main__":
    number_guessing_game()
