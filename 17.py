f = open("Files/17_tasks/17_2.txt")
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