import random
from replit import clear
import time
import art

class Card:
    def __init__(self,value,suit, face_value):
        self.face_value = face_value
        self.value = value
        self.face_down = False
        self.dealt = False
        self.ace = False
        self.suit = '♥♦♣♠'[suit] # 1,2,3,4 = ♥♦♣♠
        self.lines = [
            '┌───────┐',
            f'| {self.value:<2}    |',
            '|       |',
            f'|   {self.suit}   |',
            '|       |',
            f'|    {self.value:>2} |',
            '└───────┘']
        self.blank_lines = [
            '┌───────┐',
            '|///////|',
            '|///////|',
            '|///////|',
            '|///////|',
            '|///////|',
            '└───────┘']


# card values
card_values = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
# card face_values to compare later on A will be 11 until its not later
face_values = [2,3,4,5,6,7,8,9,10,10,10,10,11]
#the empty playing card deck.
deck = []
# building actual 52 card deck
for index, value in enumerate(card_values):
    for i in range(0,4):
        #create the deck[] with 52 class instances of Card. each entry is one distinct card
        deck.append(Card(value, i, face_values[index]))

# shuffle deck
random.shuffle(deck)

#will be passed an array of cards to print side by side.
def print_cards(cards):
    # loops over the 7 strings/ card
    for i in range(0,7):
        # will be the ith line of each card
        screen_line = ""
        for card in cards:            
            # make screen line = the ith line of all cards in array and then print that
            # individually to build the image. if the passed card is set to be dealt down,
            # the lines used will be the card attr "blank_lines" else, "lines"  
            screen_line += card.blank_lines[i] if card.face_down else card.lines[i]
        print(screen_line)

# will be called to add cards to hands, can pass in "True" to deal the card face 
# down(for dealers second card) they all default to face up.
def deal_card(face_down = False):
    #sets card = to the next card that has not been dealt.. searches deck for first card
    # that has "dealt" = False 
    card = next(card for card in deck if card.dealt == False)
    #set card attr facedown to false, unless true is passed in when called
    card.face_down = face_down
    #switch the card attr "dealt" to true so not dealt twice
    card.dealt = True
    return card

#will be passed an array of cards (player and dealer hands)
def calc_score(cards):
    score = 0
    for card in cards:
        # incrament the score + all cards in hand by adding card attr "face_value"
        score += card.face_value      
    return score

def print_readout():
    clear()
    print("##### DEALERS HAND #####")
    print_cards(dealer_hand)
    print("##### YOUR HAND #####")
    print_cards(player_hand)
    print(f' player score: {calc_score(player_hand)}')
    print(f' dealer score: {calc_score(dealer_hand)}') 

def face_down_print():
    clear()
    """prints out cards in hand and score with dealers second card and score hidden"""
    print("##### DEALERS HAND #####")
    print_cards(dealer_hand)
    print("##### YOUR HAND #####")
    print_cards(player_hand)
    print(f' player score: {calc_score(player_hand)}')
    print(f' dealer showing: {calc_score(dealer_hand) - dealer_hand[-1].face_value}')

def deal_hand():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card(True)]
    return player_hand, dealer_hand

# player_score = 0
# computer_score = 0
# player_hand = [deck[51], deck[28]]
# player_hand = [deal_card(), deal_card()]
# dealer_hand = [deal_card(), deal_card(True)]

game_on = True
while game_on == True:
    player_hand, dealer_hand = deal_hand()

    game_on = False
    hit = True
    while hit == True:

        
        face_down_print()

        if input("would you like to hit or stand (type 'hit' or 'stand'): ").lower() == "hit":
            player_hand.append(deal_card())

            print_readout()

            for card in player_hand:
                if card.value == "A" and calc_score(player_hand) > 21:
                    card.face_value = 1
            
            print_readout()
        
            if calc_score(player_hand) > 21:
                # if player hand is over 21 and holding ace, ace = 1 => continue drawing
                # ace = next(card for card in player_hand if card.value == "A")
                hit = False
                print(art.player_bust)
                if input("Hit enter to deal again") == "":
                    game_on = True
        else:
            time.sleep(1)
            for card in dealer_hand:
                card.face_down = False
            hit = False
            
            print_readout()

            while calc_score(dealer_hand) < 17:
                time.sleep(1)
                dealer_hand.append(deal_card())

                print_readout()

                for card in dealer_hand:
                    if card.value == "A" and calc_score(dealer_hand) > 21:
                        card.face_value = 1
                time.sleep(1)
        
            print_readout()

            if calc_score(player_hand) > calc_score(dealer_hand):
                print(art.win)
                time.sleep(2)
                if input("Hit enter to deal again") == "":
                    game_on = True
            elif calc_score(dealer_hand) > 21:
                print(art.dealer_bust)
                time.sleep(2)
                if input("Hit enter to deal again") == "":
                    game_on = True
            elif calc_score(player_hand) < calc_score(dealer_hand):
                print(art.lose)
                time.sleep(2)
                if input("Hit enter to deal again") == "":
                    game_on = True
            elif calc_score(player_hand) == calc_score(dealer_hand):
                print(art.push)
                time.sleep(2)
                if input("Hit enter to deal again") == "":
                    game_on = True
    

