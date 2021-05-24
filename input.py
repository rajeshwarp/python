print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
cost = 0
#Write your code below this line 👇
if(size == "S"):
  cost = 15
  if(add_pepperoni == "Y"):cost+2
elif  (size == "L"):
  cost =20
  if(add_pepperoni == "Y"):cost=+3
else: 
  cost=25
  if(add_pepperoni == "Y"):cost=+3

if(extra_cheese=="Y"):
  cost=+1

print(f"Please pay {cost} for your {size} pizza")