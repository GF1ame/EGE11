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
# print(int(min([centr(i)[0] for i in clA])*10000))
# print(int(min([centr(i)[1] for i in clA])*10000))

a = [len(cl) for cl in clB]
# print(min(a))
# print(max(a))
#--------------------25440--------------------
clA = [[],[]]

for s in open("Files/27_tasks/27A_25440.txt"):
    x,y = [float(d) for d in s.replace(",",".").split()]
    if x < -5 or y < -20: 
        pass
    elif y > 6:
        clA[0].append([x,y])
    else:
        clA[1].append([x,y])

clB = [[],[],[]]

for s in open("Files/27_tasks/27B_25440.txt"):
    x,y = [float(d) for d in s.replace(",",".").split()]
    if x < -2 or x > 0:
        pass
    elif y>5:
        clB[0].append([x,y])
    elif x < -1:
        clB[1].append([x,y])
    else:
        clB[2].append([x,y])


# print(int(max([centr(i)[0] for i in clA])*10000))
# print(int(max([centr(i)[1] for i in clA])*10000))

absciss = [centr(cl)[0] for cl in clB]
ordinat = [centr(cl)[1] for cl in clB]
# print(int(sum(absciss)/len(absciss)*10000))
# print(int(sum(ordinat)/len(ordinat)*10000))

#--------------------25441--------------------
clA = [[],[]]

for s in open("Files/27_tasks/27A_25441.txt"):
    x,y = [float(d) for d in s.replace(",",".").split()]
    if x < 0 or y < 5: 
        pass
    elif y > 15:
        clA[0].append([x,y])
    else:
        clA[1].append([x,y])

clB = [[],[],[]]

for s in open("Files/27_tasks/27B_25441.txt"):
    x,y = [float(d) for d in s.replace(",",".").split()]
    if x < -2 or x > 0:
        pass
    elif y>5:
        clB[0].append([x,y])
    elif x < -1:
        clB[1].append([x,y])
    else:
        clB[2].append([x,y])

# clasters = [centr(i) for i in clA]
# absciss = abs(int((clasters[0][0] - clasters[1][0]) * 10000))
# ordinat = abs(int((clasters[0][1] - clasters[1][1]) * 10000))
# a = {}
# for i in clB:
#     a[len(i)] = centr(i)
# print(int(dist(a[min(a)],a[max(a)])*10000))

# m = []
# for cl in (clB):
#         s = max([dist(centr(cl),p1) for p1 in cl])
#         m.append(s)
# print(int(max(m)*10000))


#--------------------25442--------------------
clA = [[],[]]

for s in open("Files/27_tasks/27A_25442.txt"):
    x,y = [float(d) for d in s.replace(",",".").split()]
    if x > 10: 
        pass
    elif y > 10:
        clA[0].append([x,y])
    else:
        clA[1].append([x,y])

clB = [[],[],[]]

for s in open("Files/27_tasks/27B_25442.txt"):
    x,y = [float(d) for d in s.replace(",",".").split()]
    if x < 10 or x > 40:
        pass
    elif y>16:
        clB[0].append([x,y])
    elif x > 24:
        clB[1].append([x,y])
    else:
        clB[2].append([x,y])
# print(int(dist(centr(clA[0]),centr(clA[1]))*10000))
p2 = []
for cl in clA:
    a = max([dist(centr(cl),d) for d in cl])
    p2.append(a)
# print(int(max(p2)*10000))
q = [
    dist(centr(clB[0]),centr(clB[1])),
    dist(centr(clB[0]),centr(clB[2])),
    dist(centr(clB[1]),centr(clB[2]))
]
# print(int(min(q)*10000))
# print(int(max(q)*10000))



#---------------------------------------------