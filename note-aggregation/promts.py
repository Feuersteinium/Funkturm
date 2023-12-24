import random

fal = []

file = open("information.md", "r")


for loop in file:
    fal.append(loop)



print(fal[random.randrange(0, len(fal))])