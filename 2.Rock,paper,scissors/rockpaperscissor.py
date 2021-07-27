
import random

def gameStart(rounds):
    Upoints=0
    Cpoints=0
    r=1
    while rounds-r>0:
        user = input("whats your choice? r for rock,s for scissors,p for paper:")
        comp = random.choice(['r','s','p'])
        if comp == user:
            print('it is a tie')
        #rules:rock>scissor scissor>paper paper>rock
        elif iswin(user,comp):
            Upoints+=2*r
            print(f'you won this round\ncurrent scores user:{Upoints},computer:{Cpoints}')
        else:
            Cpoints+=2*r
            print(f'you lost this round\ncurrent scores user:{Upoints},computer:{Cpoints}')
        r=r+1
    if(Upoints>Cpoints):
        print("congrats you are the winner")
    elif(Upoints<Cpoints):
        print("You lost")
    else:
        print("It is a tie")

def iswin(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False
print("every round winners get twice the round number points\nincase of tie no points")
rounds = int(input("enter max rounds number to held:"))

gameStart(rounds)
