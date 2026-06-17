#--------------------27764--------------------
f = open("Files/9_tasks/9_27764.txt")
summa = []
counter = 0

for x in f:
    x = sorted(map(int,x.split()))
    if len(x) != len(set(x)) : continue
    if (2 * (x[0]+x[-1])) != sum(x[1:4]):continue
    counter += 1
# print(counter)
#--------------------2048--------------------
f = open("Files/9_tasks/9_2048.txt")
counter = 0
for x in f:
    x = list(map(int,x.split()))
    if sum(x) != 360: continue
    a,b,c,d = x[0],x[1],x[2],x[3]
    isTrapezoid = ((a + b == 180 and c+d == 180) or (b+c == 180 and d+a == 180))
    if not isTrapezoid: continue
    is_parallelogramm = (a == c and b == d)
    if not is_parallelogramm:
        counter += 1
# print(counter)
#--------------------28755--------------------
counter = 0
x = open("Files/9_tasks/9_28755.txt")
for i in x:
    i = list(map(int,i.split()))
    sortedI = sorted(i)
    if sum(sortedI[:-1]) <= sortedI[-1]: continue
    if sortedI[0] + sortedI[-1] == sortedI[1] + sortedI[2] or sortedI[0] + sortedI[2] == sortedI[1] + sortedI[-1]: continue
    counter += 1
#print(counter)

#--------------------18174--------------------

f = open("Files/9_tasks/9_18174.txt")

counter = 0

for i in f:
    i = sorted(list(map(int,i.split())))
    if len(set(i)) + 1 != len(i): continue
    minus = []
    plus = []
    for x in i:
        if x < 0:
            minus.append(x)
        else:
            plus.append(x)
    if abs(sum(minus)) > sum(plus):
        counter += 1
# print(counter) 

#--------------------29962--------------------

f = open("Files/9_tasks/9_29962.txt")
counter = 0
maxCounter = 0
for i in f:
    counter += 1
    i = list(map(int,i.split()))
    duplicates = []
    notDuplicates = []
    if any([i.count(j) == 3 for j in i]) and len(set(i)) == 5:
        for j in i:
            if i.count(j) > 1:
                duplicates.append(j)
            else:
                notDuplicates.append(j)
        if sum(notDuplicates)/4 > duplicates[0]:
            maxCounter = max(counter,maxCounter)
            print(duplicates,notDuplicates)
print(maxCounter)

#---------------------------------------------


#OTHER
# f = open("Files/9_tasks/9_3.txt")idk which one is this xd
# counter = 0
# for x in f:
#     x = sorted(list(map(int,x.split())))
#     coef1 = x[2] / x[1]
#     coef2 = x[1] / x[0]
#     if coef1 == coef2 and coef1 != 1:
#         counter += 1
# print(counter)

# f = open("Files/9_tasks/9_4.txt")

# summa = []
# for x in f:idk which one is this xd
#     x = sorted(list(map(int,x.split())))
#     if (x[0]**2) in x:
#         print(x)
#         summa.append(sum(x))
#         continue
#     counter = 0
#     tempDict = {}
#     for i in x:
#         if not tempDict.get(i):
#             tempDict[i] = 0
#         tempDict[i] += 1
#     for i in tempDict.values():
#         counter += i // 2
#     if counter < 3:continue
#     print(x)
#     summa.append(sum(x))
# print(min(summa))