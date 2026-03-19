# f = open("Files/9_tasks/9_3.txt")
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
# for x in f:
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


# f = open("Files/9_tasks/9_5.txt")

# summa = []
# counter = 0
# for x in f:
#     x = sorted(map(int,x.split()))
#     if len(x) != len(set(x)) : continue
#     if (2 * (x[0]+x[-1])) != sum(x[1:4]):continue
#     counter += 1
# print(counter)