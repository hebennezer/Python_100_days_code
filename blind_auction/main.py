import os
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highes_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highes_bid:
      highes_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highes_bid:.2f}")
      
while not bidding_finished:
  name = input("What's your name?\n>>>> ")
  price = float(input("What's your bid?\n>>>> $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n>>>> ")
  if should_continue == "no":
    bidding_finished = True
    os.system("cls")
    find_highest_bidder(bids)
  elif should_continue == "yes":
    os.system("cls")

