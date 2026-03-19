#--------------------14326--------------------
a = []
for N in range(1,1000):
    binary = bin(N)[2:]
    if binary.count("1") % 2 == 0:
        binary = "10" + binary[2:] + "0"
    else:
        binary = "1" + binary[:-2] + "10"
    R = int(binary,2)
    if R < 224:
        a.append(N)
print(max(a))
#---------------------------------------------