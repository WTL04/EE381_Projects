import numpy as np
from collections import Counter


def createDeck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    deck = [(rank, suit) for rank in ranks for suit in suits]
    return deck

#bool function
def isFourOfAKind(hand):
    #checks ranks
    ranks = [card[0] for card in hand]
    #counts occurance of each rank, returns list of key=item, value=occurence
    rank_counts = Counter(ranks)
    #returns bool if occurance 4 is found
    return 4 in rank_counts.values()


#bool function
def drawAndCheck(deck, n=5):
    #randomly chooses n indices from deck without picking same one
    indices = np.random.choice(len(deck), n, replace=False)
    hand = [deck[i] for i in indices]
    return isFourOfAKind(hand)

#single experiment of drawing 5 and check
def experiment(N):
    deck = createDeck()
    successes = 0
    for i in range(0,N):
        if drawAndCheck(deck):
            successes+=1
    return successes

if __name__ == "__main__":
    N = 1000000
    successes = experiment(N)
    probability = successes/N
    print(f"Number of successes: {successes}")
    print(f"Probability : {probability}")