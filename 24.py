#--------------------28007--------------------
f = open('Files/24_tasks/24_28007.txt').readline()
f = f.replace(")(",") (")
x = f.split()
current = ""
maximum = ""
newList = []

def saveState():
    global current
    global maximum
    if len(current) > len(maximum):
        maximum = current
    current = ""

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
        saveState()
        continue
    a = str(i).replace("+"," ").replace("-"," ").split()
    if len(a) != 2: continue
    if int(a[0]) % 5 == 0 or int(a[1]) % 5 != 0 or a[0][0] == "0" or a[1][0] == "0":
        saveState()
        continue
    current += f'({a[0]}+{a[1]})'
print(len(maximum))
#--------------------7688---------------------

t = open("Files/24_tasks/24_7688.txt").readline()
t = t.replace("TXA","^").replace("XA","*").replace("XY","*")
amount = 0
maxAmount = 0
lastDigit = ""
for x in t:
    if x == "*":
        amount += 2
    elif x == "^":
        amount+= 3
    else:
        maxAmount = max(maxAmount, amount)
        amount = 0
    lastDigit = x
print(maxAmount)

#--------------------1975---------------------
f = open("Files/24_tasks/24_1975.txt").readline()

bestAmount = 0
currentAmount = 0
lastLetter = ""

for i in range(len(f)-1):
    if f[i] == f[i+1] == "P":
        bestAmount = max(bestAmount,currentAmount)
        currentAmount = 0
    currentAmount += 1
    lastLetter = f[i]
print(bestAmount)
#--------------------2420---------------------
f = open("Files/24_tasks/24_2420.txt").readline().replace("A","*").replace("B","*").replace("E","*").replace("F","*")
counter = 0
bestCounter = 0
for i in range(len(f)-1):
    if f[i] == f[i+1] == "*":
        counter += 1
        continue
    bestCounter = max(bestCounter,counter)
    counter = 0
print(bestCounter)

#--------------------------------------------

# import time

# start = time.perf_counter()
# end = time.perf_counter()
# print(f"Время выполнения: {end - start:.6f} секунд")