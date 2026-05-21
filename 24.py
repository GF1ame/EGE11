
import time
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
f = open("Files/24_tasks/24_2420.txt").readline().replace("C"," ").replace("D"," ")

print(max([len(i) for i in f.split()]))
#--------------------2426---------------------
n = open("Files/24_tasks/24_2426.txt").readline().replace("A"," ").replace("B"," ").replace("C"," ")

print(max([len(i) for i in n.split()]))
#--------------------4682---------------------

n = open("Files/24_tasks/24_4682.txt").readline()

for i in "AE": n = n.replace(i,"+")
for i in "BCD": n = n.replace(i,"-")

mx = 1


#--------------------27777--------------------
from string import *

n = open("Files/24_tasks/24_27777.txt").readline()

for i in (ascii_uppercase + "0123456789"):
    if i.isdigit() or i == "A" or i == "B": continue
    n = n.replace(i," ")
print(max([len(i) for i in n.split()]))

#--------------------27634--------------------

n = open("Files/24_tasks/24_27634.txt").readline()


m = 2000
a = ""
zCounter = 0
bestLen = 99999

start1 = time.perf_counter()


for l in range(len(n)):
    for r in range(m+l,l,-1):
        a = n[l:r]
        if a.count("Z") < 270:break
        else: m = len(a) 
print(m)

end1 = time.perf_counter()
print(f"Время выполнения: {end1 - start1:.6f} секунд")

start2 = time.perf_counter()

for l in range(len(n)):
    a += n[l]
    if a[-1] == "Z": zCounter += 1        
    while zCounter >= 270:
        bestLen = min(bestLen,len(a))
        if a[0] == "Z": zCounter -= 1
        a = a[1:]
print(bestLen)

end2 = time.perf_counter()
print(f"Время выполнения: {end2 - start2:.6f} секунд")

#--------------------------------------------

l = 0
m = 0
n = open("Files/24_tasks/24-241.txt").readline()
for r in range(len(n)):
    if n[r] == "O" and n[l] == "O":
        while n[l:r].count("F") > 2:
            l += 1
        m = max(m,r-l+1)
    if n[l]!="O": l += 1
print(m)




         
#--------------------------------------------

