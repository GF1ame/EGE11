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

#--------------------28776--------------------

clA = [[],[]]
clB = [[],[],[]]

for s in open("Files/27_tasks/27A_28766.txt"):
    x,y,t = [d for d in s.replace(",",".").split()]
    x,y = float(x),float(y)
    a,b,c = t[0],t[1],t[2:]
    if y > 10:
        clA[0].append([x,y,a+c])
    else:
        clA[1].append([x,y,a+c])


for s in open("Files/27_tasks/27B_28766.txt"):
    x,y,t = [d for d in s.replace(",",".").split()]
    x,y = float(x),float(y)
    a,b,c = t[0],t[1],t[2:]
    if y>22:
        clB[0].append([x,y,a+c])
    elif x > 22:
        clB[1].append([x,y,a+c])
    else:
        clB[2].append([x,y,a+c])

def centr(cl):
    m = []
    for p in cl:
        s = sum(dist(p[:2],p1[:2]) for p1 in cl)
        m.append([s,p])
    return min(m)[1]

worstCluster = min([[len(i),i] for i in clA])[1]

centrOfWorstCluster = centr(worstCluster)
maxLength = 0
minLenght = 99999

for cl in clA:
    for i in cl:
        if i[2] == "YIII":
            maxLength = max(maxLength, dist(centrOfWorstCluster[:2],i[:2]))
            minLenght = min(minLenght, dist(centrOfWorstCluster[:2],i[:2]))
print(int(maxLength*10000))
print(int(minLenght*10000))

zi = []
for cls in clB:
    for cl in cls:
        if cl[2] == "ZI":
            a = sorted([dist(cl[:2],cl1[:2]) for cl1 in cls if cl1[2]=="ZI"])
            if len(a) > 1:
                zi.append(a[1])
print(int(min(zi)*10000))

yellowGiants = []

for cls in clB:
    a = len([cl for cl in cls if cl[2] == "ZI"])
    yellowGiants.append([a,cls])
print(int(dist(centr(min(yellowGiants)[1])[:2],centr(max(yellowGiants)[1])[:2]) * 10000))

#--------------------19647--------------------

clA = [[],[]]
clB = [[],[],[]]

a27 = open("Files/27_tasks/27A_19647.txt")
b27 = open("Files/27_tasks/27B_19647.txt")

rA = a27.readline().split()[0]
rB = b27.readline().split()[0]

skip = 0
for s in a27:
    if skip == 0:
         skip = 1
         continue
    x,y = [float(d) for d in s.replace(",",".").split()]
    if x > 4:
        clA[0].append([x,y])
    else:
        clA[1].append([x,y])

for s in b27:
    if skip == 1:
        skip = 0
        continue
    x,y = [float(d) for d in s.replace(",",".").split()]
    if x < 10.5:
        clB[0].append([x,y])
    elif y < 18:
        clB[1].append([x,y])
    else:
        clB[2].append([x,y])
b = [[float(i) for i in j.split()] for j in b27]

def centr(cl):
    m = []
    for c in b:
        s = sum(dist(c,cl1) for cl1 in cl)
        m.append([s,c])
    return min(m)[1]

cn1 = centr(clB[0])
cn2 = centr(clB[1])
cn3 = centr(clB[2])
a = [[9.3076, 21.1009], [13.0057, 15.9721], [12.2501, 24.1383]]
print(centr(a))





#---------------------------------------------