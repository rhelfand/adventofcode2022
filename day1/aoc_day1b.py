

calories = 0
elfcals = []

with open("input.txt") as myfile:
    for myline in myfile:
        if myline == "\n":
            elfcals.append(calories)
            calories = 0
        else:
            calories += int(myline)

#sortlist = sorted(elfcals, reverse=True)
#print(sortlist)
# Same as above, but cleaner?
# print(sorted(elfcals, reverse=True))

sortlist = sorted(elfcals, reverse=True)
print(f'Top three elves calorie total = {sortlist[0] + sortlist[1] + sortlist[2]}')
