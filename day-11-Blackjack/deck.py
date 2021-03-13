import random

class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = '♥♦♣♠'[suit] # 1,2,3,4 = ♥♦♣♠
        self.lines = [
        '┌───────┐',
        f'| {self.value:<2}    |',
        '|       |',
        f'|   {self.suit}   |',
        '|       |',
        f'|    {self.value:>2} |',
        '└───────┘']

    # def build_card(self):
    #     line1 = '┌───────┐'
    #     line2 = f'| {self.value:<2}    |'
    #     line3 = '|       |'
    #     line4 = f'|   {self.suit}   |'
    #     line5 = '|       |'
    #     line6 = f'|    {self.value:>2} |'
    #     line7 = '└───────┘'
        # return f' {line1} \n {line2} \n {line3} \n {line4} \n {line5} \n {line6} \n {line7} '
        # return [line1,line2,line3,line4,line5,line6,line7]
        
    def __str__(self):
        return f"{self.value}-{self.suit}"





# card_values = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
card_values = [2, 3, 4]

deck_dict = {}
deck = []
# building actual 52 card deck
# build the dict and list, not sure which will be more useful
for value in card_values:
    for i in range(0,4):
        new_card = Card(value, i)
        # print(new_card.lines)
        deck.append(new_card)
#       # build the deck{} with instances of card class. {instance of class: value} 
        # -- redundant because the class instance already contains value so no need to save it
        deck_dict[Card(value, i)] = value
for i in range(0,7):
    line = ""
    for card in deck:
        line = line + card.lines[i]
    print(line)


# # change the values of  J Q K to 10 and leave the A for later
# for key in deck_dict:
#     if type(deck_dict[key]) == str and deck_dict[key] != "A":
#         deck_dict[key] = 10

    # print(deck_dict[key])

# check to see that face cards got changed to 10
# print(list(deck_dict.values()))    
# prints random card from deck_dict
# print(random.choice(list(deck_dict.keys())))
#get deck_dict length
# deck_len = len(deck_dict)

deck_keys = []
deck_values = []
deck_items = deck_dict.items()
for item in deck_items:
    deck_keys.append(item[0]), deck_values.append(item[1])

# print(deck_keys[0])
# print(deck_values)










def blank_card():
    line1 = '┌───────┐'
    line2 = '|///////|'
    line3 = '|///////|'
    line4 = '|///////|'
    line5 = '|///////|'
    line6 = '|///////|'
    line7 = '└───────┘'
    return f' {line1} \n {line2} \n {line3} \n {line4} \n {line5} \n {line6} \n {line7}'
blank_card = blank_card()
# print(blank_card)









# print the deck list
# for card in deck:
#     print(f'{card}  \n')
    
# prints 4 random cards from deck
# for i in range(0,4):
#     print(random.choice(deck))

# print(deck[1].self.value)













    # def build_card(self):
    #     print('┌───────┐')
    #     print(f'| {self.value:<2}    |')
    #     print('|       |')
    #     print(f'|   {self.suit}   |')
    #     print('|       |')
    #     print(f'|    {self.value:>2} |')
    #     print('└───────┘') 