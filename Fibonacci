

print("\n FIBONACCI SERIES")

range = int(input("How many numbers in the sequence? "))

n1 = 0
n2 = 1
sum = 0
count = 0
fibo_series = []

print("\n Sequence: \n")

#fibo series
def fibo():
    global n1
    global n2
    global sum

    sum = n1 + n2
    n1 = n2
    n2 = sum
    return sum


while(count <range):
    fibo_series.append(fibo())
    count += 1

print(fibo_series)
