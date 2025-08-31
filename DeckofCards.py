# Christopher Rhyan Poole
# DeckofCards
# CIS261

import random
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self):
        self.deck = [Card(rank, suit) for suit in self.SUITS for rank in self.RANKS]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, n):
        """Deal n cards from the top of the deck and return them as a list."""
        n = min(max(n, 0), len(self.deck))
        dealt = self.deck[:n]
        self.deck = self.deck[n:]
        return dealt

    def count(self):
        return len(self.deck)

def  get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")

def main():
    print("Card Dealer\n")
    deck = Deck()
    deck.shuffle()
    print(f"I have shuffled a deck of {deck.count()} cards. \n")

    want = get_int("How many cards would you like?: ")
    if want > deck.count():
        print(f"\nOnly {deck.count()} cards remain. Dealing all of them. \n")
        want = deck.count()

    dealt = deck.deal(want)

    print("\nHere are your cards:")
    for c in dealt:
        print(str(c))

    print(f"\nThere are {deck.count()} cards left in the deck.\n"
    print("Good luck!")
    input("Press any key to continue . . .")


if __name__ == "__main__":
    main()
