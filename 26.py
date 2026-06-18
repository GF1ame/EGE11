#--------------------23765--------------------
f = open("Files/26_tasks/26_23765.txt")
N = f.readline()

products = []
rating = []
temp = {}
counter = 0
for i in f:
    counter += 1
    a,b = i.split()
    a,b = int(a),int(b)
    minProduct = min([a,b])
    name = "cx"
    if b > a:
        name = "sg"
    products.append([minProduct,name,counter])
products = sorted(products)

start = []
end = []
for i in products:
    if i[1] == "cx":
        start.append(i[2])
    else:
        end = [i[2]] + end


general = start + end

lastIndex = products[-1][2]
counter = 0
for i in general:
    counter += 1
    if lastIndex == i:
        break
print(products[-1][2])
print(counter-1)

#--------------------30401--------------------

f = open("Files/26_tasks/26_30401.txt")
storageAmount,peopleAmount = map(int,f.readline().split())

storages = []
people = []

indexedPeople = []

for i in range(storageAmount):
   cell = list(map(int,f.readline().split()))
   cell = [cell[1],cell[0]]
   storages.append(cell+[[0]]+[i+1])

for i in range(peopleAmount):
    people.append(list(map(int,f.readline().split())))
for i in range(len(people)):
    indexedPeople.append(people[i][:2]+[i]+people[i][-2:])

storages = sorted(storages)
indexedPeople = sorted(indexedPeople)

lastCells = []

amount = 0
for i in indexedPeople:
    for j in storages:
        if j[1] == i[-1] and j[0] >= i[3] and j[2][-1] < i[0]:
            amount += 1
            j[2].append(i[1])
            if i[0] == 1430:
                lastCells.append(j[-1])
            break
print(amount,lastCells)
#---------------------------------------------