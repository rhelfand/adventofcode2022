
import pandas as pd

fullinput = pd.read_fwf('input.txt', header=None, infer_nrows=8)
stackmap = fullinput.head(8)

stack1 = [ x for x in stackmap[0].values.tolist() if str(x) != 'nan' ]
stack2 = [ x for x in stackmap[1].values.tolist() if str(x) != 'nan' ]
stack3 = [ x for x in stackmap[2].values.tolist() if str(x) != 'nan' ]
stack4 = [ x for x in stackmap[3].values.tolist() if str(x) != 'nan' ]
stack5 = [ x for x in stackmap[4].values.tolist() if str(x) != 'nan' ]
stack6 = [ x for x in stackmap[5].values.tolist() if str(x) != 'nan' ]
stack7 = [ x for x in stackmap[6].values.tolist() if str(x) != 'nan' ]
stack8 = [ x for x in stackmap[7].values.tolist() if str(x) != 'nan' ]
stack9 = [ x for x in stackmap[8].values.tolist() if str(x) != 'nan' ]

stack1 = stack1[::-1]
stack2 = stack2[::-1]
stack3 = stack3[::-1]
stack4 = stack4[::-1]
stack5 = stack5[::-1]
stack6 = stack6[::-1]
stack7 = stack7[::-1]
stack8 = stack8[::-1]
stack9 = stack9[::-1]

mapper = {'1': stack1, '2': stack2, '3': stack3, '4': stack4, '5': stack5, '6': stack6, '7': stack7, '8': stack8, '9': stack9}

with open('input.txt', 'r') as myfile:
    for myline in range(10):
        myfile.readline()
    for myline in myfile:
        myline = myline.rstrip()
        linelist = myline.split(' ')
        popcount = int(linelist[1])
        slicer = -popcount
        mapper[linelist[5]].extend(mapper[linelist[3]][slicer:])
        for c in range(popcount):
            crate = mapper[linelist[3]].pop()

for key in mapper:
    print(mapper[key])
