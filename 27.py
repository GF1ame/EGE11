#--------------------25439--------------------
clA = [[],[]]

for s in open("Files/27_tasks/27A_25439.txt"):
    x,y = [float(d) for d in s.replace(",",".").split()]
    if y > 25 or x > 15: 
        pass
    elif y > 15:
        clA[0].append([x,y])
    else:
        clA[1].append([x,y])

clB = [[],[],[]]

for s in open("Files/27_tasks/27B_25439.txt"):
    x,y = [float(d) for d in s.replace(",",".").split()]
    if x < -2 or x > 0:
        pass
    elif y>5:
        clB[0].append([x,y])
    elif x < -1:
        clB[1].append([x,y])
    else:
        clB[2].append([x,y])

from math import *

def centr(cl):
    m = []
    for p in cl:
        s = sum(dist(p,p1) for p1 in cl)
        m.append([s,p])
    return min(m)[1]
print(int(min([centr(i)[0] for i in clA])*10000))
print(int(min([centr(i)[1] for i in clA])*10000))

a = [len(cl) for cl in clB]
print(min(a))
print(max(a))
#--------------------25440--------------------
clA1 = [[],[]]

for s in open("Files/27_tasks/27A_25440.txt"):
    x,y = [float(d) for d in s.replace(",",".").split()]
    if x < -5 or y < -20: 
        pass
    elif y > 6:
        clA1[0].append([x,y])
    else:
        clA1[1].append([x,y])

clB1 = [[],[],[]]

for s in open("Files/27_tasks/27B_25440.txt"):
    x,y = [float(d) for d in s.replace(",",".").split()]
    if x < -2 or x > 0:
        pass
    elif y>5:
        clB1[0].append([x,y])
    elif x < -1:
        clB1[1].append([x,y])
    else:
        clB1[2].append([x,y])

from math import *

def centr(cl):
    m = []
    for p in cl:
        s = sum(dist(p,p1) for p1 in cl)
        m.append([s,p])
    return min(m)[1]
print(int(max([centr(i)[0] for i in clA1])*10000))
print(int(max([centr(i)[1] for i in clA1])*10000))

absciss = [centr(cl)[0] for cl in clB]
ordinat = [centr(cl)[1] for cl in clB]
print(int(sum(absciss)/len(absciss)*10000))
print(int(sum(ordinat)/len(ordinat)*10000))



# print(min(a))
# print(max(a))
#---------------------------------------------