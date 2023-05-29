# Secret Auction
# Allow users to bid on an item in secret, reveal winner when all bids have been entered
# 29/05/2023
import os
from art import logo
# os.system("cls")
bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    """ Find the highest bidder from the bids dict"""
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = int(bidding_record[bidder])
        if (bid_amount > highest_bid):
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is: {winner}, with a bid amount of ${highest_bid}")


print(logo)
while not bidding_finished:
    name = input("Please enter name: ")
    price = input("what is your bid? $")
    bids[name] = price
    should_continue = input("Are there any other bidders? yes/no ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system("CLS")

input("\n\nPress enter to exit the program.")
