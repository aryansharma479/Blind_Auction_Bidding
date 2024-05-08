from art import logo
from replit import clear

print(logo)
dict = {}
while True:
  choice = input("Do You Want To Bid? yes or no : ").lower()
  if choice == 'yes':
    name = input("Enter Your Name: ")
    bid = int(input("What's Your Bid:$ "))
    dict[name] = bid
    question = input("Are There Any More Bidders? yes or no: ").lower()
    if question == 'yes':
      clear()
      choice == 'yes'
    else:
      print(dict)
      high_bid = 0
      winner = ''
      for key in (dict):
        bid_amt = dict[key]
        if bid_amt > high_bid:
          high_bid = bid_amt
          winner = key
      print(f"The Bidder Is: {winner} With The Maximum Bid That Is {high_bid}")
      exit()

  elif choice == 'no':
    print(dict)
