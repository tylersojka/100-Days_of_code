import art
from replit import clear

clear()
print(art.logo)
# empty dict for holding all input
auction_dict = {}

# flag to start the while loop
add_more = True

# build the name:bid dictionary to hold all the entries
while add_more == True:
    dict_name = input("What is your name?\n")
    dict_bid = int(input("What is your bid?\n"))

    auction_dict[dict_name] = dict_bid

    # flag to end the loop if no more people to enter
    next_person = input("Is there another person to bid? (Y/N)\n").lower()
    if next_person == "n":
        add_more = False

    clear()



    
# list to hold all the bids to then interate over and get the max
bid_list = []
for name in auction_dict:
    bid_list.append(auction_dict[name])

winning_bid = max(bid_list)

# function to parse auction_dict and get the key of the passed value
def get_key(val):
    for key, value in auction_dict.items():
        if val == value:
            return key
    
# call function to grab the key of the winning bid value and assign to winning name
winning_name = get_key(winning_bid)

# print results
print(f'{winning_name} is the winner with a bid of {winning_bid}!')

