"""
Created on Thu Sep 20 19:51:52 2018

@author: Nedrow, Vanessa

Grade School math program; for grades 1 thru 3
"""

import random


def compare(num1, num2):
    """returns the two numbers provided in order, highest to lowest.
    max() only returned highest"""
    if num1 > num2:
        return num1, num2
    return num2, num1

 # allows for repeated tries of a problem if answer is incorrect
VALIDATION = False
RANDOM_NUM1 = random.randint(0, 100)
RANDOM_NUM2 = random.randint(0, 100)

TRAIN = input("What would you like to learn?\n"
              "1) Addition (numbers 0 to 100)\n"
              "2) Subtraction (numbers 0 to 100)\n"
              "3) Multiplication (numbers 0 to 100)\n"
              "4) Division (numbers 0 to 100; significant decimal"
              "places = 3)\n")

if TRAIN == "1":
    CORRECT_ANSWER = RANDOM_NUM1 + RANDOM_NUM2
    TEXT = "What is " + str(RANDOM_NUM1) + " + " + str(RANDOM_NUM2) + "?"

elif TRAIN == "2":
    # prevent negative numbers
    RANDOM_NUM1, RANDOM_NUM2 = compare(RANDOM_NUM1, RANDOM_NUM2)
    CORRECT_ANSWER = RANDOM_NUM1 - RANDOM_NUM2
    TEXT = "What is " + str(RANDOM_NUM1) + " - " + str(RANDOM_NUM2) + "?"
elif TRAIN == "3":
    CORRECT_ANSWER = RANDOM_NUM1 * RANDOM_NUM2
    TEXT = "What is " + str(RANDOM_NUM1) + " * " + str(RANDOM_NUM2) + "?"

elif TRAIN == "4":
     # allows composite numbers, but no qoutient < 1
    RANDOM_NUM1, RANDOM_NUM2 = compare(RANDOM_NUM1, RANDOM_NUM2)
    if RANDOM_NUM2 == 0:
        RANDOM_NUM2 = random.randint(1, RANDOM_NUM1) # do not divide by zero!
    CORRECT_ANSWER = RANDOM_NUM1 / RANDOM_NUM2
    TEXT = "What is " + str(RANDOM_NUM1) + " / " + str(RANDOM_NUM2) + "?"
else:
    VALIDATION = True  # exit program

while not VALIDATION:
    print(TEXT) # equation to be solved
    YOUR_ANSWER = float(input(">>>"))
    DIFF = CORRECT_ANSWER - YOUR_ANSWER
    # for division, expect level of significance of 3 or more
    if abs(DIFF) > .0001:
        print("You were off by ", abs(round(DIFF, 3)), "in your answer."
              "  Why don't you try again?")
    else:
        print("You got it!  Great Job!")
        VALIDATION = True
input("Press enter to exit")
