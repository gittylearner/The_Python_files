#ROCK PAPER SCISSORS GAME

import random

list1 = ["rock","paper","scissors"]

print("3 TURNS to play Rock, Paper Scissors. \n Let's begin!")

turn = 1

while(turn < 4):

    #Player's input
    print("Round ",turn)

    p1 = input("Rock, Paper or Scissors ? ").lower()
    p2 = random.choice(list1)
    print("Computer's choice is: " + p2)
    
    if (p1 == p2):
        print("No one wins this round!")
    else:
        if (p1=="rock"):
            if (p2=="scissors"):
                print("You Win!")
            else:
                print("You Lost!")
        elif (p1=="paper"):
            if (p2=="rock"):
                print("You Win")
            else:
                print("You Lost")
        elif (p1 == "scissors"):
            if(p2 == "paper"):
                print("You Win")
            else:
                print("You lost")
        else:
            print("Value incorrect! Try again")
    turn += 1


