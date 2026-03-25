#--------------------16264--------------------
f = open("Files/17_tasks/17_16264.txt")
a = [int(i) for i in f]
minimumKratn = 0

def countNumbers(number):
    counter = 0
    for i in str(number):
        counter += int(i)
    return counter


for i in sorted(a):
    if len(str(i)) != 2: continue
    if i % countNumbers(i) == 0:
        minimumKratn = i
        break

maxSum = 0
amount = 0
for i in range(len(a) - 1):
    if a[i] % 36 != 0 and a[i+1] % 36 != 0: continue
    if a[i] + a[i+1] > maxSum:
        maxSum = a[i] + a[i+1]
    amount += 1
print(amount,maxSum)
#--------------------21712--------------------

x = [int(i) for i in open("Files/17_tasks/17_21712.txt")]
minPlus = 0
a = []
def isGood(x):
    return 1000 <= abs(x) <= 9999 and abs(x) % 10 == 6

mn = min(i for i in x if i > 0 and isGood(i))

for i in range(len(x)-2):
    trio = [x[i],x[i+1],x[i+2]]
    quadCount = 0
    for z in trio:
        if len(str(abs(z)))==4 and str(abs(z))[-1]=="6":
            quadCount += 1
    if quadCount != 1: continue
    if sum(trio) > mn: continue
    a.append(sum(trio))

print(len(a),max(a))

#---------------------------------------------