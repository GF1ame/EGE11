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

#---------------------------------------------
