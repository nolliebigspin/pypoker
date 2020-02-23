from card import Card
import random

class Carddeck:



    def __init__(self):
        self.colors = ["spade", "clover", "heart", "diamond"]
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.deck = []
        for color in self.colors:
            for number in self.numbers:
                self.deck.append(Card(color,number))

    
    def mix(self):
        random.shuffle(self)
        return self
