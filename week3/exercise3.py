"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the ADVANCED guessing game!")
    print("A number between _ and _ ?")

    integer = False 
    while integer == False:
      try:
        lowerBound = int(input("Enter a lower bound: "))
        integer = True
      except:
        print("No.")
    
    integer = False
    while integer == False:
      try:
        upperBound = int(input("Enter an upper bound: "))
        if upperBound > lowerBound + 1:
          integer = True
        else:
          print("Try higher.")
      except:
        print("A number please.")

    print("OK then, a number between " , lowerBound , "and" , upperBound , "?")
    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False
    while guessed == False:
      try:
        guessedNumber = int(input("Guess a number: "))
        if guessedNumber == actualNumber:
          print("Ring-a-ding-ding-baby!")
          guessed = True
        elif guessedNumber < actualNumber:
          if guessedNumber < lowerBound:
            print("Come on now...")
          else:
            print("Too small, try again :'(")
        else:
          if guessedNumber > upperBound:
            print("Come on now...")
          else:
            print("Too big, try again :'(")
      except:
        print("A number please!")

    return "You got it!"
  
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
