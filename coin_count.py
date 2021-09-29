import meth
# meth.py is a library I wrote to do math functions (+, -, //, *, %) in a similar way to how an actual cpu performs math functions using binary logic.
# the name comes from math, but since math.py is a default library I named it meth, which is fitting because I was high on meth when I wrote it.

coins = {0:200, 1:100, 2:25, 3:10, 4:5, 5:1}
names = {0:" toonie", 1:" loonie", 2:" quarter", 3:" dime", 4:" nickel"}
money = input("How much money do you have? format as '$XX.XX' or 'X' cents\n")

if money[0] == "$":
    money = float(money[1:])
    cents = int(money * 100)
else:
    cents = int(money)

money = cents/100

round = True if input("round pennies? (y/n)\n") == 'y' else False

if round:
    # rounds cents to the nearest nickel
    cents = meth.add(cents, meth.subtract(5, meth.divide(cents, 5)[1])) if meth.divide(cents, 5)[1] >= 3 else meth.subtract(cents, meth.divide(cents, 5)[1])

outCoins = []

for i in range(6):
    temp = meth.divide(cents, coins[i])[0]
    cents = meth.divide(cents, coins[i])[1]
    
    # this is really messy but it works, it makes sure the formatting of the line is gramatically correct.
    if i < 5:
        if temp == 0:
            outCoins = outCoins + [""]
        elif temp == 1:
            outCoins = outCoins + [("\n"+str(temp)+names[i])]
        else:
            outCoins = outCoins + [("\n"+str(temp)+names[i]+"s")]
    else:
        # of course there had to be just one coin that i can't just slap an 's' on the end of to make it plural
        if temp == 0:
            outCoins = outCoins + [""]
        elif temp == 1:
            outCoins = outCoins + [("\n"+str(temp)+" penny")]
        else:
            outCoins = outCoins + [("\n"+str(temp)+" pennies")]

rnd = ", rounded to the nearest nickel, " if round else " "

print("The least amount of coins to represent ${}{}is:{}".format(money, rnd, "".join(outCoins)))