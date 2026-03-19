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
for i in sorted(found)[:10]:
    print(i,i//39)
