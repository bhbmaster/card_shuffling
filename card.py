# -*- coding: utf-8 -*-

# note: need above comment so that the unicode in the actual source code works -> https://www.python.org/dev/peps/pep-0263/
# sidenote: to run /Users/kkhlebop/.pyenv/versions/3.9.0/bin/python card.py

class Card:

    _suits = [ "HEART", "SPADE", "CLUB", "DIAMOND", "JOKER" ]
    _values = [ "ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", None ]
    __red_suits = [ _suits[0], _suits[3] ]  # heart and diamond
    __black_suits = [ _suits[1], _suits[2] ] # spade and club

    __str_heart = "♡"
    __str_spade = "♠"
    __str_club = "♣"
    __str_diamond = "♢"

    # note None goes with Joker
    def __init__(self, value, suit):

        """
        Accepted Inputs:
        
        value in [ "ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", None ]

        suit in [ "HEART", "SPADE", "CLUB", "DIAMOND", "JOKER" ]

        Output: Card object
        """

        # if number given as int convert number to str
        if type(value) is int:
            value = str(value)

        # values are lower case
        if type(value) is str:
            value = value.lower()
        
        # suits are upper case
        if type(suit) is str:
            suit = suit.upper()

        # check for valid values
        if value in self._values:
            self.value = value
        else:
            raise ValueError("unsupported value `"'"'f"{value}"'"'"`")

        # check for valid suit
        if suit in self._suits:
            self.suit = suit
        else:
            raise ValueError("unsupported suit `"'"'f"{suit}"'"'"`")

        # check for valid joker
        if suit == "JOKER" and value is not None:
            raise ValueError("Joker Fail -> value of '"'JOKER'"' must be suit of `None`")

        if value == None and suit != "JOKER":
            raise ValueError("Joker Fail -> suit of `None` must have value of `'"'JOKER'"'`")

    def __repr__(self): # used repr instead of str so that can get string out of obj and it works for str too

        # start with our values and suits as stored in data
        print_val = self.value
        print_suit = self.suit

        # modify suit to look better
        if self.suit == "HEART":
            print_suit = self.__str_heart
        if self.suit == "SPADE":
            print_suit = self.__str_spade
        if self.suit == "CLUB":
            print_suit = self.__str_club
        if self.suit == "DIAMOND":
            print_suit = self.__str_diamond

        # modify value to look better
        if self.value == "ace":
            print_val = "A"
        if self.value == "jack":
            print_val = "J"
        if self.value == "queen":
            print_val = "Q"
        if self.value == "king":
            print_val = "K"

        # modify joker to look better
        if self.suit == "JOKER":
            print_val = "JKR"
            print_suit = ""

        # return f"{print_suit}{print_val}"
        return f"{print_val}{print_suit}"

def test():

    # testing our produced cards
    print("TEST PRODUCTION OF ALL CARDS:\n")
    for i_s in Card._suits:
        for i_v in Card._values:
            print(i_s, i_v, "=", end=" ")
            try:
                TEST_CARD = Card(i_v, i_s)
            except Exception as e:
                print("FAIL:", e)
                continue
            print(TEST_CARD)

    # nice print
    print("\nPRINT ALL CARDS NICELY:\n")
    for i_s in Card._suits:
        for i_v in Card._values:
            try:
                TEST_CARD = Card(i_v, i_s)
            except:
                continue
            print(TEST_CARD, end="\t")
        print()

    # create deck clean deck no jokers
    print("\nCLEAN DECK (NO JOKERS):\n")
    clean_deck = []
    for i_s in Card._suits:
        for i_v in Card._values:
            try:
                CARD = Card(i_v, i_s)
            except:
                continue
            clean_deck.append(CARD)
    clean_deck.pop() # pop the last joker out
    print(len(clean_deck))
    print([i for i in clean_deck])

    # create normal deck w/ 2 jokers
    print("\nNORMAL DECK (2 JOKERS):\n")
    deck = []
    for i_s in Card._suits:
        for i_v in Card._values:
            try:
                CARD = Card(i_v, i_s)
            except:
                continue
            deck.append(CARD)
            if i_v == "JOKER": # if joker add it again for 2
                deck.append(CARD)
    print(len(deck))
    print([i for i in deck])

if __name__ == "__main__":
    test() # comment out if dont want tests
    pass

# EOF