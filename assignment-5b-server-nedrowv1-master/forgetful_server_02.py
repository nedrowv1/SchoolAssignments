#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 14:26:26 2018

@author: Nedrow, Vanessa

The Forgetful Waiter
"""

import time
import textwrap


def apps(apporder):
    """save appetizer order"""
    word = ""
    app_order = 0
    for let in apporder:
        # sending to a function made the for-in look at letters, not word
        if let in (" ", ","):
            if word.casefold() == "figs".casefold():
                # keyword for roasted figs
                app_order = "roasted figs with goat cheese"
                break
            elif word.casefold() == "mushrooms".casefold():
                # key word for lamb and cheese mushrooms
                app_order = "lamb and goat cheese stuffed mushrooms"
                break
            word = ""
        else:
            word = word + let

    return app_order


def mains(mainorder):
    """save main course order"""
    word = ""
    main_order = 0
    for let in mainorder:
        # sending to a function made the for-in look at letters, not word
        if let in (" ", ","):
            if word.casefold() == "souffle".casefold():
                # keyword for cauliflower souffle
                main_order = "cauliflower and goat cheese souffle"
                break
            elif (
                 word.casefold() == "asparagus".casefold()
                 or word.casefold() == "penne".casefold()
                 or word.casefold() == "salad".casefold()
                 ):
                # keywords for penne salad
                main_order = "penne, asparagus, tomato and goat cheese salad"
                break
            elif (
                 word.casefold() == "prosciutto".casefold()
                 or word.casefold() == "chicken".casefold()
                 or word.casefold() == "dates".casefold()
                 ):
                # keywords for stuffed chicken
                main_order = "proscuitto wrapped chicken stuffed with dates " \
                             "and goat cheese"
                break
            elif (
                 word.casefold() == "halibut".casefold()
                 or word.casefold() == "lemon".casefold()
                 ):
                # keywords for lemon pepper halibut
                main_order = "goat cheese and lemon pepper encrusted halibut"
                break
            word = ""
        else:
            word = word + let
    return main_order


def desserts(dessertorder):
    """save desserts order"""
    word = ""
    dessert_order = 0
    for let in dessertorder:
        # sending to a function made the for-in look at letters, not word
        if let in (" ", ","):
            if (
               word.casefold() == "fried".casefold()
               or word.casefold() == "walnuts".casefold()
               ):
                # keywords in order for fried goat cheese
                dessert_order = "fried goat cheese drizzled with honey"
                break
            elif (
                 word.casefold() == "peaches".casefold()
                 or word.casefold() == "chevre".casefold()
                 or word.casefold() == "grilled".casefold()
                 ):
                # keywords in order for grilled peaches
                dessert_order = "grilled peaches with honey chèvre"
                break
            word = ""
        else:
            word = word + let
    return dessert_order


def house(houseorder):
    """determine house wine order while allowing
    exclusion of non-house wines"""
    winetype = 0
    glass = False
    word = ""
    for let in houseorder:
        # sending to a function made the for-in look at letters, not word
        if let in (" ", ","):
            if word.casefold() == "red":
                winetype = 1  # house red
            elif word.casefold() == "white":
                winetype = 2  # house white
            elif word.casefold() == "glass":
                glass = "a glass of "
            elif word.casefold() == "bottle":
                glass = "a bottle of "
            word = ""
        else:
            word = word + let

    return winetype, glass


def wines(wineorder):
    """save wine order"""
    winetype, glass = house(wineorder)
    word = ""
    wine_order = 0
    for let in wineorder:
        # sending to a function made the for-in look at letters, not word
        if let in (" ", ","):
            if word.casefold() == "house".casefold() \
               or word.casefold() == "California".casefold():
                # keywords for house wines
                if winetype == 1:
                    wine_order = "the house red"
                    break
                elif winetype == 2:
                    wine_order = "the house white"
                    break
                else:
                    # if not type specified, go generic
                    wine_order = "the house vintage"
                    break
            elif (
                 word.casefold() == "Burgandy".casefold()
                 or word.casefold() == "1999"
                 ):
                # keywords for Burgandy wine order
                wine_order = "a bottle of white Burgandy"
                break
            elif (
                 word.casefold() == "Semillon".casefold()
                 or word.casefold() == "blanc".casefold()
                 or word.casefold() == "2002"
                 ):
                # keywords for Samillon blanc
                wine_order = "a glass of the Sèmillon blanc"
                break
            elif (
                 word.casefold() == "Melblanc".casefold()
                 or word.casefold() == "2015"
                 ):
                # keywords for Melblanc
                wine_order = "a bottle of Melblanc"
                break
            elif (
                 word.casefold() == "Pinoit".casefold()
                 or word.casefold() == "Noir"
                 or word.casefold() == "2004"
                 ):
                # keywords for Pinoit Noir
                wine_order = "a glass of Pinoit Noir"
                break
            word = ""
        else:
            word = word + let

    if winetype > 0:
        wine_order = glass + wine_order
    return wine_order


def order():
    """takes customer's order"""

    # take appetizer order
    your_order = input("What appetizer would you like? Please order by "
                       "name.\n>>>")
    app_order = apps(your_order + " ")
    if app_order == 0:
        appcheck = input("The prix fixe menu comes with an appetizer. Are "
                         "you sure you don't want one?\n>>>")
        if appcheck[0].casefold() == 'n':
            your_order = input("What appetizer would you like? "
                               "Please order by name.\n>>>")
            app_order = apps(your_order + " ")

    # take main course order
    your_order = input("What main course would you like?  Please order by "
                       "name.\n"
                       ">>>")
    main_order = mains(your_order + " ")
    if main_order == 0:
        maincheck = input("The prix fixe menu comes with a main course. Are "
                          "you sure you don't want one?\n>>>")
        if maincheck[0].casefold() == 'n':
            your_order = input("What main course would you like? Please "
                               "order by "
                               "name.\n>>>")
            main_order = mains(your_order + " ")

    # take dessert order
    your_order = input("What dessert would you like?  Please order by "
                       "name.\n>>>")
    dessert_order = desserts(your_order + " ")
    if dessert_order == 0:
        dessertcheck = input("The prix fixe menu comes with a dessert. Are "
                             "you sure you don't want one?")
        if dessertcheck[0].casefold() == 'n':
            your_order = input("What dessert would you like? Please order by "
                               "name.\n>>>")
            dessert_order = desserts(your_order + " ")

    # take wine order
    your_order = input("What wine would you like?  Please order by "
                       "name\n>>>")
    wine_order = wines(your_order + " ")

    return app_order, main_order, dessert_order, wine_order


def print_wrap(text):
    """print wrapped text"""
    for line in text:
        print(line)


def prixtext():
    """menu text"""

    prix = textwrap.wrap("Today's three course "
                         "prix fixe meal starts with your choice of roasted "
                         "figs "
                         "with goat cheese "
                         "or goat cheese and lamb stuffed mushrooms.")
    print_wrap(prix)
    time.sleep(5)
    prix = textwrap.wrap("The vegetarian mains include either a cauliflower "
                         "and goat cheese "
                         "souffle, served "
                         "with roasted peppers and chard or a roasted "
                         "asparagus and tomato salad tossed with "
                         "pepper, olive oil, penne and "
                         "goat cheese.")
    print()
    print_wrap(prix)
    time.sleep(5)
    prix = textwrap.wrap("We also have prosciutto wrapped chicken "
                         "stuffed with goat cheese, shallots, dates and "
                         "basil or a lemon pepper and goat "
                         "cheese encrusted halibut served with wild rice "
                         "and seasonal vegetables.")
    print()
    print_wrap(prix)
    time.sleep(5)
    print()
    prix = textwrap.wrap("For dessert, we have fried goat cheese and walnuts "
                         "drizzled with honey "
                         "or grilled peaches with a honey chèvre.")
    print_wrap(prix)
    print()


def winetext():
    """wine list text"""
    wine = textwrap.wrap("The house red and white are both from California.  "
                         "The red has notes of cedar.  The white is dry, "
                         "with hints of "
                         "apple and honeydew.  Both are available by the "
                         "glass or the "
                         "bottle.")
    print_wrap(wine)
    print()
    time.sleep(5)
    wine = textwrap.wrap("We also have a 1999 white Burgandy, available in "
                         "the bottle, a Sèmillon blanc from 2002 available "
                         "by the "
                         "glass - it is a very "
                         "good year, though as a machine I have never "
                         "tried it.")
    print_wrap(wine)
    print()
    time.sleep(5)
    wine = textwrap.wrap("For reds we have a 2015 Melblanc by the bottle and "
                         "a "
                         "2004 Pinot Noir by the glass.")
    print_wrap(wine)


LASTNAME = ""

GREETING = textwrap.wrap("Welcome to G.O.A.T - the greatest restaurant in "
                         "the universe!  I will "
                         "be your host for the evening.  If I could verify "
                         "your reservation?", 70)
print_wrap(GREETING)
NAME = input("Please enter your name, surname first: \n>>>")

for letter in NAME:
    if letter in (" ", ","):
        break
    else:
        LASTNAME += letter

print("Ah yes,", LASTNAME.capitalize(), "San.  We have your table over here.")
time.sleep(10)
PRIX = textwrap.wrap("And here is your table.  There will be a waterbot "
                     "by in a moment to fill your glasses.")
print()
print_wrap(PRIX)
prixtext()
time.sleep(5)
winetext()
time.sleep(5)
WINE = APP = MAIN = DESSERT = 0
WAITED = False
ANSWER = input("And are you ready to order?\n>>>")
while "no".casefold() in ANSWER.casefold():
    print("That's fine.  I will give you a minute to think it over.")
    time.sleep(60)
    ANSWER = input("And are you ready to order?\n>>>")
    WAITED = True

if WAITED:
    prixtext()
    time.sleep(5)
    winetext()
    time.sleep(5)

APP, MAIN, DESSERT, WINE = order()

print("Thank you for your order.  The kitchen will start on it right away.")
time.sleep(15)
if WINE != 0:
    print("Here's your wine, " + WINE)
time.sleep(15)
if APP != 0:
    print("Here is your appetizer.  Enjoy your " + APP)
time.sleep(15)
if MAIN != 0:
    print("Here is the main course.  Enjoy your " + MAIN)
time.sleep(30)
if DESSERT != 0:
    print("I have dessert for you, " + DESSERT + " is a great choice!")
time.sleep(10)
print("Here is your check.  I do hope you enjoyed your meal.")
time.sleep(10)
input("How will you be paying this evening?")
print("Thank you.  I will return in a moment.")
time.sleep(60)

GOODBYE = textwrap.wrap("And here is your receipt.  "
                        "Thank you so much for joining us at G.O.A.T, and "
                        "we hope to see you back here soon.")
print_wrap(GOODBYE)

'''Did not include revisions mentioned in feedback.'''
