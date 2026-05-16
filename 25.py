#--------------------4114---------------------
from itertools import product
import time
found = {

}
digits = ["0","1","2","3","4","5","6","7","8","9"]
for a0,a1,a2,a3,a4 in product(digits,repeat=5):
    digit = f'{a0}{a1}{a2}{a3}{a4}'
    for i in range(10):
        number = int("12"+digit[:i]+"6789")
        if number%39 == 0 < 10:
            found[number] = number // 39
print("-------4114-------")
for i in sorted(found)[:10]:
    print(i,i//39)
#--------------------7601---------------------
from itertools import product
digits = [0,1,2,3,4,5,6,7,8,9]
a = []
for n1,n2,n3,n4 in product(digits,repeat = 4):
    digit = f'{n1}{n2}{n3}{n4}'
    for x in range(1,10):
        for y in range(1,10):
            for z in range(5):
                newDigit = int(f'12{x}{y}36{digit[:z]}1')
                if newDigit % 273 == 0:
                    if newDigit in a: continue
                    a.append(newDigit)
print("-------7601-------")
for i in sorted(a)[:10]:
    print(i,i//273)

#--------------------27635--------------------

from fnmatch import *

m = []
for i in range(0,10**8,171):
    if fnmatch(str(i),"1*23??56"):
        m.append(i)

for i in range(len(m)):
    print(m[i],m[i]/171)

#--------------------28711--------------------
print("-------28711-------")
counter = 0
def mnoj(n):
    d=[]
    i=2
    while i**2<=n:
        while n%i==0: 
            d.append(i)
            n=n//i
        i+=1
    if n>1:
        d.append(n)
    return d
for n in range(2400001, 2400001+1000000):
    if counter == 5: break
    d=mnoj(n)
    d1=[int(x) for x in d if (str(x).count('4')>=1) or (str(x).count('7')>=1)]
    if len(d1)==len(d)==3 and len(d)==len(set(d)):
        counter += 1
        print(n, max (d),d)

#--------------------28710--------------------
# print("-------28710-------")
# counter = 0
# def mnoj(n):
#     d=[]
#     i=2
#     while i**2<=n:
#         while n%i==0: 
#             d.append(i)
#             n=n//i
#         i+=1
#     if n>1:
#         d.append(n)
#     return d
# for n in range(3600001, 3600001+1000000):
#     if counter == 5: break
#     d=mnoj(n)
#     d1=[int(x) for x in d if (str(x).count('3')>=1) and (str(x).count('5')>=1)]
#     if len(d1)==len(d)==3:
#         counter += 1
#         print(n, max (d),d)

#--------------------28709--------------------
print("-------28709-------")
counter = 0
def mnoj(n):
    d=[]
    i=2
    while i**2<=n:
        while n%i==0: 
            d.append(i)
            n=n//i
        i+=1
    if n>1:
        d.append(n)
    return d
for n in range(6300001, 6300001+1000000):
    if counter == 5: break
    d=mnoj(n)
    d1=[int(x) for x in d if (str(x).count('3')>=1) or (str(x).count('4')>=1)]
    if len(d1)==len(d)==3:
        counter += 1
        print(n, max (d),d)

#--------------------28708--------------------
print("-------28708-------")
counter = 0
def mnoj(n):
    d=[]
    i=2
    while i**2<=n:
        while n%i==0: 
            d.append(i)
            n=n//i
        i+=1
    if n>1:
        d.append(n)
    return d
for n in range(8929999,1,-1):
    if counter == 5: break
    d=mnoj(n)
    if len(d) != 3: continue
    d1=[int(x) for x in d if (str(x).count('3')>=1)]
    if len(d1) == 1 and len(d)==len(set(d)):
        counter += 1
        print(n, d1[0],d)

#--------------------28707--------------------
print("-------28707-------")
counter = 0

def solver(n):
    pokazatel = 0
    found = False
    for i in range(0,10):
        for j in range(0,3000,2):
            if n == (7**i + j**2):
                pokazatel = i
                found = True
                break
    if not found: return
    return pokazatel


for n in range(8699999,1,-1):
    if counter == 5: break
    strN = str(n)
    if strN.count('1') == 0 and strN.count("3") == 0: continue
    pokazatel = solver(n)
    if not pokazatel: continue
    counter += 1
    print(n,pokazatel)

    

#---------------------------------------------
