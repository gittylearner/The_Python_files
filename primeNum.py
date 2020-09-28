

print("\n Prime Number Calculator")

proceed = True

def primeOrnot():
    i = 2
    qot = int(numb/2)

    while(i < qot):
        mod = numb%i
        if (mod == 0):
            print("The numb %d is not prime"%numb)
            qot = int(numb/i)
            print("{} * {} = {}\n".format(qot,i,numb))
            break
        i += 1

    if(i == qot):
        print("The numb {} is prime".format(numb))

#play again ?
def askContinue():
    resume = input("Do you want to check another number? (Y/N)").lower()

    if (resume == "y") or (resume == "yes"):
        return True
    elif (resume == "n") or (resume == "no"):
        return False
    else:
        return askContinue()

def askNumb():
    numb1 = int(input("\n Enter the number:  "))
    return numb1

#main function
while(proceed):
    numb = int(input("\n Enter the number:  "))
    primeOrnot()
    proceed = askContinue()
