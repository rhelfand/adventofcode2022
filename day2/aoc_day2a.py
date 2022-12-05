
# opponent - A = rock ; B = paper ; C = scissors
# me       - Y = paper ; X = rock ; Z = scissors

# score is my selection    - 1 for Rock, 2 for Paper, and 3 for Scissors
# plus                     - 0 for loss, 3 for a draw, and 6 for a win

totalscore = 0

with open("input.txt") as myfile:
    for myline in myfile:
        myline = myline.strip()
        elf, me = myline.split(" ")
        #print(elf, me)
        if elf == "A":
            match me:
                case "Y":
                    totalscore += 8
                case "X":
                    totalscore += 4
                case "Z":
                    totalscore += 3
        if elf == "B":
            match me:
                case "Y":
                    totalscore += 5
                case "X":
                    totalscore += 1
                case "Z":
                    totalscore += 9
        if elf == "C":
            match me:
                case "Y":
                    totalscore += 2
                case "X":
                    totalscore += 7
                case "Z":
                    totalscore += 6

print(totalscore)

