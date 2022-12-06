
# opponent - A = rock ; B = paper ; C = scissors
# me       - Y = paper ; X = rock ; Z = scissors

# score is my selection    - 1 for Rock, 2 for Paper, and 3 for Scissors
# plus                     - 0 for loss, 3 for a draw, and 6 for a win

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.

totalscore = 0

with open("input.txt") as myfile:
    for myline in myfile:
        myline = myline.strip()
        elf, me = myline.split(" ")
        #print(elf, me)
        if elf == "A":
            match me:
                case "X":
                    totalscore += 3
                case "Y":
                    totalscore += 4
                case "Z":
                    totalscore += 8
        if elf == "B":
            match me:
                case "X":
                    totalscore += 1
                case "Y":
                    totalscore += 5
                case "Z":
                    totalscore += 9
        if elf == "C":
            match me:
                case "X":
                    totalscore += 2
                case "Y":
                    totalscore += 6
                case "Z":
                    totalscore += 7

print(totalscore)

