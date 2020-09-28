
import random

print("Rock, Paper, Scissors, Spock, Lizard!!")
print("""To play the game follow the instructions as below: \n
Choose the number associated with your choice of attack:\n
-----------------------------------------------------------
1. Rock \n
2. Paper \n
3. Scissors \n
4. Spock \n
5. Lizard \n
-----------------------------------------------------------
The computer will then make its choice. The rules to win are as below: \n
Rock crushes Scissors and crushes Lizard \n
Paper covers Rock and disproves Spock \n
Scissors cuts Paper and decapitates Lizard \n
Spock vaporises Rock and smashes Scissors \n
Lizard eats Paper and poisons Spock 
""")

game_ele = {"rock":"1","paper":"2","scissors":"3","spock":"4","lizard":"5"}
win = (-4,-2,1,3)
t = 0
w = 0
l = 0

def askContinue():
    inputStr = input("\nDo you want to play another round? (Y/N)").lower()
    print("-"*80)
    if (inputStr == "n") or (inputStr == "no"):
        return False
    elif (inputStr =="y") or (inputStr == "yes"):
        return True
    else:
        askContinue()

while(True):

    p1 = int(input("\nEnter your choice!\n"))

    while (True):
        if not(0<p1<6):
            p1 = int(input("\nEnter a valid choice!\n"))
        else:
            break
    
    p2_act,p2_num = random.choice(list(game_ele.items()))
    p2 = int(p2_num)

    for action,numb in game_ele.items():
        if p1 == int(numb):
            print("\nYou chose " + action)

    print("\nPlayer2 chose " + p2_act)

    if (p1 == p2):
        print("\nNo one wins this round")
    elif (p1-p2) in win:
            print("\nYou win")
            w += 1  #win counter
    else:
            print("\nYou lost")
            l += 1  #lost counter

    #total counter
    t += 1
    
    proceed= askContinue()

    if not proceed:
        break


#choice = False
print("Thank you for playing! \n Total games played: ",t)
print("Total games won: ",w)
print("Total games lost: ", l)
print("Total games drawn: ",t - (w+l))
