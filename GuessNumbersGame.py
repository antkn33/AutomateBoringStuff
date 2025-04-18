# guess the number game

import random

print("Hello, what is your name?")
name = input()

print("Well, " + name + ", I am thinking of a number between 1 and 20.")
secretNumber = random.randint(1, 20)

#print("DEBUG: Secret number is: " +str(secretNumber))

for guessTaken in range(1, 7): # gives 6 guesses
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high")
    else:
        break # guess is correct. breaks out of loop 

if guess == secretNumber:
    print("Your guess is correct! You took " + str(guessTaken) + " guesses.")
else:
    print("Too many guesses. The number was " + str(secretNumber))

