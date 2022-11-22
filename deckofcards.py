import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print('{} of {}'.format(self.value, self.suit))


class Deck:
    def __init__(self):
        # Create an empty list for cards
        self.cards = []
        self.create_deck()

    def create_deck(self):
        for suits in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            for numbers in range(1, 14):
                if numbers == 11:
                    numbers = "Jack"
                if numbers == 12:
                    numbers = "Queen"
                if numbers == 13:
                    numbers = "King"
                if numbers == 1:
                    numbers = "Ace"
                self.cards.append(Card(suits, numbers))

    def shuffle_deck(self):
        for i in range(len(self.cards) - 1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def show(self):
        for c in self.cards:
            c.show()

    def get_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def show_hand(self):
        for c in self.hand:
            c.show()

    def draw(self):
        self.cards.append(Deck.get_card())
        return self


deck = Deck()
deck.shuffle_deck()
deck.show()