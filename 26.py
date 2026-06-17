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