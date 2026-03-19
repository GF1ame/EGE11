f = open("Files/24_tasks/24_1.txt").readline()

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
        