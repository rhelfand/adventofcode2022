
stringcount = 0
received = []

with open("input.txt") as myfile:
    for myline in myfile:
        myline = myline.rstrip()
        for c in myline:
            stringcount += 1
            received.append(c)
            lastfour = received[-4:]
            if stringcount > 4:
                if len(set(lastfour)) == len(lastfour):
                    print(stringcount)
                    break



