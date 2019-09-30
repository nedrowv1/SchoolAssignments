import random
from collections import Counter
import re


class Die(object):
    """a single die, top face
        faces: the number of sides on the die
        top: the value of the top side face
        attributes: faces, top"""

    def __init__(self, faces):
        """standard die has a set number of faces and a value for the face
        that is pointing upward"""
        self.faces = faces
        self.top = self.roll()

    def __eq__(self, other):
        """check if two die, or a number representing the upward face
        match"""
        if isinstance(other, Die):
            return self.top == other.top
        return self.top == other

    def __add__(self, other):
        """add a number to a die, or two die together"""
        if isinstance(other, Die):
            return self.top + other.top
        return self.top + int(other)

    def __radd__(self, other):
        """add a number to a die"""
        return self.top + int(other)

    def roll(self):
        """reroll die"""
        self.top = random.randint(1, self.faces)
        return self.top

    def __hash__(self):
        """allow a die to be used as the key in a dictionary, I guess?
        not sure why I had to add it, but the ditionaries didn't work
        without it"""
        return hash(str(self))

    def __lt__(self, other):
        """compare die"""
        if isinstance(other, Die):
            return self.top < other.top
        else:
            return self.top < other

    def __gt__(self, other):
        """compare die"""
        if isinstance(other, Die):
            return self.top > other.top
        return self.top > other

    def __repr__(self):
        return str(self.top)


class YachtDie(Die):
    """a die specifically for use in Yacht.  had additional attribute
    to check if the dice should be rolled or not, and one for pygame
    integration

    attributes: held_color(for pygame), hold"""
    def __init__(self):
        """held_color is for pygae integration, hold=True prevents the die
        from rolling in a given round"""
        super(YachtDie, self).__init__(6)
        self.hold = False

    def is_held(self):
        """return the value of hold"""
        return self.hold


class YatzeeRoll(object):
    """1 - 5 dice rolled together
    attributes: dice, size, rolls_left"""

    def __init__(self, size=5, maxrolls=3):
        """standard Yacht game uses five die, and three rolls."""
        self.size = size
        self.dice = []
        self.rolls_left = maxrolls
        for i in range(size):
            self.dice.append(YachtDie())

    def is_held(self, index):
        """checks if a die of a given index is held"""
        return self.dice[index].is_held()

    def die(self, index):
        """return a die of a specific index"""
        return self.dice[index]

    def roll(self):
        """roll die in hand"""
        if self.rolls_left > 0:
            for i in range(self.size):
                if not self.is_held(i):
                    self.die(i).roll()
            self.rolls_left -= 1
        else:
            raise Exception("reached maximum number of rolls")

    def hold(self, index):
        """hold a die"""
        self.dice[index].hold = True

    def release_hold(self, index):
        """release hold on a die"""
        self.dice[index].hold = False

    def end_turn(self):
        """start the next round of play by resetting the number of
        rolls available and removing the hold from all die"""
        self.rolls_left = 3
        for i in range(self.size):
            self.dice[i].hold = False

    def tops(self):
        """used for 'in' operation and for 'Counter' object
        escentially converting the Die into an integer"""
        for i in self.dice:
            yield i.top

    def __contains__(self, value):
        """checks if a value is in a roll"""
        return value in self.tops()

    def __getitem__(self, index):
        """allows indexing"""
        return self.dice[index]

    def __iter__(self):
        """iterate through dice in hand"""
        self.i = 0
        return self

    def __next__(self):
        """iternate through dice in hand"""
        if self.i < self.size:
            result = self.dice[self.i]
            self.i += 1
            return result
        else:
            raise StopIteration

    def sort(self):
        """sort dice in hand"""
        self.dice.sort()
        return self

    def __str__(self):
        return str(self.dice)

    def print_held(self):
        temp = []
        for i in range(self.size):
            if self.is_held(i) == True:
                held = "Held"
            else:
                held = "Open"
            temp.append((self.dice[i], held))
        return temp

def available_scores(diecup, max_score=-1):
    """determine what scores are still needed for end game."""
    tempup = upperscores(diecup)
    tempdown = lowerscores(diecup)

    upperboxes = {}
    lowerboxes = {}
    for a_type in tempup:
        if upper_scores[a_type] == 0 and tempup[a_type] > max_score:
            upperboxes[a_type] = tempup[a_type]
    for a_type in tempdown:
        if lower_scores[a_type] == 0 and tempdown[a_type] > max_score:
            lowerboxes[a_type] = tempdown[a_type]
    return upperboxes, lowerboxes


def setscore(s_type, s_amt):
    """update player score with selected score"""
    if s_amt == 0:
        s_amt = -1
    if s_type in upper_scores:
        upper_scores[s_type] = s_amt
    elif s_type in lower_scores:
        lower_scores[s_type] = s_amt


def straight(cup, st_type):
    """return rolls point value for small and large straight.  st_type
    check for large over small straight"""
    if 3 in cup and 4 in cup:
        if st_type == "large":
            if 2 in cup and 5 in cup:
                if 1 in cup or 6 in cup:
                    return 40
        elif st_type == "small":
            if (1 in cup and 2 in cup) \
                    or (2 in cup and 5 in cup) \
                    or (5 in cup and 6 in cup):
                return 30
    return 0


def akind(cup, num, k=0):
    """checks for pairs, three of a kind, four of a kind and yacht"""
    scores = {2: 2, 3: sum(cup), 4: sum(cup), 5: 50}
    temp = cup[k]
    cnt = 0
    score = 0
    for i in cup:
        if i == temp:
            cnt += 1
    if cnt >= num != 2:
        score = scores[num]
    elif cnt == num and num == 2:  # prevent invalid Full House
        score = scores[num]
    else:
        if k < (cup.size - 1):
            score = akind(cup, num, k + 1)
    return score


def fullhouse(cup):
    """check that a roll has three of one die value and two of a another"""
    cnt1 = akind(cup, 2)
    cnt2 = akind(cup, 3)
    if cnt1 > 0 and cnt2 > 0:
        return 25
    return 0


def upperscores(cup):
    """returns the available scores for the upper section of the score
    board given a specific roll"""
    temp = Counter(cup.tops())
    upper = {"Ones": temp[1] * 1, "Twos": temp[2] * 2,
             "Threes": temp[3] * 3, "Fours": temp[4] * 4,
             "Fives": temp[5] * 5, "Sixes": temp[6] * 6}
    return upper


def lowerscores(sorteddice):
    """return the available scores for the lower section of the score board
    given a specific roll"""
    lower = {"Chance": sum(sorteddice.tops()),
             "Small Straight": straight(sorteddice,
                                        "small"),
             "Large Straight": straight(sorteddice, "large"),
             "Full House": fullhouse(sorteddice),
             "Three of a Kind": akind(sorteddice, 3),
             "Four of a Kind": akind(sorteddice, 4),
             "Yacht": akind(sorteddice, 5)
             }
    return lower


def getuptotal():
    """get the sum total of the upper section"""
    total = 0
    for i in upper_scores:
        if upper_scores[i] != -1 and i != "Total" and i != "Bonus":
            total += upper_scores[i]
    if total > 63:
        print(total)
        upper_scores["Bonus"] = 35
        
    upper_scores["Total"] = total + upper_scores["Bonus"]


def getlowtotal():
    """get the sum total of the lower section, and the entire board"""
    total = 0
    for i in lower_scores:
        if lower_scores[i] != -1 and (i != "Total" and i != "Final Score"):
            total += lower_scores[i]
    lower_scores["Total"] = total
    lower_scores["Final Score"] = total + upper_scores["Total"]


def game_over():
    for score in upper_scores:
        if upper_scores[score] == 0 and score != "Bonus":
            return False
    for score in lower_scores:
        if lower_scores[score] == 0 and score != "Yacht Bonus":
            return False
    return True
        
def new_game():
    global upper_scores, lower_scores
    player1_dicecup = YatzeeRoll()
    temp = ""
    upper_scores = {"Ones": 0, "Twos": 0, "Threes": 0, "Fours": 0,
                        "Fives": 0, "Sixes": 0, "Bonus": 0, "Total": 0}
    lower_scores = {"Full House": 0, "Small Straight": 0,
                        "Large Straight": 0, "Three of a Kind": 0,
                        "Four of a Kind": 0, "Chance": 0, "Yacht": 0,
                        "Yacht Bonus": 0, "Total": 0, "Final Score": 0}
    game = False
    while not game:
        if player1_dicecup.rolls_left > 0:
            player1_dicecup.roll()
            player1_dicecup.sort()
            print(player1_dicecup.print_held())
        if player1_dicecup.rolls_left > 0:
            while True:
            
                helddice = input("which dice would you like to hold?  list them, comma separated 1 to 5\n"
                                 "Press enter to score\n>>>")
                if helddice:
                    temp = ""
                    for char in helddice:
                        if char == ",":
                            index = int(temp)
                            if index not in range(1, 6):
                                print("Please only enter values between 1 and 5")
                                break
                            else:
                                if player1_dicecup.is_held(index-1):
                                    hold = input("Die {} has previously been held.  Do you want to release the hold? Y or N".format(index))
                                    if hold.casefold() == "y".casefold():
                                        player1_dicecup.release_hold(index-1)
                                        temp = ""
                                else:
                                    player1_dicecup.hold(index-1)
                                    temp = ""
                        else:
                            temp += char
                    try:
                        index = int(temp)
                        if player1_dicecup.is_held(index-1):
                            hold = input("Die {} has previously been held.  Do you want to release the hold? Y or N".format(index))
                            if hold.casefold() == "y".casefold():
                                player1_dicecup.release_hold(index-1)
                                temp = ""
                        else:
                            player1_dicecup.hold(index-1)
                            temp = ""
                        break
                    except ValueError:
                        break
                    except IndexError:
                        print("Please only enter values between 1 and 5")
                else:
                    score = input("Would you like to score this round? Y or N")
                    if score.casefold() == "y".casefold():
                        player1_dicecup.rolls_left = 0
                    break
        else:
            UpperScores_Temp, LowerScores_Temp = available_scores(player1_dicecup)
            print("Potential Scores for the upper section are:\n{}\n\n"
                  "Potential Scores for the lower section are:\n{}\n".format(UpperScores_Temp, LowerScores_Temp))
            invalid = True
            while invalid:
                scored = input("Enter the score you want to use\n>>>")
                newword = ""
                word_list = list(scored)
                for word in word_list:
                    word.capitalize()
                scored = str(word_list)
                key = ""
                for letter in scored:
                    if letter in "[',] ":
                        pass
                    else:
                        if letter == letter.capitalize():
                            key += " " + letter
                        else:
                            key += letter
                if re.match(r" ", key):
                    key = re.sub(r" ", "", key, 1)
                if "ofa" in key:
                    key = re.sub("ofa", " of a", key)
                if key in upper_scores:
                    value = UpperScores_Temp[key]
                    invalid = False
                    setscore(key, value)
                    getuptotal()
                    getlowtotal()
                    player1_dicecup.end_turn()
                elif key in lower_scores:
                    value = LowerScores_Temp[key]
                    invalid = False
                    setscore(key, value)
                    getlowtotal()
                    player1_dicecup.end_turn()
                else:
                    print("You entered '{}'.  This is not a valid score type.".format(key))
            print("Your current score for the upper section is: {}, including a {} point bonus\n"
                  "Your current score for the lower section is: {}, including a {} point multiple "
                  "Yacht bonus\n"
                  "You total score is {}".format(upper_scores["Total"], upper_scores["Bonus"],
                                                 lower_scores["Total"], lower_scores["Yacht Bonus"],
                                                 lower_scores["Final Score"]))
            print("Upper Section scores: {}\nLower Section scores: {}".format(upper_scores, lower_scores))
        game = game_over()
    if lower_scores["Final Score"] > 199:
        return True
    return False

if __name__ == "__main__":
    new_game()
        
