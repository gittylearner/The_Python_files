import random
import string
from random_words import RandomWords

#r = RandomWords()
words = ["dragons", "pillows", "brushes","bimbos","velocity","flowers","brownie","sunscreen","bicycle","cartwheel","philosopher","bunglow"]

print("HANGMAN")
print("\nThe Rules")
print("""1. A random word is chosen by the computer
2. You have to guess the letters, and hence the word
3. You lose a turn if you guess a letter incorrectly.
4. The game allows for 6 incorrect guesses.
""")



#play first round and then ask the user if to continue playing for subsequent rounds
def play():
    global chance

    while(chance<6):
        letter_check()



#function to check the letter
def letter_check():
    global chance
    global win

    if (chance<6) and (hangman == word1):
        (print("\nYou win"))
        win += 1
        return True


    elif (chance >6):
        print("\n\nThe word was ","".join(word1))
        print("\nYou lost")
        return False

    else:
        guess_ele = input("\nguess a letter:  ").lower()

        if guess_ele in (string.ascii_lowercase) and (guess_ele != ""):
            if guess_ele in guess:
                print("You have already tried this letter \n")

            elif (guess_ele not in word1):
                print("You guessed wrong!! You have %d chances left" % (5 - chance))
                chance += 1

            else:
                for idx,ele in enumerate(word1):
                    if (guess_ele == ele) and (hangman[idx] == "*"):
                        hangman[idx] = ele
                    else:
                        continue
                print("".join(hangman))

            guess.append(guess_ele)

        else:
            print("Not a letter!\n")

condition = True

t = 0
win = 0

while(condition):

    word1 = list(random.choice(words))
    len1 = len(word1)
    guess = []
    chance = 0

    hangman =list("*"*len1)

    print("\n")
    print("".join(hangman))
    print("\nIt is a %d letter word" %len1)

    play()
    t += 1

    #chance = 0
    resume = input("Would you like to play another round? (Y/N)").lower()

    if not resume:
        #condition = False
        print("Hope you had fun")
        print("Total games: ",t)
        print("total wins: ",win)
        condition = False

