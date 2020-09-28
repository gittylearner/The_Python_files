import random
import string
import re


print("Random Pwd Generator")

#generating list1 consisting of upper & lower case alphabets and numbers
###lower_alpha = list(string.ascii_lowercase)
###up_alpha = list(string.ascii_uppercase)
###alpha = lower_alpha + up_alpha + num

pwd = []

list1 = list(string.ascii_uppercase) + list(string.ascii_lowercase) + list(string.digits)
spcl_chars = ["!","@","$","^","&","~"]

#random pwd length between 15 and 25
lgth1 = random.randint(15,30)

#random lenght for special chars
lgth2 = random.randint(1,6)

i = 0
copy1 = list1.copy()
while(i<lgth1):
    ele = random.choice(copy1)
    pwd.append(ele)
    #copy1 = copy1.remove(ele) ----  .remove() doesn't return any value so copy1 is NoneType Object
    copy1.remove(ele)
    i +=1

j = 0
copy2 = spcl_chars.copy()
while(j<lgth2):
    ele = random.choice(copy2)
    pwd.append(ele)
    copy2.remove(ele)
    j += 1

while(True):
    random.shuffle(pwd)  ## This method changes the original list/tuple/string, it does not return a new list/tuple/string.
    result = "".join(pwd)

    if (re.findall(("^[a-zA-Z]"),result)):  #check if pwd starts with an alphabet
        print("Your password is: \n",result)
        break
    else:
        continue
