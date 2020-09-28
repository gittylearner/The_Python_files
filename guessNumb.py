# Number Guessing Game
"""
The user is given 3 chances to guess the number right
"""

import random

print("This is a NUMBER GUESSING GAME.\n Guess a numb between 1 and 9!")

#generating a random number
ranNum = random.randint(1,9)


#defining the number of chances
chance = 1

print(ranNum)
          
while(chance <6):

    num =int(input("Guess " + str(chance) +"\n"))
    if (num == ranNum):
        print("Guess is right")
        break
    elif (num > ranNum):
        print("try a smaller number")
    else:
        print("try a bigger number")
    chance += 1

if (chance >5):
    print("You Lost the game! Good luck Next time")









