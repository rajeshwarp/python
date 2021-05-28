import logos
import game_data
import random
import os

#clear terminal
os.system('cls')
data = game_data.data

def generate_index():
    return  random.randint(0,len(data)-1)

def get_index2(index1):
    index2 = generate_index()
    while index2 == index1:
        index2 = generate_index()
    return index2

def print_item(index):
    return data[index]['name'] + " who is a " + data[index]['description'] + " from " + data[index]['country']

def print_question(index1, index2):
    print(f"Compare A : {print_item(index1)}")
    print(logos.vs)
    print(f"agaist B : {print_item(index2)}")

def validate(score,index1, index2):
    user_inut = input("who has more followers, type a for A or b for B \n")
    a_count = int(data[index1]["follower_count"])
    b_count = int(data[index2]["follower_count"])
    print(f"\n a's followers : {a_count} b's {b_count}\n")
     
    if a_count > b_count:
        index_to_be_returned = index1
        if user_inut == 'a':
            score += 1
            print(f"you are right, current score is {score}")
        else:
            print(f"you are wrong, current score remains {score}")
    elif a_count < b_count:
        index_to_be_returned = index2
        if user_inut == 'b':
            score += 1
            print(f"you are right, current score is {score}")
        else:
            print(f"you are wrong, current score remains {score}")
    elif a_count == b_count:
        score += 1
        index_to_be_returned = random.choice([index1, index2])
        print(f"both are equal , so you get benefit of doubt, current score is {score}")
    
    
    return [score,index_to_be_returned]

def play():
    score = 0;
    index1 = generate_index()
    
    while(input("do you want to play? y for yes \n") == 'y'):
        index2 = get_index2(index1)
        print_question(index1, index2)
        output = validate(score,index1, index2)
        score = output[0]
        index1 = output[1]

play()
