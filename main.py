import random
CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♦︎"]

deck_of_cards = [f"{card}{suit}" for card in CARDS for suit in SUITS]

# Implement a solution for shuffling a deck of cards without using random.shuffle()
# Using randint() is ok

def shuffle_deck(deck_of_cards):
    hand_cards = []
    deck_cards_copy = deck_of_cards[:]
    
    while len(hand_cards) < 10:
        random_card_index = random.randint(0, len(deck_cards_copy)-1)
        hand_cards.append(deck_cards_copy[random_card_index])
        deck_cards_copy.pop(random_card_index)
    
    return hand_cards

print(shuffle_deck(deck_of_cards))
        
