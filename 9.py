#--------------------27764--------------------
f = open("Files/9_tasks/9_27764.txt")
summa = []
counter = 0

for x in f:
    x = sorted(map(int,x.split()))
    if len(x) != len(set(x)) : continue
    if (2 * (x[0]+x[-1])) != sum(x[1:4]):continue
    counter += 1
print(counter)
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
print(counter)
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