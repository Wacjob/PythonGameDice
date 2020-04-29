import random

def roll(sides):

    value = random.randint(1,sides)

    return value

# test dice

dice = (4, 6, 8, 10, 12, 20, 100)
diceText = ("four", "six", "eight", "ten", "twelve", "twenty", "percentile")
        
j = 0

for sides in dice:
    for i in range(20):
        print(f"A {diceText[j]} sided die: {roll(sides)}")
        i += 1
    j += 1
