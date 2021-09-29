# this is the same as coin_count, just without the meth library

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
    cents = cents + (5 - cents % 5) if cents % 5 >= 3 else cents - cents % 5

outCoins = []

for i in range(6):
    temp = cents // coins[i]
    cents = cents // coins[i]
    
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