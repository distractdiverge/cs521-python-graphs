import math
import random


def split(n=10):
    powers = [random.randint(0, 4) for x in range(n)]

    coins = [math.pow(2, i) for i in powers]

    bonnie = []
    clyde = []

    coins.sort()

    while len(coins) > 0:
        coin = coins.pop()

        if sum(bonnie) >= sum(clyde):
            clyde.append(coin)
        else:
            bonnie.append(coin)

    print("Bonnie's Coin's: {0}".format(bonnie))
    print("Bonnie's Total: {0}".format(sum(bonnie)))

    print("Clyde's Coin's: {0}".format(clyde))
    print("Clyde's Total: {0}".format(sum(clyde)))


if __name__ == "__main__":
    split()