from random import shuffle

# define a new class for the hand
class Hand:
    def __init__(self):
        self.cards = []
    
    def score(self):
        score = 0
        for card in self.cards:
            match card:
                case "2"|"3"|"4"|"5"|"6"|"7"|"8"|"9"|"10":
                    score += int(card)
                case "J"|"Q"|"K":
                    score += 10
                case "A":
                    score += 1 if score >= 11 else 11
        return score
    
    def deal_card(self):
        global game_deck
        global cards_dealt
        card = game_deck.pop(0)
        self.cards += [card]
        cards_dealt += 1
        if cards_dealt/52 >= 0.6:
            print("Shuffling deck...\n")
            game_deck = deck_shuffle(game_deck)

    def card1_score(self):
        # get the score of card 1, used for getting the dealer's score during player's turn
        card = self.cards[0]
        match card:
                case "2"|"3"|"4"|"5"|"6"|"7"|"8"|"9"|"10":
                    score = int(card)
                case "J"|"Q"|"K":
                    score = 10
                case "A":
                    score = 11
        return score

def deck_shuffle(deck):
    if deck == []:
        # if deck has not been defined yet, define it as an unshuffled deck of cards
        deck = ["A","2","3","4","5","6","7","8","9","10","J","Q","K","A","2","3","4","5","6","7","8","9","10","J","Q","K","A","2","3","4","5","6","7","8","9","10","J","Q","K","A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    global cards_dealt
    cards_dealt = 0
    shuffle(deck)
    return deck

cards_dealt = 0
game_deck = deck_shuffle([])
p = Hand()
d = Hand()
while input("\nnew game? (y/n)\n") == "y":
    # start new game
    cont = True
    p.deal_card()
    d.deal_card()
    p.deal_card()
    d.deal_card()
    # check for any blackjacks
    if p.score() != 21 and d.score() != 21:
        # main game
        while cont:
            # player's turn
            print("\nYour Cards: {}, Score: {}".format(", ".join(p.cards), p.score()))
            print("Dealer's Cards: {}, Score: {}".format(d.cards[0], d.card1_score()))
            if input("(h)it or (s)tand?\n").lower() == "h":
                # add another card to the player's hand, detect whether to continue or not
                p.deal_card()
                if p.score() >= 21:
                    cont = False
            else:
                cont = False
        # dealer's turn
        print("\nYour Cards: {}, Score: {}".format(", ".join(p.cards), p.score()))
        print("Dealer's Cards: {}, Score: {}".format(", ".join(d.cards), d.score()))
        print()
        if p.score() <= 21:
            while d.score() < 17:
                d.deal_card()
                print("\nYour Cards: {}, Score: {}".format(", ".join(p.cards), p.score()))
                print("Dealer's Cards: {}, Score: {}".format(", ".join(d.cards), d.score()))
    else:
        print("\nYour Cards: {}, Score: {}".format(", ".join(p.cards), p.score()))
        print("Dealer's Cards: {}, Score: {}".format(", ".join(d.cards), d.score()))
    # detect who won
    match (p.score(), d.score()):
        case (ps, ds) if ps > 21:
            m = "Bust! Dealer Wins!"
        case (ps, ds) if ds > 21:
            m = "Bust! You Win!"
        case (ps, ds) if ps == ds:
            m = "Draw!"
        case (ps, ds):
            m = "You Win!" if ps > ds else "Dealer Wins!"
    print(m)
    # reset hands, put cards on bottom of deck
    game_deck += p.cards
    game_deck += d.cards
    p.cards = []
    d.cards = []
