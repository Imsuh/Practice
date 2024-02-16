import random

print("Coin Toss App \n")

random_int = random.randint(0, 1)
if random_int == 1:
    print("You got heads")
else:
    print("You got tails")
