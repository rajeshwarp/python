## Shree !! 
## BLACK JACK GAMES
import random
import os


user_cards =[]
dealer_cards =[]
user_score = 0
dealer_score = 0

def welcome():
  os.system("cls")
  #name= input("Please Enter Your Name: ")
  blackjacklogo = """
  .------.            _     _            _    _            _    
  |A_  _ |.          | |   | |          | |  (_)          | |   
  |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
  | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
  |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
  `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
        |  \/ K|                            _/ |                
        `------'                           |__/           
  """
  print(f" !! Shree Ganesha !!\nWELCOME TO BLACK JACK !!\n{blackjacklogo}")
  


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
    print("Black Jack !! dealer wins !")
    return True
  elif user_score == 21:
   # user_win = True
    print("Black Jack !! user wins!")
    return True
  elif user_score > 21:
    print("Black Jack !! dealer wins !")
    return True
  elif dealer_score > 21 :
    #user_win = True
    print("Black Jack !! user wins!")
    return True
  else: return False

#Check for Final Verdict
def final_verdict(user_cards, dealer_cards):
  user_score = calculate_score(user_cards)
  dealer_score = calculate_score(dealer_cards)
  user_win = False
  print (f"Final Dealer Cards :{dealer_cards} Sum: {dealer_score} \nFinal User Cards :{user_cards} Sum: {user_score}")
  if user_score > 21:
      user_win =False
  elif dealer_score > 21:
      user_win =True 
  elif user_score > dealer_score:
      user_win = True
  elif user_score == dealer_score:
       user_win ="Draw"

  if user_win == True:
    print(f"User Wins !")
  elif user_win == False:
    print(f"Dealer Wins!")
  else : print("its a draw :|")
      

#Game Logic
def lets_play_blackjack():

  is_game_over=False
  user_cards = [get_a_card(), get_a_card()]
  dealer_cards = [get_a_card(),get_a_card()]
  #print(f"dealer cards : {dealer_cards}")
  print(f"user cards : {user_cards}")
  print(f"dealer cards : [{dealer_cards[0]},*]")
  user_score = calculate_score(user_cards)
  dealer_score = calculate_score(dealer_cards) 

  print(f"initial user score {user_score} , dealer score {dealer_score} ")
#Check for black Jack Condition
  if check_blackjack(dealer_score, user_score):
        is_game_over = True
        return
    

  while is_game_over == False:
    user_response = input("Type 'y' to get another card, type 'n' to pass:")
    #User Playing
    if user_response == "y" :
        user_cards.append(get_a_card())
       # print(f"cards : {user_cards} ")
        # Checkinf if "Ace" appears and User Score gets > 21 substitute by 1
        if user_cards[len(user_cards)-1] == "A":
         if calculate_score(user_cards) > 21:
            user_cards[len(user_cards)-1] = 1    
        user_score =  calculate_score(user_cards)
        if user_score >= 21:
           is_game_over = True
           final_verdict(user_cards,dealer_cards)
           return
       # print(f"user cards sum  : {calculate_score(user_cards)} ")
    #Computer Playing
    elif user_response == "n":
        while calculate_score(dealer_cards) < 17 :
            dealer_cards.append(get_a_card())
        dealer_score = calculate_score(dealer_cards) 
        if dealer_score >= 21:
           is_game_over = True
           final_verdict(user_cards,dealer_cards)
           return
          # print(f" dealers cards ** :{calculate_score(dealer_cards)}")
        is_game_over = True 

#Final Results
  final_verdict(user_cards,dealer_cards)
    
#Call the game function
def go():  
  welcome()
 # userInput = input("Play : P , Stop : S")        
  while input("Play : P , Stop : S =>").capitalize() == "P":
     lets_play_blackjack()

go()
