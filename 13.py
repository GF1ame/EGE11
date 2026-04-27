from ipaddress import *

net = ip_network(f"235.86.56.0/255.255.248.0",0)

a = 0

for ip in net:
    format = str(ip).split(".")
    if bin(int(format[3]))[-2:] == "11":
        a += 1
print(a)

net = ip_network(f"191.89.109.206/255.255.224.0",0)
bestIp = None
for ip in net.hosts():
    bestIp = ip
a = sum([int(i) for i in str(bestIp).split(".")])
print(a)

    
