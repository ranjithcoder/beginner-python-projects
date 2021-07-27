import random

chances = 5

def UserGuess(x):
    secretNum = random.randint(1,x)
    guess = 0
    while guess != secretNum and chances:
        guess = int(input("enter guessed number:"))
        if guess>secretNum:
            print("sorry! too low  you have more",chances-1,"chances to guess")
        elif guess<secretNum:
            print("sorry!! too high you have more",chances-1,"chances to guess")
    if chances == 0:
        print("chances over you lost the correct number is",secretNum)
    else:
        print("Hurry you gueesed correctly")

def ComputerGuess(x):
    low = 1
    high = x
    result = ''
    while result != 'c' and chances:
        guess = random.randint(low,high)
        print(guess)
        result=input("enter result l for low ,h for high:")
        if result == 'l':
            low = guess+1
        elif result == 'h':
            high = guess-1
    if chances==0:
        print("oops chances over i lost")
def Guessgame(x):
    print("1.let computer guess the number\n2.i will guess the number")
    option = int(input("enter your choice:"))
    if option==1:
        ComputerGuess(x)
    else:
        UserGuess(x)

x = int(input("enter a number:"))      
Guessgame(x)

     
