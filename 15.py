#--------------------9545--------------------
def del10(x):
    return x % 10 == 0
def del26(x):
    return x % 26 == 0

for A in range(1000):
    fits = True
    for x in range(1000):
        if (del10(x) and del26(x) and (x>=300)) <= (A <= x): continue
        fits = False
        break
    if fits:
        print(A)
#--------------------------------------------