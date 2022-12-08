
counter = 0

with open("input.txt") as myfile:
    for myline in myfile:
        myline = myline.strip()
        podlist = myline.split(',')
        pod_a = podlist[0].split('-')
        range_a = range(int(pod_a[0]), int(pod_a[1]) + 1)
        pod_b = podlist[1].split('-')
        range_b = range(int(pod_b[0]), int(pod_b[1]) + 1)
        if all(item in list(range_a) for item in list(range_b)) or all(item in list(range_b) for item in list(range_a)):
            counter += 1

print(counter)



