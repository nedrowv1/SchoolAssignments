import time
import war
import yacht
import hangman
import braingames
def printandwait(text):
    print(text)
    time.sleep(2)
def main():
    printandwait("...\nYou step down into a darkend hallway")
    printandwait("The air smells of cookies and Noxima")
    printandwait("Distantly a cat meows...")
    printandwait("You flip a switch, the light comes on...")
    printandwait("...")
    time.sleep(5)
    printandwait("The door stands before you...")
    printandwait("...\n...")
    printandwait("...You open it...")
    time.sleep(5)
    printandwait("A stack of boxes teeters precariously...")
    printandwait("You reach up to protect your face...")
    printandwait("...but all that falls is a deck of cards.")
    printandwait("Before you can react, the air shifts...")
    printandwait("...the game begins!")
    print("Welcome to War....")
    for i in range(10):
        print(">.><.<\n")
    while True:
        won = war.new_game()
        if won:
            break
        else:
            printandwait("Laughter drifts around you and the cards shuffle.")
            printandwait("You have no choice but to play again...")
            time.sleep(3)
            print("Welcome to War....")
            for i in range(10):
                print(">.><.<\n")
    printandwait("The cards settle to the ground, the game over.")
    printandwait("You've won.  Before you can take a breath,\n"
                 "another box begins to fall...")
    printandwait("You jump out of the way of the flying pencil.")
    printandwait("There's something written on the piece of paper\n"
                 "that falls from the lid...")
    time.sleep(2)
    printandwait("Win at 200, it says, scibbled in curly script.")
    printandwait("Win at 200? What could that mean?")
    printandwait("And then the dice begin to roll...")
    print("Welcome to Yacht....")
    for i in range(10):
        print("* ** *** **** ***** ******")
        print()
    while True:
        won = yacht.new_game()
        if won:
            break
        else:
            printandwait("Laughter drifts around you...")
            printandwait("...the dice jump back into the cup.")
            printandwait("You have no choice but to play again...")
            time.sleep(3)
            for i in range(10):
                print("* ** *** **** ***** ******")
                print()
    printandwait("The dice fall silent, the game over")
    printandwait("You've won.  Pushing the dice and papers away,\n"
                 "you see another box tumbling down")
    printandwait("You catch this one, a shoebox.")
    printandwait("The notebook falls out...")
    printandwait("The pen with it...")
    for i in range(10):
        print("O-<--<")
    while True:
        won, word, definition = hangman.new_game()
        if won:
            break
        else:
            printandwait("The laughter fills your ears.")
            printandwait("You'd swear the little line drawing of a man\n"
                         "on a gallows swings in an unfelt breeze")
            printandwait("You have no choice but to play again...")
            for i in range(10):
                print("O-<--<")
    printandwait("The pen settles,")
    printandwait("The word, {}, scribbled on the page".format(word))
    printandwait("It means {}".format(definition))
    printandwait("It's over.  It has to be over.")
    printandwait("But no...another box,")
    printandwait("all plastic and rought edges, tumbles down...")
    printandwait("...into your outstretched hands...")
    for i in range(10):
        print("o o o o o")
        print(" o o o o o")
    won = braingames.new_game()
    printandwait("The lights flicker, then steady.")
    printandwait("Around you is the detritus of games played")
    printandwait("Outside a storm settles...")
    printandwait("...from raging to light drizzle")
    printandwait("A woman's voice calls your name.")
    printandwait("You look up...")
    printandwait("Of course...")
    printandwait("This was just...")
    printandwait("Grandma's Game Closet")
    while True:
        game = input("Choose a game to play:\n"
                     "[W]ar\n"
                     "[Y]acht\n"
                     "[H]angman\n"
                     "[B]rain Games\n")
        if game.casefold() == "w".casefold():
            war.new_game()
        elif game.casefold() == "y".casefold():
            yacht.new_game()
        elif game.casefold() == "h".casefold():
            hangman.new_game()
        elif game.casefold() == "b".casefold():
            braingames.new_game()
        elif game.casefold() == "q".casefold():
            break
        
                         
if __name__ == "__main__":
    main()
