# a = []
# for N in range(1000):
#     binary = bin(N)[2:]
#     if binary.count("0") % 2 == 0:
#         binary = "1" + binary + "1"
#     else:
#         binary = "10" + binary
#     R = int(binary,2)
#     if R < 100:
#         a.append(R)
# print(max(a))
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