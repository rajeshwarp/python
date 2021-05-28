import random
print("Welcome to number guessing game !!")
computer_no = random.randint(1,101)
HARD_LEVEL_LIFE = 5
EASY_LEVEL_LIFE = 10

#print(computer_no)

def getattempts(level):
    if level == "HARD":
       return  HARD_LEVEL_LIFE
    elif level == "EASY":
        return EASY_LEVEL_LIFE
    else:  return  "NVI" 

def guess_a_no():
    return input("please enter a number: ")

def validateno(number):
    if number > computer_no:
        return 1
    elif number < computer_no:
        return  -1
    elif number == computer_no:
        return 0

def gusser():
    level = input("Please select a Level ,  Hard or Easy: ").upper()
    user_attempts =  getattempts(level)
    while user_attempts > 0:
        user_number=int(guess_a_no())
        code= validateno(user_number)
        if code == 0:
            print(f"you guessed it correctly : {user_number}")
            return
        elif code == 1:
            user_attempts -= 1
            print(f"number greater then  computer ")
        elif code == -1:
            print(f"number smaller then  computer ")
            user_attempts -= 1
        print(f"number of attempts left {user_attempts} ")
        
    print(f"Your ran out of attempts, cerrect number is {computer_no}")

gusser()
