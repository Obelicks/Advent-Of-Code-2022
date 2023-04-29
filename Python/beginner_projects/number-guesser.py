from random import randint
hidden = randint(1,10)
cheat = True
if cheat:
    print(hidden)
while(True):
    t = input("Pick a number between 1 and 10\n")
    if (int(t) == hidden):
        print("Correct! You rock!")
        break
    else:
        print("Wrong try again!") 