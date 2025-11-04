import logo
print(logo.logo)

bids = {}  # To store the bidder and his/her bids
continue_bidding = True  # Condition to stop the bid


def find_highest_bidder(bids_dictionary):  # To find the highest bidder name and his bid
    bidder_name = ""  # Bidder name changes as loop runs and his bid is greater than highest_bid
    highest_bid = 0  # Stores the highest bid of a bidder as loop runs
    for bidder in bids:  # Loop to find highest bid and their name
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            bidder_name = bidder
    print(f"\nThe winner is {bidder_name} with the bid of ${highest_bid}.")


while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid? $"))
    bids[name] = price  # Adding bidder name and his bid to dictionary
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)  # Calling function to find highest bid and their name
    elif should_continue == "yes":
        print("\n"*100)  # To make the bid of previous person invisible
