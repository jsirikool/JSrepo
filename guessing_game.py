"""Guessing game by jsirikool 4/21/2017"""

import random

user_name = raw_input("Hi, What's your name? ")
print "Hi %s!" % user_name

def congratulations():
    print "Congratulations %s and thank you for playing!" % user_name

def main():
    print "I'm thinking of a number between 1 and 100."
    # randomNumber = 45 for debugging only
    randomNumber = random.randint(1, 100)
    found = False # flag variable to see if user guessed it

    while not found:
        userGuess = int(raw_input("Your guess: "))
        if userGuess == randomNumber:
            print "Ya! You got it!"
            print "The number was %d." % randomNumber
            found = True
            congratulations()
        elif userGuess > randomNumber:
            print "Guess lower."
        else:
            print "Guess higher."

if __name__ == "__main__":
    main()
