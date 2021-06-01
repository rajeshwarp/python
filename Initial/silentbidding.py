
#HINT: You can call clear() to clear the output in the console.
#import art
#print(art.logo)

# ---  
bidder = {}
bidder_list = []

stop_bidding = False
maxBid = 0

while stop_bidding == False:
  name = input("Please Enter Your Name: ")
  bidding_amount = input("Please Enter Your Bidding amount : ")
  bidder[name] = bidding_amount
  #bidder_list.append(bidder)
  
  continuebid = input("Do you have another Bidder ,  enter yes to continue OR no to end bidding: ")

  if continuebid == "no":
    stop_bidding = True
    
print(bidder)

for name in bidder:
    if int(bidder[name]) > int(maxBid):
        maxBid = bidder[name]
        winnername = name

print(f"{winnername} wins the bid with Bidding amount INR: {maxBid}")
    
    
    