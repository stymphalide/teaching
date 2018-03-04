import random

colors = ["green","red","purple"]
shapes =["oval","rectangular","wave"]
numbers =["1","2","3"]
fillings =["empty","half","full"]

class Card(object):
    """docstring for Card"""
    def __init__(self, color,shape,number,filling):
        super(Card, self).__init__()
        self.color=color
        self.shape=shape
        self.number=number
        self.filling=filling
    def __str__(self):
        return self.color + self.shape + self.number + self.filling


def create_cards(colors,shapes,numbers,fillings):
    cards =[]
    for c in colors:
        for s in shapes:
            for n in numbers:
                for f in fillings:
                    cards.append(Card(c,s,n,f))
    return cards

cards = create_cards(colors,shapes,numbers,fillings)
sample = random.sample(cards,12)

print(sample)