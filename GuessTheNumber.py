#
import random

print("Hello what is your name")
name = input()

print("Well, " + name + ", I am thinking of a number between 1 & 20.")
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print("Take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break # this condition is for a correct guess

if guess == secretNumber:
        print(f"Good job, {name} !. You guessed the number in {guessesTaken} guesses.")
else:
     print(f"Too many guesses. The number was {secretNumber}.")



