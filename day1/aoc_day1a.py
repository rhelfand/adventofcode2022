

calories = 0
elfcals = []

with open("input.txt") as myfile:
    for myline in myfile:
        if myline == "\n":
            elfcals.append(calories)
            calories = 0
        else:
            calories += int(myline)

#print(elfcals)
print(max(elfcals))
