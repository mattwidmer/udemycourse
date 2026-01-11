#secret auction
#initializing a dictionary
bids = {}

#functions
def get_bidder_info():
    bidder_name = input("What is your name? ")
    bid_value = input("What is your bid? $")
    bidder_name = bidder_name.strip()
    bid_value = int(bid_value.strip())
    return bidder_name, bid_value

def get_should_continue():
    should_continue = input("Are there more bidders? Y/N: ")
    should_continue = should_continue.strip().lower()
    return should_continue[0] == "y"

#get highest value from dictionary and return the name
def get_highest_bid():
    highest_bid = 0
    highest_bidder = "None"
    for bid in bids.items():
        name, value = bid
        if value > highest_bid:
            highest_bid = value
            highest_bidder = name
    return highest_bidder, highest_bid


print("Welcome to the blind auction!")
allow_more_bids = True
#only running the code when there are more expected bidders
while allow_more_bids == True:
    name, bid = get_bidder_info()
    bids[name] = bid
    allow_more_bids = get_should_continue()

name, value = get_highest_bid(bids)
print("Winner is " + name)
print("Winning bid is " + str(value))
