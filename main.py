from replit import clear
from art import logo

print(logo)
#HINT: You can call clear() to clear the output in the console.
print("Welcome to the secret auction program.")


bidder_dic = {}
bidding_finished = False

while not bidding_finished:
    name = input("What's your name?\n")
    bid = int(input("What's your bid?\n"))
    bidder_dic[name] = bid
    is_again = input("Are there any other bidders? Type 'yes' or 'no' \n")
    if is_again == 'no':
      bidding_finished = True
      highest = 0
      for key, value in bidder_dic.items():
        if bidder_dic[key] > highest:
          highest = bidder_dic[key]
          name = key
      print(f"The winner is {name} with a bid {highest}")
