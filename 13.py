from ipaddress import *

net = ip_network(f"235.86.56.0/255.255.248.0",0)

a = 0

for ip in net:
    format = str(ip).split(".")
    if bin(int(format[3]))[-2:] == "11":
        a += 1
# print(a)

net = ip_network(f"191.89.109.206/255.255.224.0",0)
bestIp = None
for ip in net.hosts():
    bestIp = ip
a = sum([int(i) for i in str(bestIp).split(".")])
# print(a)

counter = 0
net = ip_network("123.222.111.192/255.255.255.248",0)
for i in net:
    a = str(i).split(".")
    if bin(int(a[3]))[2:].count("0") % 3 != 0:
        print(bin(int(a[3]))[2:])
        counter += 1
print(counter)
    




from ipaddress import *

network = ip_network("190.202.83.62/255.255.252.0",0)

maxIp = 0
for x in network.hosts():
    x = str(x)
    maxIp = sum(list(map(int,x.split('.'))))
print(maxIp)