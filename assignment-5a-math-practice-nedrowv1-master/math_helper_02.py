"""
Created on Sun Sept 30 19:51:52 2018

@author: Nedrow, Vanessa

Grade School math program; for grades 1 thru 4
"""

import random


def compare(num1, num2):
    """returns the two numbers provided in order, highest to lowest.
    max() only returned highest"""
    if num1 > num2:
        return num1, num2
    return num2, num1


def validate(correct, ptext, num, num_problems):
    """checks that the answer is correct"""
    global VALIDATION
    global CHANGE

    print(ptext)  # equation to be solved
    answer = float(input(">>>"))
    difference = correct - answer
    # for division, expect level of significance of 3 or more
    if abs(difference) > .0001:
        print("You were off by ", abs(round(difference, 4)), "in your answer."
              "Why don't you try again?")
        try_again = input("[T]ry again or [G]ive up?\n>>>")
        if try_again == "":
            try_again = "Try Again"

        if try_again[0].casefold() != "g".casefold() \
           and try_again[0].casefold() != "t".casefold():
            try_again = "Try Again"

        if try_again[0].casefold() == "g".casefold():
            VALIDATION = True
            if num + 1 != num_problems:
                check_chg = input("Do you want to change the type of problems you're working on? "  # line too long
                                  "[Y]es/[N]o\n>>>")
                if check_chg[0].lower() == "y".lower():
                    CHANGE = True

        elif try_again[0].casefold() != "t".casefold():
            # allows for repeated tries of a problem if answer is incorrect
            if num + 1 != num_problems:
                check_chg = input("Do you want to change the type of problems you're working on? "  # line too long
                                  "[Y]es/[N]o\n>>>")
                if check_chg[0].lower() == "y".lower():
                    CHANGE = True
    else:
        print("You got it!  Great Job!")
        VALIDATION = True
        if num + 1 != num_problems:
            check_chg = input("Do you want to change the type of problems you're working on? "  # line too long
                              "[Y]es/[N]o\n>>>")
            if check_chg[0].casefold() == "y".casefold():
                CHANGE = True


def get_answer():
    """get the correct answer and text for expression"""
    global TRAIN
    global PLAY
    global VALIDATION

    rand_num1 = random.randint(0, 100)
    rand_num2 = random.randint(0, 100)

    if TRAIN == "1":
        corr_ans = rand_num1 + rand_num2
        txt = "What is " + str(rand_num1) + " + " + str(rand_num2) + "?"

    elif TRAIN == "2":
        # prevent negative numbers
        rand_num1, rand_num2 = compare(rand_num1, rand_num2)
        corr_ans = rand_num1 - rand_num2
        txt = "What is " + str(rand_num1) + " - " + str(rand_num2) + "?"

    elif TRAIN == "3":
        corr_ans = rand_num1 * rand_num2
        txt = "What is " + str(rand_num1) + " * " + str(rand_num2) + "?"

    elif TRAIN == "4":
        # allows composite numbers, but no qoutient < 1
        rand_num1, rand_num2 = compare(rand_num1, rand_num2)
        if rand_num2 == 0:
            rand_num2 = random.randint(1, rand_num1)  # do not divide by zero!
        corr_ans = rand_num1 / rand_num2
        txt = "What is " + str(rand_num1) + " / " + str(rand_num2) + "?"

    else:
        PLAY = False
        VALIDATION = True  # exit program
        corr_ans = 0
        txt = ""

    return corr_ans, txt


def type_switch():  # two blank lines before/after function declaration
    """switch between different operators"""
    global VALIDATION
    global TRAIN
    global CHANGE
    global RANDOM_OPS

    VALIDATION = False

    if CHANGE:
        CHANGE = False
        RANDOM_OPS = False
        TRAIN = input("What would you like to learn?\n"
                      "1) Addition (numbers 0 to 100)\n"
                      "2) Subtraction (numbers 0 to 100)\n"
                      "3) Multiplication (numbers 0 to 100)\n"
                      "4) Division (numbers 0 to 100; significant decimal "
                      "places = 3)\n"
                      "5) Random Selection\n>>>")
    if TRAIN == "5":
        RANDOM_OPS = True

    if RANDOM_OPS:
        # random selection
        operator = random.choice("+-/*")
        if operator == "+":
            TRAIN = "1"
        elif operator == "-":
            TRAIN = "2"
        elif operator == "/":
            TRAIN = "3"
        elif operator == "*":
            TRAIN = "4"

    return get_answer()


VALIDATION = False
PLAY = True
CHANGE = False
RANDOM_OPS = False

while PLAY:
    TRAIN = input("What would you like to learn?\n"
                  "1) Addition (numbers 0 to 100)\n"
                  "2) Subtraction (numbers 0 to 100)\n"
                  "3) Multiplication (numbers 0 to 100)\n"
                  "4) Division (numbers 0 to 100; significant decimal"
                  "places = 3)\n"
                  "5) Random Selection\n>>>")
    NUM_PROBLEMS = int(input("How many problems of this type would you like to try?\n>>>"))  # line too long
    for NUM in range(NUM_PROBLEMS):
        CORRECT_ANSWER, TEXT = type_switch()
        while not VALIDATION:
            validate(CORRECT_ANSWER, TEXT, NUM, NUM_PROBLEMS)
    PLAY_CHECK = input("Continue? [Y]es/[N]o\n>>>")
    if PLAY_CHECK[0].casefold() == "n".casefold():
        PLAY = False

input("Press enter to exit")

'''Great work.  Just a few lines > 79 characters (tabs count as 4)'''
