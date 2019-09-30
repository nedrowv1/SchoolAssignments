import random


class Card(object):
    """A single card, used in a deck
    attributes: suit, value, face"""

    def __init__(self, suit, value, face):
        """create a card of a given suit, value and face; when
        used with is_empty in a deck can be used to pre-set the deck"""
        self.suit = suit
        self.value = value
        self.face = face

    def __str__(self):
        return self.face + " of " + self.suit

    def __repr__(self):
        return self.face + " of " + self.suit

    def __gt__(self, other_card):
        return self.value > other_card.value

    def __lt__(self, other_card):
        return self.value < other_card.value

    def __eq__(self, other_card):
        try:
            return self.value == other_card.value
        except AttributeError:
            return False
        
    def facelookup(self):
        try:
            return IMAGES[self.face + self.suit]
        except KeyError:
            return IMAGES[self.face[0] + self.suit]


class Deck(object):
    """a deck of cards, also containing the dealt hands of the deck
    attributes: deck, hands"""

    def __init__(self, num_players=0, is_shuffled=False, is_empty=False):
        """num_players determines the number of hands to deal.
        zero default creates central card pool of 52 cards, 1 creates
        a single player deck of 52if is_shuffled is set to True, the saved
        deck will be already shuffled,if set to false, the deck will have
        to be shuffled manually if is_empty is set to True, an empty deck
        class will be created"""

        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        faces = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9',
                 '10', 'Jack', 'Queen', 'King']
        values = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.deck = []
        self.hands = []
        if not is_empty:
            for i in range(13):
                face = faces[i]
                value = values[i]
                for suit in suits:
                    self.deck.append(Card(suit, value, face))

            if is_shuffled:
                self.shuffle()

            if num_players > 1:
                self.deal(num_players)

    def __repr__(self):
        return self.deck

    def __str__(self):
        return str(self.deck)

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, index):
        result = self.deck[index]
        return result

    def __iter__(self, index):
        return self.deck[index]

    def shuffle(self):
        """shuffle self.deck"""
        return random.shuffle(self.deck)

    def deal(self, decks):
        """deal deck to player hands"""
        last_dealt = 0
        for a_player in range(decks):
            self.hands.append(Deck(is_empty=True))
        while len(self.deck) >= len(self.hands):
            for a_deck in range(len(self.hands)):
                self.hands[a_deck].deck.append(self.deck.pop(0))
                last_dealt = a_deck
        for a_card in range(len(self.deck)):
            self.hands[last_dealt].deck.append(self.deck.pop(0))
            last_dealt += 1

    def card(self):
        """return to top card of the deck"""
        return self.deck[0]

    def return_hands(self):
        """return the hands in the deck"""
        return self.hands

    def give_card(self, otherdeck):
        """give card from self deck to another deck, used for decks
        in self.hands"""
        otherdeck.deck.append(self.deck.pop(0))

    def move_card(self):
        """move top card in deck to the bottom,
        used for decks in self.hands"""
        self.deck.append(self.deck.pop(0))

def determine_card(deck, index):
    if len(deck) - 1 >= index + 2:
        return deck[index + 2]
    elif len(deck) - 1 >= index + 1:
        return deck[index + 1]
    else:
        try:
            return deck[index]
        except IndexError:
            return None
        
def declare_war(deck1, deck2, index):
    global game
    """a single declaration of war; when players card == computers card"""
    deck1_playedcard = determine_card(deck1, index)
    deck2_playedcard = determine_card(deck2, index)
    if deck1_playedcard == None:
        game = True
        WIN = False
        return None
    elif deck2_playedcard == None:
        game = True
        WIN = True
        return None
    if deck1_playedcard > deck2_playedcard:
        if len(deck2) <= 3:
            game = True
        for a_card in range(index + 3):
            try:
                deck1.move_card()
                deck2.give_card(deck1)
                WIN = True
            except IndexError:
                pass
    elif deck1_playedcard < deck2_playedcard:
        if len(deck1) <= 3:
            game = True
        for a_card in range(index + 3):
            try:
                deck2.move_card()
                deck1.give_card(deck2)
                WIN = False
            except IndexError:
                pass
    else:
        declare_war(deck1, deck2, index + 3)
    return None

    print("Your card: ", deck1_playedcard, ". Their card: ", deck2_playedcard)
    win = ""
    if deck1_playedcard > deck2_playedcard:
        print("War: You win!")
        for a_card in range(index + 3):
            try:
                deck1.move_card()
                deck2.give_card(deck1)
                print("You got card: ", deck1[-1])
            except IndexError:
                pass
        win = True
    elif deck1_playedcard < deck2_playedcard:
        print("War: You lose!")
        for a_card in range(index + 3):
            try:
                deck2.move_card()
                deck1.give_card(deck2)
                print("You lost card: ", deck2[-1])
            except IndexError:
                pass
        win = False
    return win


def new_game():
    """play card game: War"""
    global game
    game_deck = Deck(2, True)
    hands = game_deck.return_hands()
    player_deck = hands[0]
    computer_deck = hands[1]
    cont = False

    while player_deck and computer_deck:
        if not cont:
            play = input("Play a card (press enter to play a single round, "
                         "'continue' to play through, 'exit' to exit)")

            if play == "continue":
                cont = True
            elif play == "exit":
                exit()

        card_index = -2
        print("Your card: ", player_deck.card(), ". Their card: ",
              computer_deck.card())
        if player_deck.card() == computer_deck.card():
            declare_war(player_deck, computer_deck,
                                  card_index + 3)
        elif player_deck.card() > computer_deck.card():
            player_deck.move_card()
            computer_deck.give_card(player_deck)
            print("You've won the round!")
        else:
            computer_deck.move_card()
            player_deck.give_card(computer_deck)
            print("You've lost the round")
        if len(player_deck) == 1 and player_deck.card() == computer_deck.card():
            player_deck.give_card(computer_deck)
        elif len(computer_deck) == 1 and computer_deck.card() == player_deck.card():
            computer_deck.give_card(player_deck)
            
    if not computer_deck:
        return True
    else:
        return False
