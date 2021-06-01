## Shree !! 
## BLACK JACK GAMES
import random
#import art
#from replit import clear

#print(art.logo)

#Flag to Check game status
is_game_over=False

# Select a card randomly
def get_a_card():
  cards = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
  return random.choice(cards)

#get card value
def get_card_value(card):
  cards_dct = {
  "A" : 11,
  "J" : 10,
  "Q" : 10,
  "K" : 10,
  }
  if  type(card) != int:
       return cards_dct[card]
  else :
     return card
     
def calculate_score(cards):
 cards_value=0
 for card in cards:
    cards_value = cards_value + get_card_value(card)
 return cards_value

user_cards =[]
dealer_cards =[]


def bj_game():
  user_cards = [get_a_card(), get_a_card()]
  print(f"user cards : {user_cards}")
  dealer_cards = [get_a_card(),get_a_card()]
  print(f"dealer cards : {dealer_cards}")
  user_score = calculate_score(user_cards)
  dealer_score = calculate_score(dealer_cards) 
  print(f"initial user score {user_score} , dealer score {dealer_score} ")

#Check for initial Black Jack
 
  if dealer_score == 21 :
    print("dealer wins !")
    is_game_over =True
    return is_game_over
  elif user_score == 21:
    print("user wins!")
    is_game_over =True
    return is_game_over
  # while is_game_over == False:
  user_response = input("Type 'y' to get another card, type 'n' to pass:")
  if user_response == "y" :
    user_cards.append(get_a_card())
    print(f"cards : {user_cards} ")
    if user_cards[len(user_cards)-1] == "A":
     if calculate_score(user_cards) > 21:
       user_cards[len(user_cards)-1] = 1      
    print(f"user cards sum  : {calculate_score(user_cards)} ")
  elif user_response == "n":
    print(f" dealers cards :{dealer_cards}")
    print(f" dealers cards :{calculate_score(dealer_cards)}")
    while calculate_score(dealer_cards) < 17:
      dealer_cards.append(get_a_card())
    print(f" dealers cards ** :{calculate_score(dealer_cards)}")

  print (f"final Dealer Sum :{calculate_score(dealer_cards)} , user Cards {calculate_score(user_cards)}")
  if calculate_score(dealer_cards) > calculate_score(user_cards) and not calculate_score(dealer_cards) >=21 and not calculate_score(user_cards) >=21:
    print(f"Delear Wins !")
    is_game_over =True
    return is_game_over
  else:
    print(f"User Wins !")
    is_game_over =True
    return is_game_over



def black_jack():
  # clear()
   flag= bj_game()
 


black_jack()

# # Initial User Cards 
# user_cards = [get_a_card(), get_a_card()]
# user_cards_sum = get_card_value(user_cards[0]) + get_card_value(user_cards[1])
# print(f"your cards: {user_cards}, Current Score = {user_cards_sum}")

# #Initial Dealer Card
# dealer_cards = [get_a_card(),get_a_card()]
# dealer_cards_value = get_card_value(dealer_cards[0])
# print(f"Dealer First card: {dealer_cards_value}")

# while is_game_over == False:
#   user_response = input("Type 'y' to get another card, type 'n' to pass:")
#   if user_response == "y" :
#     user_cards.append(get_a_card())
#     print(f"cards : {user_cards} ")
#     user_cards_sum = user_cards_sum +  get_card_value(user_cards[0])
#     print(f"cards sum  : {user_cards_sum} ")
#   elif user_response == "n":
#     print(f" dealers cards :{dealer_cards}")

#   if user_cards_sum > 21:
#     print("user lost")
#     is_game_over = True

#   if dealer_cards_value > 21:
#     print("dealer lost")
#     is_game_over = True

#   if  dealer_cards_value <=17 :
#     dealer_cards.append(get_a_card())
#     dealer_cards_value = dealer_cards_value + dealer_cards[2]

#   if dealer_cards_value > user_cards_sum : 
#     print("Dealer wins **")
#     is_game_over = True
#   else :
#     print("user lost **") 
#     is_game_over = True


























############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

