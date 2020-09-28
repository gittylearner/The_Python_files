import random
import string
import re


"""
Password Generator:
 Generates a random pas4
 sword for the user. 
 Ask the user how long they want their password to be, 
 and how many letters and numbers they want in their password. 
 Have a mix of upper and lowercase letters, as well as numbers and symbols. 
 The password should be a minimum of 6 characters long.
"""

print("\n PASSWORD GENERATOR")

pwd = ""
low = ""
up = ""
dig = ""
spl_char = ("!","@","$","&","^")
#length of the pwd

lgth = 0
num = 0
chars = 0

while (lgth<6) or (lgth == 6) or (lgth>20):
    lgth = int(input("Specify the length of the pwd. Should be more than 6 or less than 20! \n"))

while (num==0):
    num = int(input("Specify the number of digits \n"))

while (chars == 0):
    chars = int(input("Specify the numb of special characters \n"))

j = random.randint(1,3)
#print(j)
alpha = lgth - (num+chars) - j

#generating lowercase alphabets
i = 0
while(i<alpha):
    low = random.choice(string.ascii_lowercase)
    if low in pwd:
        continue
    else:
        pwd = pwd + low
        i += 1

#generating 2 uppercase alphabets. can randomise the j value to keep the uppercase random.
#works best if j value is generated in the beginning

while not (j==0):
    up = random.choice(string.ascii_uppercase)
    if up.lower() in pwd:   #to eliminate repetition of alphabet
        continue
    else:
        pwd = pwd + up
        j -= 1

#generating numbers
n = 0
while(n < num):
    dgt = str(random.randint(0,9))
    if dgt in pwd:
        continue
    else:
        pwd = pwd + dgt
        n += 1

#generating special characters
c = 0
while(c<chars):
    ch = random.choice(spl_char)
    if ch in pwd:
        continue
    else:
        pwd = pwd + ch
        c += 1


# shuffling the elements
#converting the str to list as str is immutable = TypeError: 'str' object does not support item assignment
#also verifying that the first char is not a special char

list1 = list(pwd)

print(pwd)

while(True):
    random.shuffle(list1)
    if (list1[0] in string.ascii_lowercase) or (list1[0] in string.ascii_uppercase):
        break
    else:
        continue

new_pwd = "".join(list1)
print(new_pwd)

"""
#can also use the below method. 

list1 = random.sample(pwd,len(pwd))

"""
