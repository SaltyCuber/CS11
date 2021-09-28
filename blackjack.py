import random

cards_dealt = 0

def shuffle(deck):
    if deck == []:
        deck = []
    global cards_dealt
    cards_dealt = 0
    random.shuffle(deck)
    return deck

def deal_hand(deck):
    dealer = []
    player = []
    player.append(deal_card(deck))
    dealer.append(deal_card(deck))
    player.append(deal_card(deck))
    dealer.append(deal_card(deck))

def deal_card(deck):
    card = deck.pop(0)
    global cards_dealt
    cards_dealt += 1
    if cards_dealt/52 >= 0.6:
        deck = shuffle(deck)
    return card

def end_hand(dealer, player, deck):
    deck = deck + dealer + player
    return(deck)