## Shree !! 
## BLACK JACK GAMES
import random

user_cards =[]
dealer_cards =[]
user_score = 0
dealer_score = 0

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

# Calculate Scores 
def calculate_score(cards):
 cards_value=0
 for card in cards:
    cards_value = cards_value + get_card_value(card)
 return cards_value

#Check for BlackJack
def check_blackjack(dealer_score, user_score):
  if dealer_score == 21 :    
    print(" Black Jack !! dealer wins !")
    return 
  elif user_score == 21:
    user_win = True
    print("Black Jack !! user wins!")
    return 
  elif user_score > 21:
    print("Black Jack !! dealer wins !")
    return
  elif dealer_score > 21 :
    user_win = True
    print("Black Jack !! user wins!")
    return
  else: return False


#Game Logic
def lets_play_blackjack():
  user_win = False
  is_game_over=False
  user_cards = [get_a_card(), get_a_card()]
  print(f"user cards : {user_cards}")
  dealer_cards = [get_a_card(),get_a_card()]
  #print(f"dealer cards : {dealer_cards}")
  print(f"dealer cards : [{dealer_cards[0]},*]")
  user_score = calculate_score(user_cards)
  dealer_score = calculate_score(dealer_cards) 
  print(f"initial user score {user_score} , dealer score {dealer_score} ")

  if check_blackjack(dealer_score, user_score):
      return

#Check for initial Black Jack 
#   if dealer_score == 21 :    
#     print(" Black Jack !! dealer wins !")
#     return 
#   elif user_score == 21:
#     user_win = True
#     print("Black Jack !! user wins!")
#     return 
#   elif user_score > 21:
#     print("Black Jack !! dealer wins !")
#     return
#   elif dealer_score > 21 :
#     user_win = True
#     print("Black Jack !! user wins!")
#     return
  
  while is_game_over == False:
    user_response = input("Type 'y' to get another card, type 'n' to pass:")
    #User Playing
    if user_response == "y" :
        user_cards.append(get_a_card())
        print(f"cards : {user_cards} ")
        if user_cards[len(user_cards)-1] == "A":
         if calculate_score(user_cards) > 21:
            user_cards[len(user_cards)-1] = 1    
        user_score =  calculate_score(user_cards)
        if user_score >= 21:
           is_game_over = True
        print(f"user cards sum  : {calculate_score(user_cards)} ")
    #Computer Playing
    elif user_response == "n":
        while calculate_score(dealer_cards) < 17 :
            dealer_cards.append(get_a_card())
        dealer_score = calculate_score(dealer_cards) 
        if dealer_score >= 21:
           user_win = True
           is_game_over = True
           print(f" dealers cards ** :{calculate_score(dealer_cards)}")
        is_game_over = True 

#Final Results
  user_score = calculate_score(user_cards)
  dealer_score = calculate_score(dealer_cards)
  print (f"Final Dealer Cards :{dealer_cards} Sum :{dealer_score} /n, Final User Cards :  {dealer_score}")
  if user_score > 21:
      user_win =False
  elif dealer_score > 21:
      user_win =True 
  elif user_score > dealer_score:
      user_win = True
  elif user_score == dealer_score:
       user_win =False

  if user_win == True:
    print(f"User Wins !")
  elif user_win == True:
    print(f"Dealer Wins!")
  else : print("its a draw :|")
   
#Call the game function
lets_play_blackjack()


