f = open('Files/24_tasks/24_28007.txt').readline()
f = f.replace(")(",") (")
x = f.split()
current = ""
maximum = ""
newList = []
for i in x:
    i = i.replace("("," ").replace(")"," ")
    splitted = i.split()
    for z in range(len(splitted)):
        if not splitted[z][0].isdigit():
            splitted[z] = ""
            continue
    newList += splitted
for i in newList:
    if i == "":
        if len(current) > len(maximum):
            maximum = current
        current = ""
        continue
    a = str(i).replace("+"," ").replace("-"," ").split()
    if len(a) != 2: continue
    if int(a[0]) % 5 == 0 or int(a[1]) % 5 != 0 or a[0][0] == "0" or a[1][0] == "0":
        if len(current) > len(maximum):
            maximum = current
        current = ""
        continue
    current += f'({a[0]}+{a[1]})'
print(len(maximum),maximum)
# for i in range(len(f)):
#     for x in range(i,len(f)-1):
#         print(f[x])
    

#--------------------1975--------------------
# f = open("Files/24_tasks/24_1.txt").readline()

# bestAmount = 0
# currentAmount = 0
# lastLetter = ""

# for i in range(len(f)-1):
#     if f[i] == f[i+1] == "P":
#         bestAmount = max(bestAmount,currentAmount)
#         currentAmount = 0
#     currentAmount += 1
#     lastLetter = f[i]
# print(bestAmount)
#--------------------------------------------