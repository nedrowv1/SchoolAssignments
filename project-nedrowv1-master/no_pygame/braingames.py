import random
from collections import Counter


"""colors used in game"""
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TAN = (222, 184, 135)
ORANGE = (255, 128, 0)


class Peg(object):
    """a single peg.  location attribute is used for pygame integration"""
    def __init__(self, color, locIndex=None):
        self.color = color
        self.location = locIndex

    def __eq__(self, other):
        return self.color == other.color

    def hue(self):
        return self.color


class pegRow(object):
    def __init__(self):
        self.pegs = []

    def __eq__(self, other):
        if len(self.pegs) == len(other.pegs):
            for pIndex in range(len(self.pegs)):
                if self.pegs[pIndex] == other.pegs[pIndex]:
                    pass
                else:
                    return False
            return True
        return False

    def __str__(self):
        printvalue = []
        revert = {RED: "red", BLUE: "blue", GREEN: "green", PURPLE: "purple", YELLOW: "yellow", TAN: "tan",
         WHITE: "white", BLACK: "black", ORANGE: "orange"}
        for i in self.pegs:
            textcolor = revert[i.color]
            printvalue.append(textcolor)
        return str(printvalue)

    def all_colors(self):
        return ("red", "blue", "green", "purple", "yellow", "tan",
                     "white", "black", "orange")



class answerRow(pegRow):
    def __init__(self, numpegs=5):

        self.pegchoices = {"red": RED, "blue": BLUE, "green": GREEN, "purple": PURPLE, "yellow": YELLOW, "tan": TAN,
                           "white": WHITE, "black": BLACK, "orange": ORANGE}

        pegcolors = ("red", "blue", "green", "purple", "yellow", "tan",
                     "white", "black", "orange")
        self.pegs = []

        for pIndex in range(numpegs):
            blind_peg = random.choice(pegcolors)
            self.pegs.append(Peg(self.pegchoices[blind_peg]))


class guessRow(pegRow):
    def __init__(self, numpegs=5):
        self.pegchoices = {"red": RED, "blue": BLUE, "green": GREEN, "purple": PURPLE, "yellow": YELLOW, "tan": TAN,
                           "white": WHITE, "black": BLACK, "orange": ORANGE}
        self.answerkey = []
        self.pegs = [None] * numpegs

    def add_peg(self, colors, pIndex, locIndex=None):
        self.pegs[pIndex] = Peg(color=colors, locIndex=locIndex)

    def is_equal(self, other):
        self.answerkey = [WHITE] * len(other.pegs)
        cntr = 0
        aCounter = {RED: 0, BLUE: 0, GREEN: 0, YELLOW: 0, PURPLE: 0, ORANGE: 0, TAN: 0, WHITE: 0,
                    BLACK: 0}
        others = []
        for pIndex in range(len(other.pegs)):
            others.append(other.pegs[pIndex].hue())
        bCounter = Counter(others)
        for pIndex in range(len(self.pegs)):
            if type(self.pegs[pIndex]) != int: # catch initilization errors
                if self.pegs[pIndex] in other.pegs:
                    if aCounter[self.pegs[pIndex].hue()] < bCounter[self.pegs[pIndex].hue()]:
                        self.answerkey[cntr] = RED
                        aCounter[self.pegs[pIndex].hue()] += 1
                        cntr += 1
        cntr = 0
        for peg in range(len(self.pegs)):
            if self.pegs[peg] == other.pegs[peg]:
                self.answerkey[cntr] = GREEN
                cntr += 1
        return self.answerkey


def convert(item):
    wrongplace = 0
    rightplace = 0
    for i in item:
        if i == GREEN:
            rightplace += 1
        elif i == RED:
            wrongplace += 1
        else:
            break
    return rightplace, wrongplace


def new_game():
    guesssize = 5
    answer = answerRow(guesssize)
    while True:
        guess = guessRow(guesssize)
        guess_text = []
        for i in range(guesssize):
            print("Enter a color from the below list.  The current guess size is {}:".format(guesssize))
            color = input("{}\n>>>".format(guess.all_colors()))
            while True:
                try:
                    guess.add_peg(guess.pegchoices[color], i)
                    break
                except KeyError:
                    print("There was an error in your guess.  You entered {}, the only available options are:\n"
                          "{}".format(color, guess.all_colors()))
                    color = input(">>>")
        print(guess)
        if guess == answer:
            return True
        else:
            right, wrong = convert(guess.is_equal(answer))
            total = right + wrong
            print("you have {} pegs of the correct colors, {} are in the right spot".format(total, right))

if __name__ == "__main__":
    new_game()
